import express from 'express';

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// CORS - dopusta pozive s frontenda na drugoj domeni (npr. Render)
app.use((req, res, next) => {
  res.set('Access-Control-Allow-Origin', '*');
  res.set('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, OPTIONS');
  res.set('Access-Control-Allow-Headers', 'Content-Type');

  if (req.method === 'OPTIONS') {
    return res.sendStatus(204);
  }

  next();
});

// ---------------------------------------------------------------
// Podaci u memoriji (bez baze) - resetiraju se pri restartu servera
// ---------------------------------------------------------------
let studenti = [
  { id: 1, ime: 'Ivan',   prezime: 'Horvat',  jmbag: '0012345678', godina: 2 },
  { id: 2, ime: 'Ana',    prezime: 'Kovac',   jmbag: '0012345679', godina: 1 },
  { id: 3, ime: 'Marko',  prezime: 'Babic',   jmbag: '0012345680', godina: 3 }
];

let sljedeciId = 4;

// ---------------------------------------------------------------
// GET / - popis dostupnih ruta
// ---------------------------------------------------------------
app.get('/', (req, res) => {
  res.json({
    poruka: 'Studenti API radi',
    rute: [
      'GET    /studenti',
      'GET    /studenti/:id',
      'POST   /studenti',
      'PUT    /studenti/:id',
      'DELETE /studenti/:id'
    ]
  });
});

// GET /studenti - ispis svih studenata
app.get('/studenti', (req, res) => {
  res.json(studenti);
});

// GET /studenti/:id - ispis jednog studenta
app.get('/studenti/:id', (req, res) => {
  const student = studenti.find(s => s.id === Number(req.params.id));

  if (!student) {
    return res.status(404).json({ greska: `Student s id ${req.params.id} ne postoji` });
  }

  res.json(student);
});

// POST /studenti - dodavanje novog studenta
app.post('/studenti', (req, res) => {
  const { ime, prezime, jmbag, godina } = req.body ?? {};

  if (!ime || !prezime) {
    return res.status(400).json({ greska: 'Polja "ime" i "prezime" su obavezna' });
  }

  const novi = {
    id: sljedeciId++,
    ime,
    prezime,
    jmbag: jmbag ?? '',
    godina: godina ?? 1
  };

  studenti.push(novi);
  res.status(201).json(novi);
});

// PUT /studenti/:id - update postojeceg studenta
app.put('/studenti/:id', (req, res) => {
  const student = studenti.find(s => s.id === Number(req.params.id));

  if (!student) {
    return res.status(404).json({ greska: `Student s id ${req.params.id} ne postoji` });
  }

  const { ime, prezime, jmbag, godina } = req.body ?? {};

  if (ime !== undefined) student.ime = ime;
  if (prezime !== undefined) student.prezime = prezime;
  if (jmbag !== undefined) student.jmbag = jmbag;
  if (godina !== undefined) student.godina = godina;

  res.json(student);
});

// DELETE /studenti/:id - brisanje studenta
app.delete('/studenti/:id', (req, res) => {
  const index = studenti.findIndex(s => s.id === Number(req.params.id));

  if (index === -1) {
    return res.status(404).json({ greska: `Student s id ${req.params.id} ne postoji` });
  }

  const [obrisani] = studenti.splice(index, 1);
  res.json({ poruka: 'Student obrisan', student: obrisani });
});

// Nepostojeca ruta
app.use((req, res) => {
  res.status(404).json({ greska: `Ruta ${req.method} ${req.originalUrl} ne postoji` });
});

app.listen(PORT, () => {
  console.log(`Studenti API radi na http://localhost:${PORT}`);
});
