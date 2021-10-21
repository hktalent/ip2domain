#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from scapy.all import *
from datetime import datetime
import time,datetime,sys,os,pysnooper
from mysql.connector import (connection)


szCurlDir=os.path.dirname(os.path.abspath(__file__))

config={'database':"sgdb_51pwn",'user':'sgdb_51pwn','password':'sgdb_51pwn','host':'127.0.0.1','raise_on_warnings': True}

interface = 'en0'
filter_bpf = 'udp and port 53'

# debug
# @pysnooper.snoop()
class _51pwn_ip2domain(object):
    # 初始化
    def __init__(self):
        self.conn = connection.MySQLConnection(**config)
    # 自动关闭连接
    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.commit()
            self.conn.close()
    def execSql(self,sql,data,bClsCursor=True):
        self.cursor = self.conn.cursor()
        lstId=None
        try:
            self.cursor.execute(sql,data)
            lstId=self.cursor.lastrowid
        except Exception as e:
            print(e)
        if bClsCursor:
            self.cursor.close()
        return lstId
    def query(self,data):
        sql='SELECT id1, id2 FROM sgdb_51pwn.ip2domain where id1=%s and id2=%s;'
        lstId=self.execSql(sql,data,bClsCursor=False)
        aRst=[]
        for (ip, domain) in self.cursor:
            aRst.append([ip, domain])
        self.cursor.close()
        return aRst
    def insert(self,data):
        aRst=self.query(data)
        # print(aRst)
        if 0 == len(aRst):
            sql='INSERT INTO sgdb_51pwn.ip2domain (id1, id2) VALUES(%s, %s);'
            oR = self.execSql(sql,data)
            self.conn.commit()
            return oR
        return None

dbC=_51pwn_ip2domain()

def select_DNS(pkt):
    pkt_time = pkt.sprintf('%sent.time%')
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
           print ('start ' + s)
           if pkt[DNS].an:
             for ix in range(pkt[DNS].ancount):
                ip = pkt[DNS].an[ix].rdata
                if not isinstance(ip,bytes):
                    nLsId = dbC.insert((ip,s))
                    if 0 == nLsId:
                        print(s+ "(" + ip + ")")
    except Exception as e:
        print(e)
        pass

sniff(iface=interface, filter=filter_bpf, store=0,  prn=select_DNS)
