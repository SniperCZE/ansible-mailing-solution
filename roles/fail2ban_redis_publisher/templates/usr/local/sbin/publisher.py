#!/usr/bin/env python3
import sys
import redis


redis_server = "{{ publisher_redis_server }}"
redis_port = 6379
redis_db = 0
redis_channel = 'fail2ban'


def encryptor(message):
    # Out of article's scope
    return message


def main():
    message = encryptor(sys.argv[1])
    r = redis.StrictRedis(
        host=redis_server,
        port=redis_port,
        db=redis_db
        )
    p = r.pubsub()
    r.publish(redis_channel, message)
    p.close()


main()
