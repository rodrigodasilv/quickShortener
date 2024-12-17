import json
import random
import string
import redis

redis_client = redis.Redis(host='localhost', port=6379, charset="utf-8", decode_responses=True)


def get_url(shorter_code):
    return redis_client.get(shorter_code)


def create_short_url(url):
    shorter_code = str(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(16)))
    redis_client.set(shorter_code, url)
    return json.dumps({"shorter_code": shorter_code})
