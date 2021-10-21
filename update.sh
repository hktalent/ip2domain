rm -rf ip2domain.txt
mysqldump  --set-gtid-purged=OFF --host=127.0.0.1 --protocol=tcp -C  --user=sgdb_51pwn --lock-tables=FALSE --port=3306 --default-character-set=utf8  "sgdb_51pwn" "ip2domain" --password='sgdb_51pwn'> init_data.sql
git commit -m "up" .
git push

