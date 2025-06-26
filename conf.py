# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# sys.path.insert(0, os.path.abspath('../src'))  # Uncomment if using local modules

# -- Project information -----------------------------------------------------

project = 'Download Quicken Already Purchased'
copyright = '2025, Download Quicken Already Purchased'
author = 'Download Quicken Already Purchased'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

extensions = []

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output settings ----------------------------------------------------

html_theme = 'furo'

html_theme_options = {
    "footer_icons": [],  # Hides 'Made with Furo'
    "sidebar_hide_name": False,
    "navigation_with_keys": False,
    "show_powered_by": False  # Optional, even though Furo doesn't use this
}

# Paths to templates and static files
templates_path = ['_templates']

html_title = "Step-by-Step: How to Download Quicken Already Purchased"
html_short_title = "Download Quicken Already Purchased"
html_favicon = 'favicon.ico'

html_show_sourcelink = False
html_allow_unsafe = True
raw_enabled = True
