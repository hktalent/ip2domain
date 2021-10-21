# What is
Sometimes, we need to know what connections our local machine has, and what are their IP, domain name, program and parameters?
- get ip to domain
- Know the domian corresponding to the local network connection IP
## How get Local network connection
```
# pid ip cmdAndArgs
./getCurNetConn.sh f
```

# How install for macos
```bash
brew install mysql tmux
brew services start mysql
brew services list|grep mysql
pip3 install mysql-connector-python scapy pysnooper

ln -s `which python3`  /usr/local/bin/py3
```

## How init mysql
```sql
create database sgdb_51pwn default charset 'utf8';
create user 'sgdb_51pwn'@'%' identified by 'sgdb_51pwn';
grant all on sgdb_51pwn.* to 'sgdb_51pwn'@'%';
flush privileges;

CREATE TABLE `ip2domain` (
  `id1` varchar(100) NOT NULL,
  `id2` varchar(100) NOT NULL,
  KEY `NewTable_id1_IDX` (`id1`) USING BTREE,
  KEY `NewTable_id2_IDX` (`id2`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

```

# How run
```bash
tmux
sudo py3 ip2domain.py

```
## run for centos vps  
```bash
python3 ip2domain2.py
rm -rf ip2d.txt
scp -i ~/.ssh/id_rsa -r -P $myVpsPort root@51pwn.com:/root/ip2d.txt ./
sort -u ip2d.txt|uniq >ip2domain.txt
rm -rf ip2d.txt
mysqlimport -u sgdb_51pwn -psgdb_51pwn --local sgdb_51pwn  `pwd`/ip2domain.txt
rm -rf ip2domain.txt

#  or

mysql -u sgdb_51pwn -psgdb_51pwn
use sgdb_51pwn;
SET GLOBAL local_infile=1;
LOAD DATA LOCAL INFILE '/ip2domain/ip2domain.txt' INTO TABLE ip2domain FIELDS TERMINATED BY ' ' LINES TERMINATED BY '\n';
exit
rm -rf ip2domain.txt
```

# How query ips
```bash
py3 ip2d4query.py -i 52.35.195.250,17.57.145.167
```
## Know the domian corresponding to the local network connection IP
```bash
./getCurNetConn.sh f|awk '{print $2}'|xargs -I % py3 ip2d4query.py -i %
# Now you can see: 
# pid ip domain cmd & args
./getCurNetConn.sh f
```
