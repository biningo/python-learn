import asyncio
import time


async def say(delay, msg):
    await asyncio.sleep(delay)
    print(msg)


async def run():
    print(time.strftime('%X'))

    #并发执行 下面的只需要1s
    t1 = asyncio.create_task(say(1, 'hello'))
    t2 = asyncio.create_task(say(1, 'world'))
    await t1
    await t2

    print(time.strftime('%X'))

if __name__ == '__main__':
    asyncio.run(run())