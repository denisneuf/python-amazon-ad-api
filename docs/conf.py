# Configuration file for Sphinx documentation builder

import os
import sys

# Agregar directorio padre al path
sys.path.insert(0, os.path.abspath('..'))

# -- Project information -----------------------------------------------------
project = 'Python Amazon Advertising API'
copyright = '2023, Daniel Alvaro'
author = 'Daniel Alvaro'
release = '0.7.4'
version = '0.7.4'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Para docstrings estilo Google
    'sphinx_rtd_theme',
]

# Configuración MINIMAL pero FUNCIONAL
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'member-order': 'bysource',
}

# IMPORTANTE para métodos decorados
autodoc_inherit_docstrings = True

# Configuración de napoleon
napoleon_google_docstring = True
napoleon_numpy_docstring = False

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
