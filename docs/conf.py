# Configuration file for Sphinx - ENFOQUE RADICAL
# NO intenta importar el módulo, solo mockea TODO

import os
import sys

# Agregar directorio padre al path (por si acaso)
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
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]

# MOCKEAR TODO - ENFOQUE RADICAL
autodoc_mock_imports = [
    # Dependencias del sistema
    'requests',
    'six',
    'cachetools',
    'pycryptodome',
    'pytz',
    'confuse',
    'python-dotenv',
    'pyyaml',
    
    # Módulos del paquete - MOCKEAR TODO EL PAQUETE
    'ad_api',
    'ad_api.base',
    'ad_api.api',
    'ad_api.api.sp',
    'ad_api.api.sb',
    'ad_api.api.sd',
    'ad_api.api.dsp',
    'ad_api.auth',
]

# Configuración AGRESIVA de autodoc
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': False,
    'special-members': '__init__',
    'inherited-members': True,
    'show-inheritance': True,
    'member-order': 'bysource',
}

# CRÍTICO: Forzar que funcione incluso con módulos mockeados
autodoc_inherit_docstrings = True
autodoc_preserve_defaults = True
autodoc_typehints = 'none'  # Simplificar

# Napoleon para docstrings estilo Google
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
