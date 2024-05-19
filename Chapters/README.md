# PinNET
Toto je kódová báze pro bakalářskou práci na téma "Lokalizace klíčových bodů pomocí neuronových
sítí".

Autorem je Daniel Slavík. 

Vedoucím práce je Ing. Tomáš Fabián, Ph.D.


## Adresářová struktura
- `data/` - složka obsahující vstupní data
- `logs/` - složka obsahující natrénované modely
- `metrics/` - složka obsahující metriky
- `samples/` - složka obsahující ukázková data
- `src/` - zdrojové kódy
- `src/config/` - konfigurační soubory
- `src/models/` - definice modelů
- `src/plots` - skripty pro vykreslování grafů
- `src/processing/` - skripty pro zpracování dat
- `src/scripts/` - pomocné skripty
- `src/utils/` - pomocné funkce
- `src/start.py` - hlavní skript pro spuštění
- `src/dinov2` - implementace modelu DINOV2

## Příprava prostředí

Před spouštením proframu je potřeba nainstalovat závislosti pomocí příkazu:
```bash
pip install -r requirements.txt
```
Úplně na začátek je třeba ověřit cesty v `src/config/paths.py`. 

Model k trénování a ostatní parametry je třeba specifikovat a ověřit v `src/config`


## Spouštění programu

Program se spouští pomocí skriptu `start.py`. Skript má:
- první jednoslovný parametr pro výběr akce
- povinný parametr `-o` pro výběr pracovní/výstupní složky. Tento parametr navazuje také i na
cesty definované v `src/config/paths.py`
```bash
inference -o /home/wortelus/bp/
```

### Možné akce

- `fit` - natrénování modelu
- `inference` - inference modelu
- `real` - inference modelu na reálných datech
- `false_detections` - metrika pro falešné detekce
- `precision` - metrika pro přesnost
- `single` - tvorba datasetu pro jeden klíčový bod
- `partial` - tvorba datasetu pro vybraný set klíčových bodů
- `complete` - tvorba datasetu pro všechny klíčové body
- `convert` - konverze checkpointu do modelu
- `samples` - tvorba ukázkových dat
