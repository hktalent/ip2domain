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
g_szDomainIp = "199.180.115.7"
g_szDomain = ["51pwn.com",'exploit-poc.com']

def myAny(s):
    for k in g_szDomain:
        if k in s:
            return True
    return False

# @pysnooper.snoop()
def select_DNS(pkt):

    if DNSRR in pkt:
        pkt.show()
    f1=open('dns51pwn.txt','ab')
    try:
        if DNSQR in pkt and pkt.dport == 53:
            s=pkt[DNS].qd.qname
            s=s[0:len(s)-1]
            if isinstance(s,bytes):
                s = s.decode('utf8')
            s1 = pkt[IP].src + "\t" + s + "\t" + str(datetime.datetime.now()) + "\n"
            f1.write(s1.encode('utf8'))
            if myAny(s):
                print(s)
                spf_resp = IP(dst=pkt[IP].src)/UDP(dport=pkt[UDP].sport, sport=53)/DNS(qr=1,opcode='QUERY',rd=1,ra=1,aa=0,id=pkt[DNS].id,qdcount=1,ancount=1,an=DNSRR(rrname=pkt[DNSQR].qname, rdata=g_szDomainIp)/DNSRR(rrname=pkt[DNSQR].qname,rdata=g_szDomainIp))
                send(spf_resp, verbose=0, iface=interface)
    except Exception as e:
        print(e)
    f1.close()

sniff(iface=interface, filter=filter_bpf, store=0,  prn=select_DNS)
