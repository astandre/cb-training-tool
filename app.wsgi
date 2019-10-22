#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/andreHP/cb-training-tool')
from app import app as application
application = create_app()