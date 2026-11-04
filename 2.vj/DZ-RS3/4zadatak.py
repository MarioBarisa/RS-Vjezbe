import asyncio, time
import random


async def provjeri_parnost(broj):
    await asyncio.sleep(2)
    if broj%2==0:
        print(f"Broj {broj} je paran")
    else:
        print(f"Broj {broj} nije paran")

async def main():
    brojevi = [random.randrange(1,100) for _ in range(10)]
    zadaci = [
        asyncio.create_task(provjeri_parnost(t)) for t in brojevi
    ]
    await asyncio.gather(*zadaci)

if __name__ == '__main__':
    t1=time.perf_counter()
    asyncio.run(main())
    t2=time.perf_counter()
    print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")

