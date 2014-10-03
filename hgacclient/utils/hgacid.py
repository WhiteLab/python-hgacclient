import re

REGEX = r'(?P<id>{regex})'.format(regex=r'_'.join([
  r'(?P<bid>\d{4}-\d+)',  # BID
  r'(?P<date>\d{6})',     # Date
  r'(?P<mac>[^_]+)',      # Machine
  r'(?P<run>\d+)',        # Run
  r'(?P<bar>[^_]+)',      # Barcode
  r'(?P<lane>\d)',        # Lane
])+r'(?:_(?P<pair>\d))?') # Pair

REGEX = re.compile(REGEX)

def hgacid(s): return REGEX.search(s)
