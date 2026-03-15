# -*- coding: utf-8 -*-
#
# Configuration file for Sphinx documentation

import os
import sys

# Agregar el directorio padre al path
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# Extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # Para docstrings estilo Google
    'sphinx_rtd_theme'
]

# Configuración de napoleon
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True

# Configuración de autodoc
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'member-order': 'bysource'
}

# Para métodos decorados
autodoc_inherit_docstrings = True

# Mockear importaciones problemáticas
autodoc_mock_imports = [
    'requests',
    'cachetools',
    'pycryptodome',
    'pytz',
    'confuse',
    'six',
    'python-dotenv',
    'pyyaml',
    'ad_api',  # Mockear el paquete principal
]

# Templates
templates_path = ['_templates']

# Source
source_suffix = '.rst'
master_doc = 'index'

# Project info
project = u'Python Amazon Advertising API'
copyright = u'2023, Daniel Alvaro'
author = u'Daniel Alvaro'
version = u'0.7.4'
release = u'0.7.4'

# Exclusiones
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_theme_options = {"collapse_navigation": False}
html_static_path = ['_static']
