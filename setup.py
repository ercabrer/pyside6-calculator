from pathlib import Path

from setuptools import setup, find_packages

DISTNAME = "quest-calculator"
PYTHON_REQUIRES = ">=3.6, <3.11"
DESCRIPTION = "Sandia National Laboratories Energy Storage Application Platform"
ROOT = Path(__file__).resolve().parent
LONG_DESCRIPTION = (ROOT / "README.md").read_text()
AUTHOR = "Sandia National Laboratories"
MAINTAINER_EMAIL = "eecabre@sandia.gov"
LICENSE = "BSD 3-clause"
URL = "https://github.com/ercabrer/pyside6-calculator.git"
VERSION = (ROOT / "version.txt").read_text().strip()

setup(
    name=DISTNAME,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    python_requires=PYTHON_REQUIRES,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    maintainer_email=MAINTAINER_EMAIL,
    license=LICENSE,
    url=URL,
    install_requires=[
        "PySide6==6.5.2",
        "PySide6-Addons==6.5.2",
        "PySide6-Essentials==6.5.2",
        "shiboken6==6.5.2"
    ],
    package_data={
        '': ['*.txt', '*.rst', '*.json', '*.jpg', '*.qss', '*.sh', '*.svg', '*.png', '*.kv', '*.bat', '*.csv', '*.md', '*.yml', '*.dll', '*.idf', '*.doctree', '.*info', '*.html', '*.js', '*.inv', '*.gif', '*.css', '*.eps', '*.pickle', '*.xlsx', '*.ttf', '*.pdf', '**/license*', '*.yml', '*.ui', '*.eot', '*.woff', '*.woff2', 'LICENSE', '*.mplstyle', '*.ini'],
    },
    entry_points={
        'console_scripts': [
            'calculator = calculator.__main__:main'
        ]
    }
)
