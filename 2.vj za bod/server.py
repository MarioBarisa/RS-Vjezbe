import asyncio, time, random, json

random.seed(42)

studenti = [
  { 'id': 1, 'ime': 'Ivan',   'prezime': 'Horvat',  'jmbag': '12332113', 'godina': 2 },
  { 'id': 2, 'ime': 'Ana',    'prezime': 'Kovac',   'jmbag': '321123321', 'godina': 2 },
  { 'id': 3, 'ime': 'Marko',  'prezime': 'Babic',   'jmbag': '456654456', 'godina': 3 }
];

async def allStudents():
    print("Dohvacanje podataka svih studenata")
    await asyncio.sleep(2)
    print("Svi studenti:",studenti)
    return studenti

async def studentById(id):
    print(f"Traženje studenta sa ID:{id}")
    for studnet in studenti:
        if id==studnet["id"]:
            await  asyncio.sleep(random.randrange(1,3))
            print("Student pronađen.",studnet)
            return studnet

async def studentByJMABG(id):
    print(f"Traženje studenta sa JMBAG:{id}")
    for student in studenti:
        if id==student["jmbag"]:
            await asyncio.sleep(random.randrange(1,3))
            print("Student pronađen",student)
            return student

async def allStudentsByYear(year):
    print(f"Traženje svih studenata koji su na godini studija:{year}")
    results=[student for student in studenti if student["godina"]==year]
    await  asyncio.sleep(random.randrange(1,3))
    print("Studenti:",results)
    return results

async def main():
    t1=time.perf_counter()
    results = await asyncio.gather(allStudents(),allStudentsByYear(2),studentByJMABG(456654456),studentById(1))
    concJSON = json.dumps(results, ensure_ascii=False)
    t2=time.perf_counter()
    print(f" --- Vrijeme izvođenja konkurentno {t2 - t1:.2f} sekunde ---")
    print("concJSON:", concJSON)

async def sec():
    t1=time.perf_counter()
    results = []
    results.append(await asyncio.create_task(allStudents()))
    results.append(await asyncio.create_task(allStudentsByYear(2)))
    results.append(await asyncio.create_task(studentByJMABG(456654456)))
    results.append(await asyncio.create_task(studentById(1)))
    secJSON = json.dumps(results, ensure_ascii=False)
    t2=time.perf_counter()
    print(f" --- Vrijeme izvođenja sekvnecijalno {t2 - t1:.2f} sekunde ---")
    print("secJSON:", secJSON)



if __name__ == '__main__':
    asyncio.run(main())
    asyncio.run(sec())



"""

Koliko traje izvođenje programa pri sekvencijalnoj obradi? Zašto?
Sekvencijalno izvođenje traje cca kao zbroj svih pojedinačnih čekanja (oko 5-8 s), jer svaku korutinu awaitamo jednu nakon druge pa nema preklapanja čekanja.

Koliko traje izvođenje programa pri konkurentnoj jednodretvenoj obradi? Zašto?
Konkurentno izvođenje traje približno koliko i najduža pojedinačna korutina (oko 2-3 s), jer se korutine pokrenu zajedno (asyncio.gather) i dok jedna čeka (await), event loop izvršava druge.

Koja je glavna razlika između ovih dvaju načina izvođenja? Kako se korutine izvršavaju unutar event loopa?
Glavna razlika je u raspoređivanju: sekvencijalno = jedna po jedna; konkurentno = više korutina napreduje naizmjenično.
Event loop u konkurentnom načinu prebacuje izvršavanje na drugu korutinu kad trenutna dođe do await točke (npr. await asyncio.sleep).

Što se događa ako u korutinama zamijenimo asyncio.sleep s time.sleep? Koja je tehnička razlika?
time.sleep je koji 'uspava' cijeli thread i blokira event loop, pa ostale korutine ne mogu napredovati.
asyncio.sleep je awaitable: suspendira samo trenutnu korutinu i vraća kontrolu event loopu da napravi druge zadatke.

Vraća li asyncio.gather() rezultate uvijek istim redoslijedom? Odgovara li taj redoslijed redoslijedu proslijeđenih
korutina ili redoslijedu njihova dovršavanja?
Ne odgovara kako koja korutina završi svoje izvršavanje. Odgovar redosljedu izvršavanja.

"""