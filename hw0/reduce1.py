#!/usr/bin/env python
# coding=utf-8
import sys

current_key=None
for line in sys.stdin:
    kv=line.split("\t")
    if current_key==None:	
       current_key=kv[0]
       counter=0.0
       summ=0
    if current_key!=kv[0]:
       print((str(current_key))+"\t"+str(summ/counter))
       current_key=kv[0]
       counter=0
       summ=0
    summ+=float(kv[1])
    counter+=1
print((str(current_key))+"\t"+str(summ/counter))
