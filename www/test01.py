import orm
from models import User, Blog, Comment
import asyncio, time


@asyncio.coroutine
def save(loop):
    yield from orm.create_pool(loop, user='root', password='root@123', db='test')
    u = User(name='Test', email='test6@example.com', passwd='1234567890', image='about:blank')
    yield from u.save()


@asyncio.coroutine
def update(loop):
    yield from orm.create_pool(loop, user='root', password='root@123', db='test')
    u = User(id='001512628712288ca6825d65f1f41a9ac40dd7a480ee65e000', email='test0@example.com', passwd='1234567890', admin=False, name="中国", image='about:blank', created_at=time.time())
    yield from u.update()


@asyncio.coroutine
def find(loop):
    yield from orm.create_pool(loop, user='root', password='root@123', db='test')
    u = yield from User.find('001512628712288ca6825d65f1f41a9ac40dd7a480ee65e000')
    print(str(u))


@asyncio.coroutine
def findAll(loop):
    yield from orm.create_pool(loop, user='root', password='root@123', db='test')
    uList = yield from User.findAll()
    print(uList)


@asyncio.coroutine
def findNumber(loop):
    yield from orm.create_pool(loop, user='root', password='root@123', db='test')
    number = yield from User.findNumber('passwd')
    print(number)


loop = asyncio.get_event_loop()
loop.run_until_complete(findNumber(loop))
#loop.run_forever()