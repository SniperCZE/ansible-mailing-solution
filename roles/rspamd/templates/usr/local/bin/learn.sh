#!/bin/sh
TYPE=$1

for LINEID in `mysql -h{{dovecot_mysql_server}} -u{{dovecot_mysql_user}} -p{{dovecot_mysql_passwd}} -BNe "select id from spam_autolearn_queue where class='$TYPE' limit 10" {{dovecot_mysql_dbname}}`; do

    mysql -h{{dovecot_mysql_server}} -u{{dovecot_mysql_user}} -p{{dovecot_mysql_passwd}} -BNe "select email_source from spam_autolearn_queue where id=$LINEID limit 1" postfix |sed 's/\\n//g' |base64 -d >/tmp/message.eml
    
    if [ "$TYPE" = "SPAM" ]; then
        /usr/bin/rspamc -h {{rspamd_server_hostname}}:11334 -P {{ vault_rspamc_password }} learn_spam /tmp/message.eml
        if [ $? -eq 0 ]; then
            mysql -h{{dovecot_mysql_server}} -u{{dovecot_mysql_user}} -p{{dovecot_mysql_passwd}} -BNe "delete from spam_autolearn_queue where id=$LINEID" postfix
        fi
    else
        /usr/bin/rspamc -h {{rspamd_server_hostname}}:11334 -P {{ vault_rspamc_password }} learn_ham /tmp/message.eml
        if [ $? -eq 0 ]; then
            mysql -h{{dovecot_mysql_server}} -u{{dovecot_mysql_user}} -p{{dovecot_mysql_passwd}} -BNe "delete from spam_autolearn_queue where id=$LINEID" postfix
        fi
    fi

done
