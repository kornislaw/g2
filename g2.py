#! /usr/bin/env python

"""Generating files based on a template and a CSV list of keywords to be replaced

Usage:
  g2.py --template=<template_file> --data=<keywords_csv>
  g2.py -h | --help
  g2.py -v | --version

"""

import csv
from docopt import docopt

arguments = docopt(__doc__, version='G2 1.0')

with open(arguments['--template'], 'r') as t:
    template = t.read()
    with open(arguments['--data'], 'r') as d:
        reader = csv.reader(d)
        headers = next(reader)[1:]

        for r in reader:  # iterating over rows
            data = template
            for i in range(0,len(headers)):  # iterating over headers
                data = data.replace(headers[i].strip(), r[i+1])
            with open('output/'+r[0], 'w') as o:  # store output in json
                o.write(data)
                print(r[0]+' saved')
