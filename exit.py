import math
import re
import urllib.request , urllib.parse , urllib.error
from bs4 import BeautifulSoup
import ssl

def exiter() :
    print('Something Went Wrong!! An Error occured')
    print('''   1. Slow Connection
    2. Invalid Website''')
    exiter = input("If you would like to exit type yes/y or press any key\n")
    if exiter.lower() == "yes" or exiter.lower() == "y":
        exit()
