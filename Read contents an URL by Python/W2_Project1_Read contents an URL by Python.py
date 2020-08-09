# -*- coding: utf-8 -*-
"""
Python code for reading the content of a URL
@idMoteb everywhere

"""


import requests
r =requests.get('https://www.wikipedia.org')
print (r.text)
file = open("url Data.txt","w") 
 
file.write(r.text) 
 
 
file.close() 

