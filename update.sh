rm -rf ip2d.txt
scp -i ~/.ssh/id_rsa -C -r -P $myVpsPort root@exploit-poc.com:/root/ip2d.txt ./
sort -u ip2d.txt|uniq >ip2domain.txt
rm -rf ip2d.txt
echo ip2domain.txt
wc -l ip2domain.txt
mysqlimport -u sgdb_51pwn -psgdb_51pwn --local sgdb_51pwn  `pwd`/ip2domain.txt
# rm -rf ip2domain.txt

mysqldump  --set-gtid-purged=OFF --host=127.0.0.1 --protocol=tcp -C  --user=sgdb_51pwn --lock-tables=FALSE --port=3306 --default-character-set=utf8  "sgdb_51pwn" "ip2domain" --password='sgdb_51pwn'> init_data.sql
git commit -m "up" .;git push

