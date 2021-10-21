#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import argparse
from mysql.connector import (connection)

config={'database':"sgdb_51pwn",'user':'sgdb_51pwn','password':'sgdb_51pwn','host':'127.0.0.1','raise_on_warnings': True}

class _51pwn_ip2domain(object):
    # 初始化
    def __init__(self):
        self.conn = connection.MySQLConnection(**config)
    # 自动关闭连接
    def __del__(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            pass
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
    def queryip(self,data):
        sql='SELECT id1, id2 FROM sgdb_51pwn.ip2domain where id1=%s or id2=%s;'
        lstId=self.execSql(sql,data,bClsCursor=False)
        aRst=[]
        for (ip, domain) in self.cursor:
            aRst.append([ip, domain])
        self.cursor.close()
        return aRst
    
if __name__=='__main__':
    dbC=_51pwn_ip2domain()
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--ips",help="ip1,ip2")
    args = parser.parse_args()
    if args.ips:
        a=args.ips.split(",")
        for k in a:
            aRst = dbC.queryip((k,k))
            if 0 < len(aRst):
                for x in aRst:
                    print(x[0] + " " + x[1])