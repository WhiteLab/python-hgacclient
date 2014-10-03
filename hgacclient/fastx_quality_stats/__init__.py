import os
import yaml

from plugin import *

__PACKAGE = os.path.dirname(__file__)

# Load settings file.
settings = os.path.join(__PACKAGE,'settings.yaml')
settings = yaml.load(open(settings).read())
