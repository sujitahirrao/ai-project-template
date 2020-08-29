from waitress import serve

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

import api

serve(api.app, host='0.0.0.0', port=443)
