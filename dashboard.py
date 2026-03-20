"""
Dashboard Page

Consumes data from global 'all-sites-store'
"""

from dash import html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import pandas as pd
from config import config


# import components
from src.components.navbar import create_navbar
from src.components.kpi_cards import create_kpi_section, create_single_kpi_card
from src.components.map_view import create_map_section
from src.components.site_table import create_site_table
from src.components.charts import create_charts_section, create_empty_charts_section
from src.components.filters import create_filter_panel

# data service (for site-specific data only)
from src.data import data_service

# =================== LAYOUT ===================
layout = dbc.Container(
    [
        # dbc.Alert("DASHBOARD LOADED", color="success"), # DEBUG TEST
        # page-specific stores
        dcc.Store(id="selected-site-store"),  # site user clicked
        dcc.Store(id="filtered-sites-store"),  # subset for map + table
        dcc.Store(id="national-stats-store"),  # derived KPIs
        # KPI cards
        create_kpi_section(),
        html.Hr(),
        # filter panel
        create_filter_panel(),
        html.Hr(),
        # map section
        create_map_section(),
        html.Hr(),
        # site table
        html.H3("BESS Deployments", className="mt-4 mb-3"),
        create_site_table(),
        html.Hr(),
        html.Div(
            id="charts-section",
            children=create_charts_section(),  # ALWAYS exists
            style={"display": "none"},  # hidden until site selected
        ),
    ],
    fluid=True,
    className="px-4",
)

# =================== DASHBOARD CALLBACKS ===================
# all callbacks read from 'all-sites-store' rather than calling data_service


# === Callback 1: update KPI cards ===
@callback(
    [
        Output("kpi-total-capacity", "children"),
        Output("kpi-operational", "children"),
        Output("kpi-construction", "children"),
        Output("kpi-duration", "children"),
        Output("national-stats-store", "data"),
    ],
    Input("all-sites-store", "data"),
)
def update_kpi_cards(all_sites):
    """
    Update KPI cards with latest statistics

    Triggers: Page load + every 30 seconds

    Returns:
    - 4 KPI card components
    - National stats dict
    """
    # get stats
    stats = data_service.get_national_stats(all_sites)
    if not all_sites:
        empty = create_single_kpi_card("", 0, "", "", "fas fa-spinner", "secondary")
        return empty, empty, empty, empty, {}

    # card 1: total capacity
    kpi_total = create_single_kpi_card(
        title="Total Capacity",
        value=stats["total_power_kW"],
        unit="kWh",
        subtitle=f"{stats['total_energy_kWh']:,.0f} KWH nationwide",
        icon="fas fa-bolt",
        color="success",
    )

    # card 2: operational sites
    kpi_operational = create_single_kpi_card(
        title="Operational Sites",
        value=stats["operational_sites"],
        unit="sites",
        subtitle=f"{stats['operational_power_kW']:,.0f} KW online",
        icon="fas fa-check-circle",
        color="success",
    )

    # card 3: under construction
    kpi_construction = create_single_kpi_card(
        title="Under Construction",
        value=stats["construction_sites"],
        unit="sites",
        subtitle=f"{stats['construction_power_kW']:,.0f} KW in pipeline",
        icon="fas fa-hard-hat",
        color="warning",
    )

    # card 4: average duration
    kpi_duration = create_single_kpi_card(
        title="Average Duration",
        value=stats["avg_duration_hours"],
        unit="hours",
        subtitle="Storage Capacity",
        icon="fas fa-clock",
        color="info",
    )

    return kpi_total, kpi_operational, kpi_construction, kpi_duration, stats


# === Callback 2: Populate filters ===
@callback(
    [
        Output("filter-state", "options"),
        Output("filter-technology", "options"),
    ],
    Input("all-sites-store", "data"),
)
def populate_filters(locations):
    """
    Fill filter dropdowns with options

    Triggers: Page load
    """
    if not locations:
        return [], []

    states = sorted(
        {loc.get("State/Province") for loc in locations if loc.get("State/Province") is not None}
    )
    techs = sorted(
        {
            loc.get("Storage Device Technology Mid-Type")
            for loc in locations
            if loc.get("Storage Device Technology Mid-Type") is not None
        }
    )

    return (
        [{"label": s, "value": s} for s in states],
        [{"label": t, "value": t} for t in techs],
    )


# === Callback 3: Filter Sites ===
@callback(
    [
        Output("filtered-sites-store", "data"),
        Output("filter-summary", "children"),
    ],
    [
        Input("all-sites-store", "data"),
        Input("filter-state", "value"),
        Input("filter-status", "value"),
        Input("filter-technology", "value"),
        Input("filter-min-capacity", "value"),
    ],
)
def filter_sites(all_sites, states, statuses, technologies, min_capacity):
    """
    Filter sites based on user selections

    Triggers: Any filter change
    """
    if not all_sites:
        return [], "no data"

    total_sites = len(all_sites)
    filtered = all_sites

    if states:
        filtered = [s for s in filtered if s["State/Province"] in states]

    if statuses:
        filtered = [s for s in filtered if s["Status"] in statuses]

    if technologies:
        filtered = [s for s in filtered if s["Storage Device Technology Mid-Type"] in technologies]

    if min_capacity:
        filtered = [
            s
            for s in filtered
            if s.get("Rated Power (kW)") is not None and s.get("Rated Power (kW)") >= min_capacity
        ]

    summary = f"showing {len(filtered):,} of {total_sites:,} sites"
    return filtered, summary


# === Callback 4: Reset filters ===
@callback(
    [
        Output("filter-state", "value"),
        Output("filter-status", "value"),
        Output("filter-technology", "value"),
        Output("filter-min-capacity", "value"),
    ],
    Input("reset-filters-btn", "n_clicks"),
    prevent_initial_call=True,  # dont run on page load
)
def reset_filters(n_clicks):
    """
    Clear all filters

    Triggers: Reset button click
    """
    return None, None, None, None


# === Callback 5: Update Map ===
@callback(Output("us-bess-map", "figure"), Input("filtered-sites-store", "data"))
def update_map(filtered_sites):
    """
    Create interactive map with BESS site markers

    Triggers:
        - when filtered sites change (from filters or page load)

    Creates:
        - plotly scattermapbox figure
        - colored markers by status
        - sized markers by capacity
        - hover text with site details

    Returns:
        - Plotly figure object
    """
    # print("Filtered Sites:", filtered_sites)  # Debugging line

    # --- Handle empty case ---
    if not filtered_sites or len(filtered_sites) == 0:
        # return empty map centered on US
        fig = go.Figure(
            go.Scattermapbox(
                lon=[],
                lat=[],
            )
        )

        fig.update_layout(
            mapbox=dict(
                style=config.MAP_STYLE,
                center=dict(lat=config.MAP_CENTER_LAT, lon=config.MAP_CENTER_LON),
                zoom=config.MAP_ZOOM,
            ),
            margin=dict(l=0, r=0, t=0, b=0),
            showlegend=False,
            height=config.MAP_HEIGHT,
        )

        return fig

    # --- Convert filtered_sites to DataFrame ---
    """
    valid_points = []
    for site in filtered_sites:
        lat = site.get("Lattitude")
        lon = site.get("Longitude")

        # skip NULL early
        if lat in [None, "", "NULL"] or lon in [None, "", "NULL"]:
            continue

        try:
            lat = float(lat)
            lon = float(lon)
        except:
            continue

        power = float(site.get("Rated Power (kW)", 0) or 0)
        status = site.get("Status", "Unknown")
        name = site.get("Project/Plant Name", "Unknown")

        # colors
        if status == "Operational":
            color = config.COLOR_OPERATIONAL
        elif status == "Under Construction":
            color = config.COLOR_CONSTRUCTION
        elif status == "Planned":
            color = config.COLOR_PLANNED
        else:
            color = config.COLOR_NEUTRAL

        # size logic for markers
        if config.MAP_SIZE_STANDARD:
            size = 12
        else:
            size = 8 + (power / 50)
            size = min(25, max(8, size))

        text = (
            f"{name}<br>"
            f"Status: {status}<br>"
            f"Power: {power} kW<br>"
            f"State: {site.get('State/Province','')}"
        )

        valid_points.append({"lat": lat, "lon": lon, "color": color, "size": size, "text": text})

        # build structured data
        # valid_points.append(
        #     {
        #         "name": site.get("Project/Plant Name", "Unknown"),
        #         "state": site.get("State/Province", "Unkown"),
        #         "power": power,
        #         "energy": energy,
        #         "status": status,
        #         "tech": site.get("Storage Device Technology Mid-Type", ""),
        #         "subtech": site.get("Storage Device Technology Sub-Type", ""),
        #         "operator": site.get("Utility", ""),
        #         "date": site.get("Commissioned Date", ""),
        #         "lon": lon,
        #         "lat": lat,
        #         "color": color,
        #         "size": size,
        #     }
        # )

    lats = [p["lat"] for p in valid_points]
    lons = [p["lon"] for p in valid_points]
    colors = [p["color"] for p in valid_points]
    sizes = [p["size"] for p in valid_points]
    texts = [p["text"] for p in valid_points]
    print(len(lats), len(lons), len(colors), len(sizes), len(texts))

    # create map figure using scattermapbox
    fig = go.Figure(
        go.Scattermapbox(
            lat=lats,
            lon=lons,
            mode="markers",
            marker=dict(size=sizes, color=colors, opacity=0.85, symbol="circle"),
            text=texts,
            hoverinfo="text",
        )
    )

    # configure map layout
    fig.update_layout(
        mapbox=dict(
            style=config.MAP_STYLE,  # carto-positron
            center=dict(
                # center on average of all states
                lat=sum(lats) / len(lats) if lats else config.MAP_CENTER_LAT,
                lon=sum(lons) / len(lons) if lons else config.MAP_CENTER_LON,
            ),
            zoom=config.MAP_ZOOM,
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        height=config.MAP_HEIGHT,
        hovermode="closest",
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )
    """

    # --- Convert filtered_sites to DataFrame ---
    df = pd.DataFrame(filtered_sites)
    df = df.dropna(subset=["Lattitude", "Longitude"])
    df["Lattitude"] = pd.to_numeric(df["Lattitude"], errors="coerce")
    df["Longitude"] = pd.to_numeric(df["Longitude"], errors="coerce")
    df = df.dropna(subset=["Lattitude", "Longitude"])

    # Split regions
    df_conus = df[
        (df["Lattitude"] >= 24)
        & (df["Lattitude"] <= 50)
        & (df["Longitude"] >= -125)
        & (df["Longitude"] <= -66)
    ]
    df_alaska = df[df["Lattitude"] > 50]
    df_puertorico = df[df["Lattitude"] < 24]

    def marker_trace(df_region):
        if df_region.empty:
            return None
        df_region["color"] = (
            df_region["Status"]
            .map(
                {
                    "Operational": config.COLOR_OPERATIONAL,
                    "Under Construction": config.COLOR_CONSTRUCTION,
                    "Planned": config.COLOR_PLANNED,
                }
            )
            .fillna(config.COLOR_NEUTRAL)
        )
        df_region["size"] = (
            df_region["Rated Power (kW)"]
            .fillna(0)
            .apply(lambda x: 12 if config.MAP_SIZE_STANDARD else min(25, max(8, 8 + x / 50)))
        )
        hover_text = (
            df_region["Project/Plant Name"].fillna("Unknown")
            + "<br>"
            + "Status: "
            + df_region["Status"].fillna("Unknown")
            + "<br>"
            + "Power: "
            + df_region["Rated Power (kW)"].fillna(0).astype(int).astype(str)
            + " kW<br>"
            + "State: "
            + df_region["State/Province"].fillna("")
        )
        return go.Scattermapbox(
            lat=df_region["Lattitude"],
            lon=df_region["Longitude"],
            mode="markers",
            marker=dict(size=df_region["size"], color=df_region["color"], opacity=0.85),
            text=[
                f"{s['Project/Plant Name']}<br>Status: {s['Status']}" for s in df.to_dict("records")
            ],
            hoverinfo="text",
            customdata=df.to_dict("records"),
        )

    fig = go.Figure()

    for region_df in [df_conus, df_alaska, df_puertorico]:
        trace = marker_trace(region_df)
        if trace:
            fig.add_trace(trace)

    # Layout centered on continental US only
    center_lat = df_conus["Lattitude"].mean() if not df_conus.empty else 39.5
    center_lon = df_conus["Longitude"].mean() if not df_conus.empty else -98.35

    fig.update_layout(
        mapbox=dict(
            style=config.MAP_STYLE,
            center=dict(lat=center_lat, lon=center_lon),
            zoom=3,
        ),
        margin=dict(l=0, r=0, t=0, b=0),
        showlegend=False,
        height=config.MAP_HEIGHT,
        hovermode="closest",
    )

    return fig


# === Callback 6: Update Table ===
@callback(
    [
        Output("bess-sites-table", "data"),
        Output("table-site-count", "children"),
    ],
    Input("filtered-sites-store", "data"),
)
def update_table(filtered_sites):
    """
    Fill table with filtered BESS sites

    Triggers:
    - when filtered sites change

    Returns:
    - table data (list of Dicts)
    - site count text
    """

    if not filtered_sites or len(filtered_sites) == 0:
        return [], "No sites"

    # filtered_sites is already in right format
    # each site is a dictionary with keys matching table column IDs

    count_text = f"{len(filtered_sites):,} sites"

    return filtered_sites, count_text


# === Callback 7: Store Selected Site ===
@callback(
    Output("selected-site-store", "data"),
    Input("bess-sites-table", "selected_rows"),
    State("bess-sites-table", "data"),
)
def store_selected_sites(selected_rows, table_data):
    """
    Store selected site data when user clicks on table row

    Triggers:
      - user clicks a row in the table

    Returns:
      - selected site dictionary (for chart callbacks to use)
    """

    # no selection
    if not selected_rows or not table_data:
        return None

    # get the firt selected row's data
    selected_site = table_data[selected_rows[0]]

    return selected_site


# === Callback 8: Toggle Charts Section ===
@callback(
    Output("charts-section", "style"),
    Input("selected-site-store", "data"),
)
def toggle_charts_section(selected_site):
    if not selected_site:
        return {"display": "none"}
    return {"display": "block"}


# === Callback 9: Update All Charts ===
@callback(
    [
        Output("selected-site-name", "children"),
        Output("chart-soc", "figure"),
        Output("chart-power", "figure"),
        Output("chart-ac-voltage", "figure"),
        Output("chart-dc-voltage", "figure"),
        Output("chart-temperature", "figure"),
        Output("chart-revenue", "figure"),
        Output("chart-data-quality", "children"),
    ],
    [
        Input("selected-site-store", "data"),
        Input("chart-time-range", "value"),
        # Input("interval-update-charts", "n_intervals"),  # <-- new input
    ],
)
def update_all_charts(selected_site, time_range):
    """
    Update all charts for the selected site, automatically triggered
    by site selection, time range, or interval
    """

    # create empty figure for error causes
    empty_fig = go.Figure()
    empty_fig.update_layout(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        annotations=[
            dict(
                text="No data",
                xref="paper",
                yref="paper",
                x=0.5,
                y=0.5,
                showarrow=False,
                font=dict(size=16, color="gray"),
            )
        ],
    )

    # no site selected
    if not selected_site:
        return (
            "",
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
            "",
        )

    site_id = selected_site["Project/Plant Name"]
    site_name = selected_site["Project/Plant Name"]

    # fetch high-resolution time-series data
    data = data_service.get_site_data(site_id, hours=time_range or 24)

    if not data:
        return (
            site_name,
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
            empty_fig,
            "No time-series data available for this site",
        )

    # convert to pandas DataFrame
    df = pd.DataFrame(data)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    # =======================
    # CHART 1: SOC
    # =======================
    fig_soc = go.Figure()
    fig_soc.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["state_of_charge"],
            mode="lines",
            name="SOC",
            line=dict(color=config.COLOR_SUCCESS, width=2),
            fill="tozeroy",
            fillcolor="rgba(6, 167, 125, 0.2)",
        )
    )
    fig_soc.update_layout(
        template=config.CHART_TEMPLATE,
        xaxis_title="Time",
        yaxis_title="State of Charge (%)",
        yaxis=dict(range=[0, 100]),
        hovermode="x unified",
        margin=dict(l=50, r=20, t=20, b=40),
    )

    # =======================
    # CHART 2: Power
    # =======================
    fig_power = go.Figure()
    df_charging = df[df["power_mw"] >= 0]
    df_discharging = df[df["power_mw"] < 0]

    if not df_charging.empty:
        fig_power.add_trace(
            go.Scatter(
                x=df_charging["timestamp"],
                y=df_charging["power_mw"],
                mode="lines",
                name="Charging",
                line=dict(color=config.COLOR_SUCCESS, width=2),
                fill="tozeroy",
                fillcolor="rgba(6, 167, 125, 0.2)",
            )
        )

    if not df_discharging.empty:
        fig_power.add_trace(
            go.Scatter(
                x=df_discharging["timestamp"],
                y=df_discharging["power_mw"],
                mode="lines",
                name="Discharging",
                line=dict(color=config.COLOR_DANGER, width=2),
                fill="tozeroy",
                fillcolor="rgba(214, 40, 40, 0.2)",
            )
        )

    fig_power.update_layout(
        template=config.CHART_TEMPLATE,
        xaxis_title="Time",
        yaxis_title="Power (MW)",
        hovermode="x unified",
        margin=dict(l=50, r=20, t=20, b=40),
        shapes=[
            dict(
                type="line",
                x0=df["timestamp"].min(),
                x1=df["timestamp"].max(),
                y0=0,
                y1=0,
                line=dict(color="gray", width=1, dash="dash"),
            )
        ],
    )

    # =======================
    # CHART 3: AC Voltage
    # =======================
    fig_ac_voltage = go.Figure()
    fig_ac_voltage.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["ac_bus_voltage"],
            mode="lines",
            name="AC Voltage",
            line=dict(color=config.COLOR_PRIMARY, width=2),
        )
    )
    fig_ac_voltage.update_layout(
        template=config.CHART_TEMPLATE,
        xaxis_title="Time",
        yaxis_title="AC Bus Voltage (V)",
        hovermode="x unified",
        margin=dict(l=50, r=20, t=20, b=40),
    )

    # =======================
    # CHART 4: DC Voltage
    # =======================
    fig_dc_voltage = go.Figure()
    fig_dc_voltage.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["dc_bus_voltage"],
            mode="lines",
            name="DC Voltage",
            line=dict(color="#9b59b6", width=2),
        )
    )
    fig_dc_voltage.update_layout(
        template=config.CHART_TEMPLATE,
        xaxis_title="Time",
        yaxis_title="DC Bus Voltage (V)",
        hovermode="x unified",
        margin=dict(l=50, r=20, t=20, b=40),
    )

    # =======================
    # CHART 5: Temperature
    # =======================
    fig_temp = go.Figure()
    fig_temp.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["temperature"],
            mode="lines",
            name="Battery Temp",
            line=dict(color=config.COLOR_WARNING, width=2),
        )
    )
    fig_temp.add_trace(
        go.Scatter(
            x=df["timestamp"],
            y=df["inverter_temp"],
            mode="lines",
            name="Inverter Temp",
            line=dict(color=config.COLOR_DANGER, width=2, dash="dash"),
        )
    )
    fig_temp.add_hrect(
        y0=40,
        y1=60,
        fillcolor="red",
        opacity=0.1,
        annotation_text="High Temp Zone",
        annotation_position="top left",
    )
    fig_temp.update_layout(
        template=config.CHART_TEMPLATE,
        xaxis_title="Time",
        yaxis_title="Temperature (°C)",
        hovermode="x unified",
        margin=dict(l=50, r=20, t=20, b=40),
    )

    # =======================
    # CHART 6: Revenue
    # =======================
    fig_revenue = go.Figure()
    if "revenue_usd_per_hour" in df.columns:
        fig_revenue.add_trace(
            go.Scatter(
                x=df["timestamp"],
                y=df["revenue_usd_per_hour"],
                mode="lines",
                name="Revenue",
                line=dict(color="#2ecc71", width=2),
                fill="tozeroy",
                fillcolor="rgba(46, 204, 113, 0.2)",
            )
        )
        fig_revenue.update_layout(
            template=config.CHART_TEMPLATE,
            xaxis_title="Time",
            yaxis_title="Revenue ($/hour)",
            hovermode="x unified",
            margin=dict(l=50, r=20, t=20, b=40),
        )
    else:
        fig_revenue = empty_fig

    data_quality = f"Displaying {len(df):,} data points over {time_range or 24} hours"

    return (
        site_name,
        fig_soc,
        fig_power,
        fig_ac_voltage,
        fig_dc_voltage,
        fig_temp,
        fig_revenue,
        data_quality,
    )
