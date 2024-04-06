import os
import json 

def filing(file):
    with open(file,'r' ,encoding='utf-8') as f:
        data = json.load(f)
        return data







# import codecs
# fileObj = codecs.open
# def filing():
#     f = open( "filter.json", "r" ,encoding='utf-8')
#     text = f.read()
#     f.close()
#     return text
# print(filing())