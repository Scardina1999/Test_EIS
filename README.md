# Analisi EIS con Python

## 📌 Descrizione
Questo progetto utilizza **Python** e la libreria `impedance.py` per analizzare i dati di **Electrochemical Impedance Spectroscopy (EIS)**.  
Viene applicato un modello di circuito equivalente per il fitting dei dati sperimentali.

---

## 📂 Struttura del Progetto
- **`test_impedence.py`** → Script principale per analizzare i dati EIS.
- **`test_impedence.ipynb`** → Versione notebook dello script, per un'esecuzione interattiva.
- **`dati.csv`** → File CSV contenente i dati di impedenza sperimentali.
- **`risultati_fit.csv`** → File CSV con i parametri del circuito equivalente ottenuti dal fitting.
- **`README.md`** → Documentazione del progetto.

---

## ⚙️ **Setup del Progetto**
### 1️⃣ **Creare e Attivare l'Ambiente Conda**
Apri il terminale ed esegui:
```sh
conda create --name test_eis python=3.9
conda activate test_eis

