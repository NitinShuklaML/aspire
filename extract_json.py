#!/usr/bin/env python

# Importing json Module for reading the incoming JSON files

import json
import sys

args=sys.argv[1]
print(args)

with open(str(args)) as json_file:
        blah= json.load(json_file)
        

print(blah[2]['src'])


