import json
import random
import string
import redis

redis_client = redis.Redis(host='redis', port=6379, charset="utf-8", decode_responses=True)


def create_shorter_code():
    return str(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16)))


def get_url(shorter_code):
    return redis_client.get(shorter_code)


def create_short_url(url):
    while True:
        shorter_code = create_shorter_code()
        if redis_client.get(shorter_code) is None:
            break
    redis_client.set(shorter_code, url)
    return json.dumps({"shorter_code": shorter_code})
