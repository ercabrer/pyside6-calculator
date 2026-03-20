"""
MAP VIEW COMPONENT - Interactive US Map

Shows all the BESS locations along with status and details
"""

from dash import html, dcc
import dash_bootstrap_components as dbc
from config import config


def create_map_section():
    """
    Create map section of the dashboard

    COMPONENTS:
    - section title
    - control buttons
    - interactive map (plotly)
    - legacy showing color meanings

    RETURNS:
      Dash Bootstrap Card with map inside
    """

    # TODO: work on time dialation callback

    return dbc.Card(
        [
            dbc.CardBody(
                [
                    # map titel and icon
                    html.H3(
                        [
                            html.I(className="fas fa-map-marked-alt me-2 text-primary"),
                            "BESS Deployment Map",
                        ],
                        className="mb-4",
                    ),
                    # map control (different views)
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    dbc.ButtonGroup(
                                        [
                                            dbc.Button(
                                                [
                                                    html.I(className="fas fa-map-pin me-2"),
                                                    "By Status",
                                                ],
                                                id="map-view-status",
                                                color="primary",
                                                size="sm",
                                                outline=True,
                                                active=True,
                                            ),
                                        ],
                                        className="mb-3",
                                    )
                                ]
                            )
                        ]
                    ),
                    # map (plotly graph component)
                    dcc.Graph(
                        id="us-bess-map",  # callbacks update map data
                        # map config
                        config={
                            "scrollZoom": True,  # enable scroll zoom
                            "displayModeBar": True,  # show toolbar
                            "displaylogo": False,  # hide plotly logo
                            # remove some tools
                            "modeBarButtonsToRemove": [
                                "lasso2d",
                                "select2d",
                                "autoScale2d",
                            ],
                        },
                        # map height
                        style={"height": f"{config.MAP_HEIGHT}px"},
                    ),
                    # map legend
                    html.Div(
                        [
                            html.Small(
                                [
                                    # operational (green)
                                    html.Span(
                                        [
                                            html.I(className="fas fa-circle text-success me-1"),
                                            "Operational",
                                        ],
                                        className="me-3",
                                    ),
                                    # under construction (orange)
                                    html.Span(
                                        [
                                            html.I(className="fas fa-circle text-warning me-1"),
                                            "Under Construction",
                                        ],
                                        className="me-3",
                                    ),
                                    # planned (blue)
                                    html.Span(
                                        [
                                            html.I(className="fas fa-circle text-info me-1"),
                                            "Planned",
                                        ]
                                    ),
                                ],
                                className="text-muted",
                            )
                        ],
                        className="mt-3 text-center",
                    ),
                ]
            )
        ],
        className="shadow-sm border-0 mb-4",
        id="map-section",
    )
