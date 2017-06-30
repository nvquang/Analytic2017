# map.py
 
import sys
import re
import string
from fingerprint import FingerPrint
 
f = FingerPrint()
 
for line in sys.stdin:
    try:
        print ("%s\t%s" % (f.fingerprint(line),line.strip()))
    except Exception as e:
        print e
        pass