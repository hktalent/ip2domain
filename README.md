# What is
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
## centos
```bash
yum install mysql tmux
service mysqld restart


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