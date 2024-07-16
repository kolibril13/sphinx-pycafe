# outline for a myst_nb project with sphinx
# build with: sphinx-build -nW -E --keep-going -b html . ./_build/html
#  .venv/bin/sphinx-build  -nW -E --keep-going -b html . ./_build/html
html_favicon = 'favicon.ico'

language = 'en'

# html_static_path = ['_static']

project = 'PyCafe Example'
# copyright = ''
# author = ''
html_title = "PyCafe Example"

# specify project details
master_doc = "index"
project = "Example for Pycafe"

# basic build settings
exclude_patterns = ["_build", "README.md"]
include_patterns = ["*.md", "*.ipynb"]


nitpicky = True

nb_execution_mode = "off"

# load extensions
extensions = [
    "sphinx_copybutton",
    "sphinxext.remoteliteralinclude",
    "pycafe_sphinx",
    "myst_parser",
]

html_theme = 'furo'