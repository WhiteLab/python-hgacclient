import os
import re
import logging

import rethinkdb as r

import hgacclient as hgac

@hgac.plugin
def add_fastq(serv,name,**kwargs):
  '''
  Add a HGAC ID'd FastQ file to the metadata service.
  '''
  # Find absolute path of file name.
  name = os.path.abspath(name)

  # Parse the HGAC ID from the FastQ file path.
  hgacid = hgac.utils.hgacid(name)

  # Generate a data packet.
  data = hgacid.groupdict()
  data.update({
    'filename': name,
    'server': serv,
  })
  logging.debug(data)

  # Sync the data packet with the database.
  r.connect(db='metadata',**hgac.settings['rethinkdb']).repl()
  r.table('fastqs').insert(data,conflict=kwargs['conflict']).run()
