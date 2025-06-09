# hello_google

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## Descrizione

**hello_google** è un semplice progetto Python di esempio che mostra:
- Come strutturare un progetto Python moderno con layout src-based
- Come effettuare una richiesta HTTP verso Google usando `requests`
- Come scrivere e lanciare test automatici con `pytest`

Questa repository è pensata come base per chi vuole imparare le best practice di struttura, packaging e testing in Python.

---

## Installazione
clona questo repository
```shell
git clone https://github.com/username/hello_google.git
cd hello_google
```

**Installa il pacchetto in modalità sviluppo**
```shell
pip install -e .
```

**Installa le dipendenze di sviluppo (opzionale, per i test)**
```shell
pip install -r requirements-dev.txt
```

---

## Utilizzo

Per eseguire l’applicazione principale:
```shell
python -m hello_google.main
```


**Cosa fa:**  
Esegue una richiesta HTTP verso [https://www.google.com](https://www.google.com) e stampa lo status code della risposta e i primi 100 caratteri della pagina.

---

## Test

I test sono scritti con `pytest` e si trovano nella cartella `tests/`.

Per eseguire i test:
```ssh
pytest
```
---
## Licenza

Questo progetto è distribuito sotto licenza MIT.  
Vedi il file [LICENSE](LICENSE) per dettagli.