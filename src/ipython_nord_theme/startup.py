#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""Load hooks for the theme."""
from IPython import get_ipython

from . import magic


def load():
    """Load the theme for the currently active IPython shell."""
    magic.load_ipython_extension(get_ipython())


def unload():
    """Unload the theme for the currently active IPython shell."""
    magic.unload_ipython_extension(get_ipython())
