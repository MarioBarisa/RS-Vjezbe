import asyncio

async def fetch_data():
    await asyncio.sleep(3)
    print("Podaci dohvaćeni.")
    return [num for num in range(1,11)] #comprehension


def main():
    asyncio.run(fetch_data())


if __name__ == "__main__":
    main()


