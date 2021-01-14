#!/usr/bin/env python3
import redis
import logging
import json
import subprocess


redis_server = "{{ listener_redis_server }}"
redis_port = 6379
redis_db = 0
redis_channel = 'fail2ban'
logfile = '/var/log/fail2ban.log'

r = redis.StrictRedis(host=redis_server, port=redis_port, db=redis_db)
p = r.pubsub()
p.subscribe(redis_channel)
logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    filename=logfile,
    level=logging.DEBUG
    )


def decryptor(message):
    # Out of article's scope
    return message


def execute(message):
    if message['action'] == 'ban':
        command = 'iptables -A {chain} -p {protocol} -s {ip} -m multiport --dports {port} -j {banaction}'.format(**message)
    else:
        command = 'iptables -D {chain} -p {protocol} -s {ip} -m multiport --dports {port} -j {banaction}'.format(**message)
    logging.debug(
        '{host} triggered: {command}'.format(
            host=message['published_by'],
            command=command
            ))
    return_code = subprocess.call(command, shell=True)
    if not return_code == 0:
        logging.info('Command: {command} failed with rc={rc}'.format(
            command=command,
            rc=return_code
            ))
    else:
        logging.debug('Command: {command} executed succesfully'.format(
            command=command
            ))


def main():
    for record in p.listen():
        if record['type'] == 'message':
            message = json.loads(decryptor(record)['data'].decode('utf-8'))
            execute(message)


main()