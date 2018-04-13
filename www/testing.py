#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import orm
from models import User,Blog, Comment
import asyncio


@asyncio.coroutine
def  test():
    yield from orm.create_pool(loop=loop, host='localhost', port=3306, user='root', password='68582188', db='awesome')
    u = User(name='Test', email='test@example.com', passwd='123456', image='about:blank',id='123')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()


if __name__=='__main__':
    test()