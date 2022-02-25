# https://opendata.rapid7.com

# http(s)
# https://opendata.rapid7.com/sonar.http/
# https://opendata.rapid7.com/sonar.https/

# TCP
# https://opendata.rapid7.com/sonar.tcp/

# DNS
# https://opendata.rapid7.com/sonar.fdns_v2/
# https://opendata.rapid7.com/sonar.rdns_v2/

# SSL
# https://opendata.rapid7.com/sonar.ssl/
# https://opendata.rapid7.com/sonar.moressl/

# 国家曝光报告的开放端口
# https://opendata.rapid7.com/sonar.national_exposure/

# UDP
# https://opendata.rapid7.com/sonar.udp/

cd data
url="$1"
# echo ${url}
rm index.html
wget -c ${url}
cat index.html|grep -Eo '(\/[^"]+\.gz\b)'|xargs -I % wget -c https://opendata.rapid7.com%
