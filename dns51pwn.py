#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from scapy.all import *
from datetime import datetime
import time,datetime,sys,os,pysnooper

# for centos

szCurlDir=os.path.dirname(os.path.abspath(__file__))

interface = 'eth0'
# interface = 'en0'
filter_bpf = 'udp and port 53'

# @pysnooper.snoop()
def select_DNS(pkt):
    pkt_time = pkt.sprintf('%sent.time%')
    f1=open('dns51pwn.txt','ab')
    try:
        if DNSQR in pkt and pkt.dport == 53:
            s=pkt[DNS].qd.qname
            s=s[0:len(s)-1]
            if isinstance(s,bytes):
                s = s.decode('utf8')
            s1 = pkt[IP].src + "\t" + s + "\t" + str(datetime.datetime.now())
            f1.write(s1.encode('utf8'))
            print(s1)
        # # queries
        # #    pkt.show()
        # #    print ('[**] Detected DNS QR Message at: ' + pkt_time)
        # #    print(pkt(DNSQR).qname)
        #     pass
        # elif DNSRR in pkt and pkt.sport == 53:
        #    s=pkt[DNS].qd.qname
        #    if b'51pwn.com' in s:
        #     s=str(s[0:len(s)-1])
        #     if isinstance(s,bytes):
        #         s = s.decode('utf8')
        #     print (s)
        #     pkt.show()
        #     if pkt[DNS].an:
        #         for ix in range(pkt[DNS].ancount):
        #             ip = pkt[DNS].an[ix].rdata
        #             if not(isinstance(ip,bytes) or ip in ['0.0.0.0','::']):
        #                 s1=str(ip) + "\t" + str(s)+"\n"
        #                 f1.write(s1.encode('utf8'))
    except Exception as e:
        print(e)
        pass
    f1.close()

sniff(iface=interface, filter=filter_bpf, store=0,  prn=select_DNS)
