import asyncio,time


async def secure_data(data):
    await asyncio.sleep(3)
    return {
        'prezime': data["prezime"],
        'broj_kartice': str(hash(data["broj_kartice"])),
        'CVV': str(hash(data["CVV"]))
    }

async def main():
    osjetljviPodaci=[
        {'prezime': 'Test', 'broj_kartice': '123321123', 'CVV': '1234'},
        {'prezime': 'TestDva', 'broj_kartice': '543345543', 'CVV': '3211'},
        {'prezime': 'TestTri', 'broj_kartice': '67887668', 'CVV': '3322'}
    ]
    zadaci=[asyncio.create_task(secure_data(t)) for t in osjetljviPodaci]
    enkriptiraniPodaci = await asyncio.gather(*zadaci)
    print(enkriptiraniPodaci)

if __name__ == "__main__":
    asyncio.run(main())