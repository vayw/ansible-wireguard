#!/usr/bin/env python3

import sys
from os.path import exists
import json
import ipaddress

client = sys.argv[1]
db = sys.argv[2]
ip = sys.argv[3]
mask = sys.argv[4]

UPD = False
if not exists(db):
    IPDB = {}
    local_iface = ipaddress.ip_interface(f"{ip}/{mask}")
    n = local_iface + 1
    IPDB["NEXT"] = str(n.ip)
    IPDB["peers"] = {}
else:
    with open(db, 'r') as dbfile:
        IPDB = json.load(dbfile)

if client in IPDB["peers"]:
    print(IPDB["peers"][client])
else:
    IPDB["peers"][client] = IPDB["NEXT"]
    print(IPDB["peers"][client])
    n = ipaddress.ip_address(IPDB["NEXT"]) + 1
    if n in ipaddress.ip_interface(f"{ip}/{mask}").network:
        IPDB["NEXT"] = str(n)
    else:
        IPDB["NEXT"] = "_FULL_"
    UPD = True

if UPD:
    with open(db, 'w') as dbfile:
        json.dump(IPDB, dbfile)
