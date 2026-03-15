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

# Configuración CRÍTICA para métodos decorados
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'private-members': False,
    'show-inheritance': True,
    'inherited-members': False,
}

# IMPORTANTE para preservar docstrings con decoradores
autodoc_inherit_docstrings = True
autodoc_preserve_defaults = True  # Preserva valores por defecto
autodoc_typehints = 'signature'   # Muestra type hints
autodoc_typehints_format = 'short'
autodoc_class_signature = 'separated'

# Configuración de napoleon para docstrings estilo Google
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_use_keyword = True
napoleon_preprocess_types = True

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
    # Mockear módulos específicos de ad_api si es necesario
    'ad_api.base',
    'ad_api.api',
    'ad_api.api.sp',
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
