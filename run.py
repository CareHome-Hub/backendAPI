#!/usr/bin/python
from web import app
import logzero
from logzero import logger


app.run(debug=True, host='0.0.0.0', port=8099)
