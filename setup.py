#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Set up ipython-nord-theme."""
import runpy

from setuptools import find_packages
from setuptools import setup

import versioneer


about = runpy.run_path("src/ipython_nord_theme/__about__.py")


def read_readme():
    """Load the project README."""
    with open("README.md") as readme:
        return readme.read()


setup_requirements = ["pip", "setuptools", "wheel"]

install_requirements = ["ipython", "nord-pygments"]

lint_requirements = [
    "flake8",
    "flake8-black",
    "flake8-bandit",
    "flake8-bugbear",
    "flake8-builtins",
    "flake8-mutable",
    "flake8-print",
    "pep8-naming",
]

test_requirements = ["pytest", "pytest-cov"]

dev_requirements = (
    ["ipython", "black", "rope", "pre-commit"] + lint_requirements + test_requirements
)


if __name__ == "__main__":
    setup(
        author=about["__author__"],
        author_email=about["__author_email__"],
        classifiers=about["__classifiers__"],
        cmdclass=versioneer.get_cmdclass(),
        description=about["__description__"],
        download_url=about["__download_url__"],
        entry_points={
            "ipython_startup_hook": "ipython_nord_theme = ipython_nord_theme.startup:load"
        },
        extras_require={
            "lint": lint_requirements,
            "dev": dev_requirements,
            "test": test_requirements,
            "hook": ["ipython-startup-hook"],
        },
        install_requires=install_requirements,
        keywords=about["__keywords__"],
        license=about["__license__"],
        long_description=read_readme(),
        long_description_content_type="text/markdown",
        name=about["__distname__"],
        packages=find_packages("src"),
        package_dir={"": "src"},
        project_urls={
            "Trackers": about["__bugtracker_url__"],
            "Source": about["__source_url__"],
        },
        setup_requires=setup_requirements,
        tests_require=test_requirements,
        test_suite="tests",
        url=about["__url__"],
        version=versioneer.get_version(),
        zip_safe=False,
    )
