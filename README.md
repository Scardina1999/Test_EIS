# 📊 Analisi di Impedenza Elettrochimica (EIS) con Python

## 📌 Descrizione
Questo progetto utilizza **Python** e la libreria `impedance.py` per analizzare i dati di **Electrochemical Impedance Spectroscopy (EIS)**. 
L'analisi prevede il fitting dei dati sperimentali con un **modello di circuito equivalente**, permettendo il confronto di più set di dati.

---

## 📂 Struttura del Progetto
- **`test_impedance.py`** → Script principale per analizzare e confrontare più dati EIS.
- **`test_impedance.ipynb`** → Versione notebook dello script, per un'esecuzione interattiva.
- **`dati/`** → Cartella contenente i file CSV con i dati di impedenza sperimentali.
- **`risultati_fit.csv`** → File CSV con i parametri stimati del circuito equivalente.
- **`README.md`** → Documentazione del progetto.

---

## ⚙️ **Setup del Progetto**
### 1️⃣ **Creare e Attivare l'Ambiente Conda**
Apri il terminale ed esegui:
```sh
conda create --name test_eis python=3.9
conda activate test_eis
```

### 2️⃣ **Installare le Dipendenze**
```sh
pip install impedance numpy scipy matplotlib pandas tkinter
```

### 3️⃣ **Eseguire lo Script**
Per avviare l’analisi, eseguire:
```sh
python test_impedance.py
```

---

## 🔬 **Funzionamento del Codice**
Lo script segue questi passaggi:
1. **Selezione multipla di file CSV contenenti i dati di impedenza.**
2. **Caricamento dei dati**: Frequenze, parte reale e immaginaria dell'impedenza.
3. **Definizione del modello di circuito equivalente**: `R0-p(R1,C1)-p(R2-Wo1,C2)`.
4. **Fitting del modello ai dati sperimentali** usando `impedance.py`.
5. **Stampa dei parametri stimati per ciascun dataset.**
6. **Visualizzazione dei risultati**:
   - **Diagramma di Nyquist** per confrontare i dati sperimentali con il modello.
   - **Diagramma di Bode** per visualizzare la risposta in frequenza in modulo e fase.

---

## 📚 **Citazioni e Riconoscimenti**
Se utilizzi `impedance.py` in pubblicazioni accademiche o lavori di ricerca, considera di citare la seguente fonte:

> **Murbach et al. (2020). impedance.py: A Python package for electrochemical impedance analysis. Journal of Open Source Software, 5(52), 2349.**  
> DOI: [10.21105/joss.02349](https://doi.org/10.21105/joss.02349)

Formato BibTeX:
```bibtex
@article{Murbach2020,
    doi = {10.21105/joss.02349},
    url = {https://doi.org/10.21105/joss.02349},
    year = {2020},
    publisher = {The Open Journal},
    volume = {5},
    number = {52},
    pages = {2349},
    author = {Matthew D. Murbach and Brian Gerwe and Neal Dawson-Elli and Lok-kun Tsui},
    title = {impedance.py: A Python package for electrochemical impedance analysis},
    journal = {Journal of Open Source Software}
}
```
Grazie agli autori di `impedance.py` per aver sviluppato questa libreria! 🙌  

---

## 🤖 **Autore**
- **Antonio** - Ingegneria Elettrica e dell'Automazione @ UNIFI 🚀 
