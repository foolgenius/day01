import random

import requests
from django.core.cache import cache

from common import keys
from day01 import cfg


def get_randomnum(length=6):
    random_list = []

    for i in range(0, length):
        list = random.randint(0, 9)
        random_list.append(str(list))

    return ''.join(random_list)


def send_vcode(phonenum):
    """send vcode"""
    vcode = get_randomnum()
    print(vcode)

    args = cfg.YZX_SMS_ARGS.copy()
    args['mobile'] = phonenum
    args['param'] = vcode
    response = requests.post(cfg.YZX_SMS_API, json=args)
    if response.status_code != 200:
        return False
    else:
        cache.set(keys.VCODE %phonenum, vcode, timeout=1800)
        # cache.set(keys.VCODE % phonenum, vcode, 1800)
        cache_vcode = cache.get(keys.VCODE % phonenum)
        print(vcode)
        print('============')
        print(phonenum)
        print('============')
        print(cache_vcode)

        return True