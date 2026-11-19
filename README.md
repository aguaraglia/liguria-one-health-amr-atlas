# Liguria One Health AMR Atlas

Edizione regionale `lig_amr_atlas`, pubblicata da Codex Vitae ETS sulla stessa
base delle edizioni Lombardia e Veneto.

Sito pubblico: <https://aguaraglia.github.io/liguria-one-health-amr-atlas/>

## Stato

In Liguria le evidenze pubblicate localizzabili sono quasi tutte cliniche,
concentrate a Genova; non risultano studi veterinari, alimentari o ambientali
localizzabili.

Letteratura scientifica del 19 novembre 2026: 37 studi con collegamento
territoriale esplicito alla Liguria, in sei layer (AMR umana, veterinaria,
alimentare, ambientale, fauna selvatica, studi a scala regionale). Il layer
umano ha 7 elementi e 29 studi. Il contorno regionale ha 8 studi, di cui 4
sulla fauna selvatica. I layer veterinario, alimentare, ambientale e della
fauna selvatica sono vuoti: l'area senza segnaposto è nessuna evidenza
pubblicata, non resistenza zero. Ogni popup cita lo studio e il DOI (o il
record PubMed se il DOI non è assegnato) e ricorda che il segnaposto è il
luogo dello studio, non una prevalenza.

Fonti istituzionali pubbliche: AR-ISS 2024 (CC BY 4.0) e AIFA Open Data 2024,
antibatterici J01 (CC BY 4.0). Confini ISTAT 2026 (234 comuni, 4 province,
regione), letti in UTF-8. Cinque strutture nominate © OpenStreetMap
contributors, ODbL. A.Li.Sa. / ATS Liguria e il PDF OsMed sono esclusi: vedi
`metadata/EXCLUDED_SOURCES.md`.

Il conteggio in homepage e in pubblicazioni legge
`public/data/literature-catalog.json` (37).

## Pagine

Sorgente su `main`. Il sito statico è pubblicato dal branch `gh-pages`
(GitHub Pages, cartella `/`). Nessun file `CNAME`. Analitica: GoatCounter
`https://atlanteamr.goatcounter.com/count`, come le edizioni Lombardia e Veneto.

## Build locale

```bash
python3 -m http.server 8000
```

Aprire `http://localhost:8000/`.

Per rigenerare i dati pubblici servono gli input in `raw/` e, per i confini,
l'archivio ISTAT indicato in `metadata/SNAPSHOTS.tsv`:

```bash
pip install -r requirements-geodata.txt
python3 scripts/build_istat_geography.py --source-root <Limiti01012026_g> --output-root public/geography
python3 scripts/build_literature_catalog.py
python3 scripts/build_study_evidence_layers.py
```

## Directory

- `public/`: dati e asset approvati per il sito;
- `metadata/`: fonti, snapshot, ambito pubblico e fonti escluse;
- `raw/`: curatela, esummary e risposte Nominatim;
- `scripts/`: ricostruzione del catalogo e dei layer;
- `private/`: nessun dato riservato in questa edizione.
