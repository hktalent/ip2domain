from requests.packages.urllib3.contrib import pyopenssl as reqs

"""
1、
nslookup -qt=ptr 116.178.217.66 8.8.8.8
2
import socket 
domain=socket.gethostbyaddr('ip')

这里的ip查询分精准
http://ip.tool.chinaz.com

http://ip.tool.chinaz.com/202.96.85.155

POST /ajaxsync.aspx?at=AiWenBaseData HTTP/1.1
Host: ip.tool.chinaz.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:96.0) Gecko/20100101 Firefox/96.0
Accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01
Accept-Language: en-US,en;q=0.5
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 75
Origin: http://ip.tool.chinaz.com
Connection: close
Referer: http://ip.tool.chinaz.com/202.96.85.155

token=61%2C262%2C216%2C218%2C209&ip=202.96.85.155&aiWenType=区县级数据

"""

ip='111.45.3.185'
port='443'
try:    
    x509 = reqs.OpenSSL.crypto.load_certificate(
        reqs.OpenSSL.crypto.FILETYPE_PEM,
        reqs.ssl.get_server_certificate((ip, port))
    )
    domain = x509.get_subject().CN
    print(domain)
except:
    print(ip+'>Get CN failed')

