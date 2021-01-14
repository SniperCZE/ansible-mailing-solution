#!/bin/bash
cat < /dev/stdin |base64 >/etc/dovecot/queues/message.txt
MESSAGE=`cat /etc/dovecot/queues/message.txt`
echo "insert into spam_autolearn_queue(class, email_source) values('$1', '$MESSAGE');" >/etc/dovecot/queues/message.sql
mysql -h{{dovecot_mysql_server}} -u{{dovecot_mysql_user}} -p{{dovecot_mysql_passwd}} {{dovecot_mysql_dbname}} </etc/dovecot/queues/message.sql
