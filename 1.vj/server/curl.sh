#!/usr/bin/env bash
# ============================================================
#  Studenti API - testne curl naredbe
#  Pokretanje:  bash curl.sh
#  (prvo pokreni server:  npm start)
# ============================================================

BASE=http://localhost:3000

echo "== 1) ISPIS svih studenata =="
curl -s "$BASE/studenti"
echo

echo "== 2) ISPIS studenta s id 1 =="
curl -s "$BASE/studenti/1"
echo

echo "== 3) DODAVANJE studenta =="
curl -s -X POST "$BASE/studenti" \
  -H "Content-Type: application/json" \
  -d '{"ime":"Luka","prezime":"Novak","jmbag":"0012345681","godina":1}'
echo

echo "== 4) UPDATE studenta s id 1 =="
curl -s -X PUT "$BASE/studenti/1" \
  -H "Content-Type: application/json" \
  -d '{"godina":3,"jmbag":"0012345699"}'
echo

echo "== 5) BRISANJE studenta s id 2 =="
curl -s -X DELETE "$BASE/studenti/2"
echo

echo "== 6) ISPIS nakon izmjena =="
curl -s "$BASE/studenti"
echo

echo "== 7) GRESKA: nepostojeci student (404) =="
curl -s -o /dev/null -w "HTTP status: %{http_code}\n" "$BASE/studenti/999"

echo "== 8) GRESKA: dodavanje bez obaveznih polja (400) =="
curl -s -o /dev/null -w "HTTP status: %{http_code}\n" -X POST "$BASE/studenti" \
  -H "Content-Type: application/json" \
  -d '{"ime":"Ana"}'
