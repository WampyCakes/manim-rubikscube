# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from distutils.sysconfig import get_python_lib

import manim
from manim_rubikscube import __version__

sys.path.insert(0, os.path.abspath('.'))

if os.environ.get("READTHEDOCS") == "True":
    site_path = get_python_lib()
    # we need to add ffmpeg to the path
    ffmpeg_path = os.path.join(site_path, "imageio_ffmpeg", "binaries")
    # the included binary is named ffmpeg-linux..., create a symlink
    [ffmpeg_bin] = [
        file for file in os.listdir(ffmpeg_path) if file.startswith("ffmpeg-")
    ]
    os.symlink(
        os.path.join(ffmpeg_path, ffmpeg_bin), os.path.join(ffmpeg_path, "ffmpeg")
    )
    os.environ["PATH"] += os.pathsep + ffmpeg_path

# -- Project information -----------------------------------------------------

project = 'Manim RubiksCube'
copyright = '2021, KingWampy'
author = 'KingWampy'

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    "sphinxext.opengraph",
    'manim_directive'
]

pygments_style = 'material'

autosummary_generate = True
add_module_names = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

if not os.path.exists('media/images'):
    os.makedirs('media/images')

if not os.path.exists('media/videos/480p30'):
    os.makedirs('media/videos/480p30')

# opengraph settings
ogp_image = "https://raw.githubusercontent.com/WampyCakes/manim-rubikscube/main/docs/source/_static/logo.png"
ogp_site_name = "Manim RubiksCube"
ogp_site_url = "https://manim-rubikscube.readthedocs.io/en/stable/"

ogp_custom_meta_tags = [
    '<meta property="og:description" content="A Manim implementation of the classic Rubik\'s Cube." />',
]

# -- Options for HTML output -------------------------------------------------

html_title = f"Manim RubiksCube v{__version__}"
html_theme = 'furo'
html_logo = '_static/logo.png'
html_favicon = '_static/logo.ico'

html_css_files = ["custom.css"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'media/images', 'media/videos/480p30']