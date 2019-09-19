#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""IPython magics."""
from nord_pygments import Nord

OLD_HIGHLIGHTING_STYLE = OLD_HIGHLIGHTING_STYLE_OVERRIDES = None


def load_ipython_extension(ip):
    """Load the ipython extension.

    Args:
        ip: IPython interactive shell for which to load the extension.

    """
    global OLD_HIGHLIGHTING_STYLE
    global OLD_HIGHLIGHTING_STYLE_OVERRIDES
    OLD_HIGHLIGHTING_STYLE, ip.highlighting_style = ip.highlighting_style, Nord
    OLD_HIGHLIGHTING_STYLE_OVERRIDES, ip.highlighting_style_overrides = (
        ip.highlighting_style_overrides,
        Nord.style_overrides,
    )
    ip.refresh_style()


def unload_ipython_extension(ip):
    """Unload the ipython extension.

    Args:
        ip: IPython interactive shell from which to unload the extension.

    """
    ip.highlighting_style = OLD_HIGHLIGHTING_STYLE
    ip.highlighting_style_overrides = OLD_HIGHLIGHTING_STYLE_OVERRIDES
    ip.refresh_style()
