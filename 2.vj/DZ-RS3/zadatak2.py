import asyncio, time

async def gatherCustomerInfo():
    await asyncio.sleep(3)
    customer = [
        {"ime": "Ivan", "prezime": "Horvat"},
        {"ime": "Karlo", "prezime": "Horvat"},
        {"ime": "Danijel", "prezime": "Horvat"},
        {"ime": "Karla", "prezime": "Horvat"},
    ]
    print("Customer data fetched.")
    return customer

async def gatherProductInfo():
    await asyncio.sleep(5)
    products=[
        {"naziv:": "Čokolada", "cijena":"2.5"},
        {"naziv:": "Jabuka", "cijena": "2.5"},
        {"naziv:": "Sir", "cijena": "2.5"},
        {"naziv:": "Cola", "cijena": "2.5"},
    ]
    print("Product data fetched.")
    return  products

async def main():
    customers, products = await asyncio.gather(gatherCustomerInfo(), gatherProductInfo())
    print(customers)
    print(products)

if __name__ == "__main__":

    t1=time.perf_counter()
    asyncio.run(main())
    t2=time.perf_counter()
    print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")







