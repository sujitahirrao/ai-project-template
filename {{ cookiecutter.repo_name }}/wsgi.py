activate_venv_script = r"..\venv\Scripts\activate_this.py"

with open(activate_venv_script) as _file:
    exec(_file.read(), dict(__file__=activate_venv_script))

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from api import app as application
