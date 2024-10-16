#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

def Space(j):
    i = 0
    while i <= j:
        print(" ", end="")
        i += 1

def findAdmin():
    f = open("link.txt", "r")
    link = input("Enter Site Name \n(ex : example.com or www.example.com ): ")
    print("\n\nAvailable links : \n")
    while True:
        sub_link = f.readline().strip()
        if not sub_link:
            break
        req_link = "http://" + link + "/" + sub_link
        req = Request(req_link)
        try:
            response = urlopen(req)
        except HTTPError as e:
            continue
        except URLError as e:
            continue
        else:
            print("OK => ", req_link)

def Credit():
    Space(9); print("#####################################")
    Space(9); print("#   +++ Admin Panel Finder v1 +++   #")
    Space(9); print("#     Script by Illûmïnåté Ðëmøñ    #")
    Space(9); print("#    Bangladesh Black Hat Hackers   #")
    Space(9); print("#####################################")

Credit()
findAdmin()
