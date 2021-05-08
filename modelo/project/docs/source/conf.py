# Configuration file for the Sphinx documentation builder.

# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
from distutils.version import LooseVersion
import os

import sphinx_material
from recommonmark.transform import AutoStructify

# -- Project information -----------------------------------------------------

project = "Documentação Luban"
html_title = "Documentação Luban"

copyright = '20xx, Nome do Aluno'
author = 'Nome do Aluno'

# The full version, including alpha/beta/rc tags
release = LooseVersion(sphinx_material.__version__).vstring

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "numpydoc",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "recommonmark",
    "sphinx_markdown_tables",
    "sphinx_copybutton",
]

autosummary_generate = True
autoclass_content = "class"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named 'default.css' will overwrite the builtin 'default.css'.
html_static_path = ["_static"]

# -- HTML theme settings ------------------------------------------------

html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"
html_logo = "./logos/Logo_Luban.png"

# material theme options (see theme.conf for more information)
html_theme_options = {
    "base_url": "https://documentacao-luban-portugal.readthedocs.io/en/latest/index.html",
    "repo_url": "https://github.com/../..",
    "repo_name": "Nome do Aluno - Documentação ",
    "google_analytics_account": "UA-XXXXX",
    "html_minify": False,
    "html_prettify": True,
    "css_minify": True,
    "repo_type": "github",
    "globaltoc_depth": 2,
    "color_primary": "brown", # "blue",
    "color_accent": "orange", #"cyan",
    "theme_color": "4b231b", #"#2196f3",
    "master_doc": False,
    #"heroes": {
    #    "index": "Instituto Politécnico de Setúbal",
    #}
    }

language = "en"
html_last_updated_fmt = ""

todo_include_todos = True
html_favicon = "./logos/Logo_Luban.png"

html_use_index = True
html_domain_indices = True
