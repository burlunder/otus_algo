#!/usr/bin/env python3
import os
import sys

if len(sys.argv) != 2:
    print("Error with input")
    sys.exit()

indata = sys.argv.pop()

if os.path.isfile(indata):
    with open(indata, 'r') as f:
        instr = f.readline()
        f.close()
else:
    instr = indata

print(len(instr.rstrip()))
