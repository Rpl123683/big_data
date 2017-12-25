#!/usr/bin/env python
# coding=utf-8
import sys
for line in sys.stdin:
    z=line.split(',')
    print(str(z[0])+"\t"+str(z[10]))
