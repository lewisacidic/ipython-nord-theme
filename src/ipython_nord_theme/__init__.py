#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2019 Rich Lewis
# License: MIT license
"""An arctic, north-bluish theme for the IPython interactive prompt.

See `ipython_nord_theme.__about__` for more info.
"""
from .__about__ import __copyright__
from .__about__ import __distname__
from .__about__ import __license__
from .__about__ import __url__
from .__about__ import __version__
from .magic import load_ipython_extension
from .magic import unload_ipython_extension
from .startup import load
from .startup import unload

__all__ = [
    "__copyright__",
    "__distname__",
    "__license__",
    "__url__",
    "__version__",
    "load",
    "load_ipython_extension",
    "unload",
    "unload_ipython_extension",
]
