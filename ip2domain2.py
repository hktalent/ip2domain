#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from scapy.all import *
from datetime import datetime
import time,datetime,sys,os

# for centos

szCurlDir=os.path.dirname(os.path.abspath(__file__))

interface = 'eth0'
# interface = 'en0'
filter_bpf = 'udp and port 53'

def select_DNS(pkt):
    pkt_time = pkt.sprintf('%sent.time%')
    f1=open('ip2d.txt','ab')
    try:
        if DNSQR in pkt and pkt.dport == 53:
        # queries
        #    pkt.show()
        #    print ('[**] Detected DNS QR Message at: ' + pkt_time)
        #    print(pkt(DNSQR).qname)
            pass
        elif DNSRR in pkt and pkt.sport == 53:
           s=pkt[DNS].qd.qname
           s=s[0:len(s)-1].decode('utf8')
        #    print ('start ' + s)
           if pkt[DNS].an:
             for ix in range(pkt[DNS].ancount):
                ip = pkt[DNS].an[ix].rdata
                if not isinstance(ip,bytes):
                    s1=ip + " " + s+"\n"
                    f1.write(s1.encode('utf8'))
    except Exception as e:
        print(e)
        pass
    f1.close()

sniff(iface=interface, filter=filter_bpf, store=0,  prn=select_DNS)
