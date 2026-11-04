import asyncio

async def timer(name, delay):
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')
        await asyncio.sleep(1)
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    await asyncio.gather(*timers)

if __name__ == '__main__':

    asyncio.run(main())

"""
1. Svi timeri se dodaju u event loop
2. Korutine se pokrecu jedna po jedna t1->t2->t3
3. Kada korutina sleepa event loop ide na sljedeću ( nakon printa ) t1(sleep)->t2(print)->t3(t2 sleep daje event loopu da na red dođe t3) i tako se ponavlja cycle
4. Ova cycle se ponavlja se sve dokle sve 3 funckije nemaju njihovo vrijeme == 0 -> do kraja for petlje

"""


