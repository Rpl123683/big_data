#!/usr/bin/env python
# coding=utf-8
import sys
current_key=None
for line in sys.stdin:
    kv=line.split("\t")
    if current_key==None:	
       current_key=kv[0]
       counter=0
       s=set()
       summ=0.0
    if current_key!=kv[0]:
       print((str(current_key))+","+str(len(set(s)))+","+str(summ/counter))
       current_key=kv[0]
       counter=0
       s=set()
       summ=0.0
    values=kv[1].split(",")
    s.add(values[0])
    summ+=float(values[1])
    counter+=1

print((str(current_key))+","+str(len(set(s)))+","+str(summ/counter))
