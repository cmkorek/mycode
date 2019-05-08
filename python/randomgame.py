#!/usr/bin/python3
"""Koreks random game via python"""

import requests

#caps GLOBAL variable, available to the whole program
#GLOBAL dog park LOCAL in your house
MYAPI = "https://www.random.org/integers/?num=1&min=0&max=1&col=1&base=10&format=plain&rnd=new"

def main():
    result = requests.get(MYAPI)
    #print(result.text)
    if "1" in result.text:
        print("you won!")
    else:
        print("you lost!")

main()

