#!/usr/bin/python

import os
import sys
import time
import requests
import re


IPVOID_BLACKLIST_URL = "http://www.ipvoid.com/ip-blacklist-check/"

""" Check IP againsts IPVOID """
def check_ipvoid(ip):
    r = requests.post(IPVOID_BLACKLIST_URL, data={'ip' : str(ip)})
    content = r.text
    # content = open("tmp.txt").read()
    
    bad_reputations = re.findall(r'<i class="fa fa-minus-circle text-danger" aria-hidden="true"></i> (.+?)</td>', content, re.MULTILINE)

    all_bad = ""
    for bad in bad_reputations:
        all_bad += bad + ", "

    # good_reputations = re.findall(r'<i class="fa fa-check-circle text-success" aria-hidden="true"></i> (.+?)</td>', content, re.MULTILINE)

    # for good in good_reputations:
    #     print good

    print ip, all_bad


lines = open(sys.argv[1]).readlines()
for line in lines:
    if line.strip() != "":
        check_ipvoid(line.strip())

        time.sleep(3) # Wait for 3 seconds for each request to ipvoid
        


