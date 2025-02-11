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
```

### 2️⃣ **Installare le Dipendenze**
```sh
pip install impedance numpy scipy matplotlib pandas jupyterlab
```

### 3️⃣ **Eseguire lo Script**
Per avviare l’analisi, eseguire:
```sh
python test_impedence.py
```
Oppure, per eseguire il notebook:
```sh
jupyter lab
```

---

## 🔬 **Funzionamento del Codice**
Lo script segue questi passaggi:
1. **Carica i dati di impedenza da `dati.csv`**  
2. **Filtra i dati**, mantenendo solo la parte utile del diagramma di Nyquist  
3. **Definisce un circuito equivalente** (`R0-p(R1,C1)-p(R2-Wo1,C2)`)  
4. **Adatta il modello ai dati sperimentali** con `impedance.py`  
5. **Calcola l'errore medio** tra dati reali e modello  
6. **Visualizza il diagramma di Nyquist** con i dati reali e il modello adattato  

---

## 🛠️ **Possibili Miglioramenti**
- ✅ Supporto per più modelli di circuiti equivalenti  
- ✅ Aggiunta di un’interfaccia grafica  
- ✅ Implementazione di un'analisi più dettagliata sui residui  

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
 

