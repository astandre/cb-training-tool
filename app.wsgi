#! /usr/bin/python3.6

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/username/ExampleFlask/')
from app import app as application
application.secret_key = 'EcVfAD:mz)c=wTn$`(3T"8W73*,a6Y'