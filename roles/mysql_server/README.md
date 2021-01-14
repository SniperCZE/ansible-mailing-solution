MySQL server
==============

This role supports following MySQL releases:

- Oracle Mysql 5.5 from debian repository
- Oracle MySQL 5.6
- Oracle MySQL 5.7
- MariaDB 10.1


Configuration
---------------

For all configuration variables see `defaults/main.yml`.


MySQL replication
-------------------

This role supports only master-slave and master-master replication. Multi-source
replication is not supported.

For master-master replication, databases are created only on first master node.
Ansible mysql_db module creates databases using `CREATE DATABASE <db_name>;`
that can break replication if run on both nodes.

Replication is not  initialized automatically, but helper commands are logged.

