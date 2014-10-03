#!/usr/bin/env python
import os
import re
import argparse

import rethinkdb as r

from hgac import utils

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Add HGAC ID FastQ to metadata.')

  parser.add_argument('fastq',help='HGAC ID FastQ')

  args = parser.parse_args()

  hgac = utils.hgacid(args.fastq)

  data = {
    'filename' : args.fastq,
  }
  data.update(hgac.groupdict())

  r.connect(
    host = 'changeme',
    port = 28015,
    db = 'changeme',
    auth_key = 'changeme',
  ).repl()

  r.table('fastqs').insert(data).run()
