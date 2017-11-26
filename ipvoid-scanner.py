#!/usr/bin/env python3

import os
import sys
import time
import requests
import re
import socket


IPVOID_BLACKLIST_URL = "http://www.ipvoid.com/ip-blacklist-check/"

def write_log(filename, line):
    f = open(filename, "a+")
    f.write(line.strip() + "\n")
    f.close()


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

    # Resolve ip to hostname
    hostnames = []

    try:
        hostnames = socket.gethostbyaddr(ip)
    except:
        pass

    tmpstr = "%s | %s | %s" % (ip, hostnames, all_bad)
    print tmpstr
    write_log("log.txt", tmpstr)


lines = open(sys.argv[1]).readlines()
for line in lines:
    if line.strip() != "":
        check_ipvoid(line.strip())

        time.sleep(3) # Wait for 3 seconds for each request to ipvoid



