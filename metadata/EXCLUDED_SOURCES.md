# Fonti escluse o non disponibili per l'atlante Liguria (verifica riuso 2026-11-19, grok-05dev)

Regola di Alex: senza un permesso di riuso chiaro, la fonte non entra nell'atlante. Nessuna email inviata, nessuna richiesta di autorizzazione.

## A.Li.Sa. / ATS Liguria (portale Liguria Salute): Alisa Informa e monitoraggio CRE / C. auris — ESCLUSO
- Pagina ICA e AMR: https://www.liguriasalute.atsliguria.it/organizzazione/direzione-generale/prevenzione-epidemiologia-programmazione-e-controlli/infezioni-assistenza-antimicrobico-resistenza.html (HTTP 200).
- Contenuti: newsletter «Alisa Informa» n. 1 (2017), 2 (2018), 3 (2020), 4 (dicembre 2023). Il n. 4 riporta la tabella regionale AR-ISS 2022 per classe di farmaco (10 laboratori, copertura 93,2%) e lo screening CRE/CPE 2015-2023. Le Aziende inviano un report mensile su test e pazienti screenati per CRE e C. auris («Monitoraggio attività di sorveglianza di CRE e C. auris»). Non esiste un rapporto annuale AMR regionale paragonabile a quelli dell'Emilia-Romagna.
- Note legali (https://www.liguriasalute.atsliguria.it/note-legali.html): «Sono quindi suscettibili di utilizzo ad uso personale e non commerciale con divieto di modifica, riproduzione totale e/o parziale o a fini di lucro». Le citazioni sono ammesse solo «a titolo di cronaca o le recensioni».
- Esito: nessun permesso di riuso dei dati. ESCLUSO. I dati AR-ISS liguri si prendono dal rapporto ISS (CC BY 4.0).

## AIFA, Rapporto OsMed Regione Liguria 2024 (PDF) — ESCLUSO, sostituito
- PDF: https://www.aifa.gov.it/documents/20142/3610201/Liguria_Osmed_2024.pdf (HTTP 200). Tabella 13, «Antibiotici»: 14,6 DDD/1.000 ab-die, 14,2 euro pro capite.
- Note legali AIFA (https://www.aifa.gov.it/copyright): i contenuti del sito (testi, tabelle) «sono protetti ai sensi della normativa in tema di opere dell'ingegno»; per fini di lucro serve permesso scritto; citazione sempre obbligatoria. La licenza CC BY 4.0 vale per gli Open Data, non per i PDF.
- Esito: nessuna licenza aperta esplicita sul PDF. ESCLUSO dal pacchetto. Al suo posto: AIFA Open Data 2024 (CSV, CC BY 4.0), aggregato J01 per la Liguria (`public/data/aifa_opendata_2024_liguria_j01.json`).
- Nota per Alex: l'edizione Veneto usa ancora la Tabella 13 del PDF OsMed. Per coerenza andrebbe sostituita con lo stesso aggregato Open Data.

## IZS Piemonte, Liguria e Valle d'Aosta (IZSPLV) — nessun dato da usare
- Note legali (https://www.izsplv.it/it/note-legali.html): «I testi e le tabelle presenti in questo sito web sono distribuiti, dove non diversamente indicato, con Licenza Creative Commons 4.0 / Attribuzione – Non Commerciale (CC BY NC)»; esclusi immagini ed elaborazioni grafiche senza riferimento esplicito alla licenza.
- La licenza è esplicita, ma l'IZSPLV non pubblica dati AMR veterinari per provincia o regione: la sezione «Dati attività» riporta solo il numero di esami per tipo (agenti batterici 358.785, senza antibiogrammi). Il progetto EpICA (antibiogrammi gratuiti dalla Liguria, piattaforma ICA/AMR) non ha dati pubblici. La pagina CeRTiS (izsalimento.izsto.it) ha risposto HTTP 500 e poi con errore TLS: non riprovata con altri mezzi.
- Esito: nessun layer veterinario istituzionale. Gli articoli IZSPLV restano nel catalogo come letteratura (citazione bibliografica).

## ARPAL — nessun dato da usare
- Note legali (https://www.arpal.liguria.it/note-legali.html): contenuti in CC BY-NC-SA 2.5, con citazione di fonte e URL e richiesta di segnalare gli usi ad ARPAL.
- AMR nei reflui: notizie del 17/05/2024 e del 12/11/2025. ARPAL è il soggetto incaricato dal PRCAR della ricerca di antibiotici, batteri resistenti e geni di resistenza in reflui e fanghi, con dottorati UniGe; sorveglianza sistematica dei principali depuratori annunciata dal 2025. Nessun dato pubblicato.
- Esito: nessun layer ambientale istituzionale. Se ARPAL pubblicherà dati, la licenza NC-SA richiede la segnalazione dell'uso: decisione di Alex.

## Regione Liguria, Open Data (CC BY 4.0)
- dati.regione.liguria.it (CKAN): 0 dataset per «antibiotic», «antibiotico», «resistenza», «depuratori»; 1 per «reflue» (PTA 2017, agglomerati ATO Est ai sensi della Direttiva 91/271/CEE), solo contesto, non AMR.

## ISS, sorveglianza CRE (RIS-4/2025) — non estratto
- https://www.epicentro.iss.it/antibiotico-resistenza/cpe/RIS-4_2025.pdf (CC BY 4.0). Il valore regionale ligure è solo nella mappa (Figura 3), non in tabella: non estratto per evitare letture da grafico.
