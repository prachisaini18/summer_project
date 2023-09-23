#!/usr/bin/python3
print("Content-type: text/html")
print()

from googlesearch import search
import subprocess
import cgi
form = cgi.FieldStorage()
query= form.getvalue('que')

print(query)
searchResults=search(query, num_results=10)
print(f"\n Top 10 results for '{query}':\n")
print("<pre>")
for index, result in enumerate(searchResults, start=1):
    print('<a href="')
    print(result)
    print('" target="_blank">')
    print(f"{index}.{result}")
    print("</a>")
print("</pre>")
