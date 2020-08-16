import urlib.request, urlib.parse, urlib.errors
from bs4 import BeautifulSoup
import ssl
import re
import sqlite3
import json

from exit import exiter

#Ignore SSl Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('We will experiment and try to make copy of 1980s Google')
print('This program will use PageRank Algo\n')
print('Try crawling a website with less link, greater the number of links, larger the time.')

#Prompting user for Website Link to Crawl
while True:
    userinput = input('Enter Website Name: ')
    url = userinput
    print('\nSearching')
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
    except:
        exiter()
        continue

#Setting up Database
cur.executescript('''
CREATE TABLE 
''')


#Retriving all of the anchor tags/links in the Website
sno = 1
atags = soup('a')
for tag in tags:
    print (sno+' '+tag)
    sno++
