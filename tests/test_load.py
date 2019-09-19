#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Tests for metadata loading."""
import pytest
from IPython import get_ipython
from ipython_nord_theme import startup
from nord_pygments import Nord
from pygments.style import Style
from pygments.token import Error


class MockHighlightingStyle(Style):
    """A test highlighting style."""

    style_overrides = {Error: "red"}


@pytest.fixture
def ip():
    """An IPython interactive terminal with a mock highlighting style."""
    ip = get_ipython()
    ip.highlighting_style = MockHighlightingStyle
    ip.highlighting_style_overrides = ip.highlighting_style.style_overrides
    return ip


def test_load(ip):
    """Test we can load and unload the theme."""
    startup.load()
    assert ip.highlighting_style == Nord
    assert ip.highlighting_style_overrides == Nord.style_overrides


def test_unload(ip):
    """Test we can unload the theme."""
    startup.load()
    assert ip.highlighting_style == Nord
    assert ip.highlighting_style_overrides == Nord.style_overrides
    startup.unload()
    assert ip.highlighting_style == MockHighlightingStyle
    assert ip.highlighting_style_overrides == MockHighlightingStyle.style_overrides
