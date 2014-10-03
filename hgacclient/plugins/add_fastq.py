import os
import re
import logging

import rethinkdb as r

import hgacclient as hgac

def add_fastq(server,fastq,**kwargs):
  '''
  Add a HGAC ID'd FastQ file to the metadata service.
  '''
  # Parse the HGAC ID from the FastQ file path.
  hgacid = hgac.util.hgacid(os.path.abspath(fastq))

  # Generate a data packet.
  data = hgac.groupdict()
  data.update({
    'filename':os.path.abspath(fastq),
  })

  # Sync the data packet with the database.
  r.connect(db='metadata',**hgac.settings['rethinkdb']).repl()
  r.table('fastqs').insert(data,conflict=kwargs['conflict']).run()
