# Quiz Game kursinis darbas

## 1. Įvadas

Šio darbo tikslas buvo sukurti paprastą Quiz tipo programą naudojant Python ir objektinį programavimą (OOP). Programa leidžia vartotojui atsakyti į klausimus, o pabaigoje pateikia rezultatą.

Programa gali užkrauti klausimus iš failo, todėl ją galima lengvai plėsti nepridedant naujo kodo.

### Kaip paleisti programą

Programą galima paleisti su komanda:

python main.py

arba, jei naudojama grafinė versija:

python gui_quiz.py

### Kaip naudotis

1. Įvedamas vartotojo vardas  
2. Sistema pateikia klausimus  
3. Vartotojas pasirenka atsakymus  
4. Pabaigoje rodomas rezultatas  

---

## 2. Programos analizė

### Objektinio programavimo principai

Šiame projekte panaudoti visi pagrindiniai OOP principai.

**Inkapsuliacija** – klasėse duomenys saugomi viduje (pvz., Player turi vardą ir score).

**Paveldėjimas** – MultipleChoiceQuestion ir TrueFalseQuestion paveldi iš bendros Question klasės.

**Polimorfizmas** – skirtingos klasės turi tą patį metodą `check_answer`, bet jis veikia skirtingai.

**Abstrakcija** – naudojama abstrakti klasė Question, kuri apibrėžia bendrą struktūrą.

---

### Dizaino šablonas

Naudojamas **Factory Pattern**.

Factory klasė leidžia sukurti skirtingus klausimų tipus pagal jų tipą (mc arba tf).  
Tai leidžia lengvai pridėti naujus klausimų tipus ateityje.

---

### Kompozicija

Quiz klasė saugo klausimų sąrašą.  
Tai reiškia, kad Quiz objektas susideda iš Question objektų.

---

### Darbas su failais

Programa naudoja:

- CSV failą klausimams saugoti  
- TXT failą rezultatams saugoti  

Tai leidžia lengvai keisti klausimus ir saugoti žaidimo istoriją.

---

### Testavimas

Buvo naudojami paprasti unit testai, kurie tikrina:

- ar teisingai tikrinami atsakymai  
- ar veikia klausimų logika  

---

## 3. Rezultatai

Programa veikia ir leidžia atsakyti į klausimus.  
Klausimai yra užkraunami iš failo, todėl jų kiekis gali būti keičiamas.  
Rezultatai yra išsaugomi faile.  

Didžiausi iššūkiai buvo susiję su failų nuskaitymu ir klaidomis importuojant klases.

---

## 4. Išvados

Šio darbo metu buvo sukurta veikianti Quiz programa, naudojanti objektinį programavimą.

Programa yra paprasta, bet ją galima plėsti.  
Galima pridėti daugiau klausimų, pagerinti dizainą arba sukurti web versiją.

Ateityje būtų galima pridėti:
- grafinę vartotojo sąsają  
- rezultatų lentelę  
- sudėtingesnius klausimus  