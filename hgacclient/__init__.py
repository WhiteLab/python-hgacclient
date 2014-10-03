import os
import yaml
import pkgutil
import logging

from plugin import *

__PACKAGE = os.path.dirname(__file__)

# Load settings file.
settings = os.path.join(__PACKAGE,'settings.yaml')
settings = yaml.load(open(settings).read())

# Import plugins.
IMPORTER = pkgutil.ImpImporter(os.path.join(__PACKAGE,'plugins'))
try: map(lambda x: IMPORTER.find_module(x).load_module(x),settings['plugins'])
except Exception as err: logging.warning(err)