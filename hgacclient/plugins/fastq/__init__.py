#import add

import sys
import json
import logging
import argparse

import hgacclient as hgac

import add

@hgac.plugin('parsers')
def fastq_parser(subparsers):

  # FastQ sub-parser.
  fastq = subparsers.add_parser('fastq',help='FastQ operations.')
  # TODO fastq sub-parser global options here

  # FastQ sub-sub-parsers.
  fastq_parsers = fastq.add_subparsers(help='FastQ sub-commands.')

  # Add FastQ to metadata database.
  add_p = fastq_parsers.add_parser('add',help='add help')
  add_p.set_defaults(func=add.add)
  add_p.add_argument('serv',help='Server name.')
  add_p.add_argument('name',help='FastQ file.')
  add_p.add_argument('-c','--conflict',choices=['error','replace','update'],
                     default='error',help='How to deal with insert conflicts.')
