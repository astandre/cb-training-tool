#! /usr/bin/python3.6

import logging
import sys
activate_this = '/home/andreHP/cb-training-tool/venv/bin/activate.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/andreHP/cb-training-tool')
from cbTraining import app as application
application = create_app()