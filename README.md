# K-NN Image Recognition (Face Dataset)

Acest proiect implementează un algoritm **K-Nearest Neighbors (K-NN)** aplicat pe un set de imagini `.pgm`, folosit pentru recunoaștere facială. Se folosește o metrică de distanță (normă) pentru a găsi cei mai apropiați vecini față de o imagine dată și se face predicția clasei (persoanei).

## 🔍 Descriere

- Se utilizează un set de imagini structurat în foldere `s1` până la `s40`, fiecare conținând imagini `1.pgm` până la `9.pgm`.
- Primele 8 imagini per persoană sunt folosite pentru antrenare.
- Se poate selecta norma dorită: `1`, `2`, `inf`, `cos`.
- Se afișează imaginea originală și cea mai apropiată imagine găsită de algoritm.

## 🧠 Algoritmul K-NN

1. Vectorizarea imaginilor și stocarea în matricea A.
2. Calcularea distanței dintre o imagine necunoscută și toate imaginile din setul de antrenament.
3. Sortarea după distanță și alegerea celor mai apropiați 3 vecini.
4. Estimarea clasei prin modă statistică.
5. Afișarea rezultatului.

## ▶️ Cum rulezi

1. Asigură-te că ai structura de directoare `m0Poze/s1/.../s40` cu fișiere `.pgm`.
2. Rulează scriptul Python și introdu norma dorită când ți se cere:
   ```
   python script.py
   ```

## 👤 Autor

**Olaru Andrei**  
[LinkedIn](https://www.linkedin.com/in/andrei-olaru-6a471a190/)
