import asyncio, time

async def autentifikacija(user):
    baza_korisnika = [
        {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
        {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
        {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
        {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
    ]
    await asyncio.sleep(3)
    postoji= any(
        korisnik["korisnicko_ime"] == user["korisnicko_ime"]
        and korisnik["email"]==user["email"]
        for korisnik in baza_korisnika
    )
    if postoji:
       await autorizacija(user["korisnicko_ime"], user["lozinka"])
       return None
    else:
        print (f"Korisnik { user["korisnicko_ime"]} nije pronađen.")
        return None

async def autorizacija(username, password):
    baza_lozinka = [
        {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
        {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
        {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
        {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
    ]
    await asyncio.sleep(2)
    for korisnik in baza_lozinka:
        if korisnik["korisnicko_ime"]==username:
            lozinka=korisnik["lozinka"]
    if lozinka==password:
        print(f"Korisnik {username}: Autorizacija uspješna.")
    else:
        print(f"Korisnik { username}: Autorizacija neuspješna.")




async def main():
    korisnik1 = {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka123'}
    korisnik2 = {'korisnicko_ime': 'mirko321', 'email': 'mirko123@gmail.com', 'lozinka': 'lozinka321'}

    authJedan = asyncio.create_task(autentifikacija(korisnik1))
    authDva = asyncio.create_task(autentifikacija(korisnik2))

    await  authJedan
    await authDva


if __name__ == "__main__":
    t1=time.perf_counter()
    asyncio.run(main())
    t2=time.perf_counter()
    print(f"Vrijeme izvođenja {t2 - t1:.2f} sekunde")
