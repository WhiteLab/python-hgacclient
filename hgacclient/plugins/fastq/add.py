import os
import re
import logging

import rethinkdb as r

import hgacclient as hgac

def add(serv,name,**kwargs):
  '''
  Add a HGAC ID'd FastQ file to the metadata service.
  '''
  # Find absolute path of file name.
  path = os.path.abspath(name)
  base = os.path.basename(name)

  # Parse the HGAC ID from the FastQ file path.
  hgacid = hgac.utils.hgacid(base)
  if not hgacid: raise ValueError('no hgac id found in filename')

  # Generate a data packet.
  data = hgacid.groupdict()
  data.update({
    'filename': path,
    'server': serv,
  })
  logging.debug(data)

  # Sync the data packet with the database.
  r.connect(db='metadata',**hgac.settings['rethinkdb']).repl()
  r.table('fastqs').insert(data,conflict=kwargs['conflict']).run()
