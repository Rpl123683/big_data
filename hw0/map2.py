#!/usr/bin/env python
# coding=utf-8
import sys
t={}
means = open("mn.txt", 'r').readlines() 
for line in means:
    antiNucleus, mean_time = line.split('\t')
    t[int(antiNucleus)] = float(mean_time)

for line in sys.stdin:
    z=line.split(',')
    an = int(z[0])
    time = float(z[10])
    if time>t[an]:
    	print(str(z[0])+"\t"+str(z[1])+","+str(z[11]))
