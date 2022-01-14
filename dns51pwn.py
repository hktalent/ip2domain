#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from scapy.all import *
from datetime import datetime
import urllib3,json
import requests as requestsSs
urllib3.disable_warnings()
requestsSs.packages.urllib3.disable_warnings()

requests = requestsSs.session()

# for centos

szCurlDir=os.path.dirname(os.path.abspath(__file__))

interface = 'eth0'
# interface = 'en0'
filter_bpf = 'udp and port 53'
g_szDomain = ["51pwn.com",'exploit-poc.com']


# @pysnooper.snoop()
def select_DNS(pkt):
    try:
        if DNSQR in pkt and pkt.dport == 53:
            s=pkt[DNS].qd.qname
            s=s[0:len(s)-1]
            if isinstance(s,bytes):
                s = s.decode('utf8')
            for k in g_szDomain:
                if k in s:
                    return
            requests.post('https://wwww.51pwn.com/ip2domain', data=json.dumps({"domain":s,"ip":pkt[IP].src}), verify=False, headers={"Content-Type": "application/json;charset=UTF-8","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.2 Safari/605.1.15"},timeout=(10,15),allow_redirects=False)
           
    except Exception as e:
        print(e)

sniff(iface=interface, filter=filter_bpf, store=0,  prn=select_DNS)
