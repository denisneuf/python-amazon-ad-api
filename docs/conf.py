# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import inspect
# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
import os
import sys

sys.path.insert(0, os.path.abspath('.'))

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

# Importar el módulo principal - ¡ESTO ES CLAVE Y DIFERENTE A LO QUE HEMOS HECHO!
import ad_api

# -- Project information -----------------------------------------------------

project = 'PYTHON-AMAZON-AD-API'
copyright = '2023, Daniel Alvaro'
author = 'Daniel Alvaro'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme", 'button', 'cookieconsent',
    'sphinx.ext.autodoc', 'sphinx.ext.coverage', 'sphinx.ext.napoleon',
    'enum_tools.autoenum',

]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
autodoc_default_options = {"members": True, "undoc-members": True, 'member-order': 'bysource'}
# html_theme_options = {
#     "collapse_navigation": False
# }
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_rtd_theme'
# html_theme = "pydata_sphinx_theme"
html_theme = 'alabaster'

html_theme_options = {
    'github_button': True,    # optional tweaks
    'github_banner': True,
    'github_button': True,
    'description': '''
A wrapper to access Amazon's Advertising API with an easy-to-use interface.
    ''',
    'donate_url': 'https://github.com/sponsors/denisneuf',
    'github_user': 'denisneuf',
    'github_repo': 'python-amazon-ad-api',
    "github_type": "star",  # watch|star|fork
'fixed_sidebar': True
}
# Add any paths that contain custom static files (such as style sheets) here,
relative to this directory. They are copied after the builtin static files,
so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['custom.css']


napoleon_google_docstring = True
napoleon_numpy_docstring = False
