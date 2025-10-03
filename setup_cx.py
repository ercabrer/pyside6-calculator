from setuptools import setup, find_packages
from cx_Freeze import setup, Executable

DISTNAME = "Quest"
VERSION = "2.0"
PYTHON_REQUIRES = ">=3.6"
DESCRIPTION = "Sandia National Laboratories Energy Storage Application Platform"
LONG_DESCRIPTION = open("README.md").read()
AUTHOR = "Sandia National Laboratories"
MAINTAINER_EMAIL = "tunguy@sandia.gov"
LICENSE = "BSD 3-clause"
URL = "https://github.com/ercabrer/pyside6-calculator.git"

options = {
    'build_exe': {
        'packages': [
            "PySide6",
            "PySide6-Addons",
            "PySide6-Essentials",
            "shiboken6"
        ],
        'include_files': [
            ("README.md", "README.md"),
            ("LICENSE", "LICENSE"),
            ("calculator", "calculator")
        ],
    },
}

base = None
executables = [Executable("calculator/__main__.py", base=base)]

setup(
    name=DISTNAME,
    version=VERSION,
    packages=find_packages(),
    include_package_data=True,
    python_requires=PYTHON_REQUIRES,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author=AUTHOR,
    maintainer_email=MAINTAINER_EMAIL,
    license=LICENSE,
    url=URL,
    executables=executables,
    options=options
)