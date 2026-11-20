#!/usr/bin/env python3
"""Build Liguria study evidence layers from the curated literature catalog.

Geometries come from the ISTAT 2026 boundaries of this edition, from a named
facility geocoded on OpenStreetMap Nominatim (1 req/s, 2026-11-19, raw
responses in raw/nominatim/). The script does not geocode farms, kennels or shelters and does not
invent a site the catalog does not name.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTE = "Il segnaposto indica dove è stato condotto lo studio, non una prevalenza."
SECTOR = {
    "healthcare_amr": "AMR clinica",
    "human_antimicrobial_use": "Consumo di antimicrobici",
    "antimicrobial_stewardship": "Stewardship antimicrobica",
    "veterinary_amr": "AMR veterinaria",
    "companion_animal_amr": "AMR negli animali d'affezione",
    "environmental_amr": "AMR ambientale",
    "foodborne_amr": "AMR alimentare",
    "wildlife_amr": "AMR nella fauna selvatica",
}
# Nominatim results checked on 2026-11-19 (raw/nominatim/results_2026-11-19.json).
# Coordinates are the facility returned for the named institution, not a sample.
POINTS = {
    "san_martino": (8.9730883, 44.4094689, "IRCCS Ospedale Policlinico San Martino, Genova",
                    "OpenStreetMap Nominatim: Ospedale San Martino, Via Angelo Scribanti, Genova (amenity=hospital)."),
    "gaslini": (8.9880616, 44.3928643, "IRCCS Istituto Giannina Gaslini, Genova",
                "OpenStreetMap Nominatim: Ospedale Pediatrico Giannina Gaslini, Via Gerolamo Gaslini, Genova (amenity=hospital)."),
    "galliera": (8.9415855, 44.3995250, "E.O. Ospedali Galliera, Genova",
                 "OpenStreetMap Nominatim: Ospedale Galliera, Via Alessandro Volta 8, Genova (amenity=hospital)."),
    "lavagna": (9.3492316, 44.3148414, "Ospedale di Lavagna (ASL4 Liguria)",
                "OpenStreetMap Nominatim: Ospedale di Lavagna, Via Don Giovanni Battista Bobbio 25, Lavagna (amenity=hospital)."),
    "albenga": (8.1996780, 44.0549813, "Ospedale Santa Maria di Misericordia, Albenga",
                "OpenStreetMap Nominatim: Santa Maria di Misericordia, Via Martiri della Foce, Albenga (amenity=hospital). L'abstract dice 'Albenga hospital'."),
}
ORGANISM = {
    "pubmed_21820758": "Acinetobacter baumannii multiresistente", "pubmed_23524898": "Gram-negativi urinari ESBL o resistenti a ceftazidime",
    "pubmed_23906074": "batteri aerobi da peritonite secondaria pediatrica", "pubmed_24906230": "E. coli NDM-4",
    "pubmed_25812459": "Gram-negativi da batteriemia in oncologia pediatrica", "pubmed_27558493": "Gram-negativi urinari, antibiotici orali",
    "pubmed_28668656": "K. pneumoniae resistente ai carbapenemi (batteriemie)", "pubmed_29229880": "K. pneumoniae resistente (microscopia a forza atomica)",
    "pubmed_29253622": "uso di antimicrobici (PPS regionale)", "pubmed_29273072": "uso di antibiotici nella polmonite pediatrica",
    "pubmed_29600324": "gestione di Enterobacterales ESBL (toolkit)", "pubmed_30988332": "Salmonella 1,4,[5],12:i:- multiresistente (stenelle)",
    "pubmed_32490767": "stafilococchi meticillino-resistenti (infezioni protesiche)", "pubmed_33021597": "uropatogeni in oncologia pediatrica",
    "pubmed_33401591": "Gram-negativi resistenti ai carbapenemi", "pubmed_33801613": "Yersinia enterocolitica (cinghiali)",
    "pubmed_34067207": "Salmonella spp. (cinghiali)", "pubmed_36558780": "Salmonella spp. (isolati umani, acque superficiali, cinghiali)", "pubmed_35690266": "Enterobacterales resistenti ai carbapenemi (screening)",
    "pubmed_35740127": "patogeni urinari pediatrici resistenti", "pubmed_36710161": "DDD pediatrica (vancomicina e altri)",
    "pubmed_36830127": "farmaci anti-MRSA nelle batteriemie pediatriche", "pubmed_37627698": "batteri da terapia intensiva",
    "pubmed_38186699": "Enterobacterales resistenti ai carbapenemi (colonizzazione)", "pubmed_38360651": "batteri da neutropenia febbrile (WISCA)",
    "pubmed_39057803": "E. coli STEC (ruminanti selvatici)", "pubmed_40142500": "uropatogeni nei lattanti, antibiotici orali",
    "pubmed_42090283": "uso di antibiotici (intelligenza artificiale)", "pubmed_41597159": "gestione antibiotica in pronto soccorso pediatrico",
    "pubmed_39204275": "batteri da emocoltura pediatrica", "pubmed_38641615": "Staphylococcus aureus meticillino-resistente (MRSA)",
    "pubmed_36551480": "geni di resistenza (T2Resistance) nella sepsi", "pubmed_34201722": "uso di ceftarolina",
    "pubmed_31466372": "K. pneumoniae resistente ai carbapenemi dopo AMS", "pubmed_26464061": "K. pneumoniae resistente ai carbapenemi (batteriemie)",
    "pubmed_21155410": "uso di antibiotici e patogeni ospedalieri (PPS)", "pubmed_30589074": "antibiotici perioperatori in chirurgia laringotracheale",
    "pubmed_22418605": "profilassi antibiotica chirurgica",
}

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def feature(geometry, place, level, basis, studies, extra_note=""):
    note = NOTE + (" " + extra_note if extra_note else "")
    return {"type": "Feature", "geometry": geometry, "properties": {
        "place": place, "geography_level": level, "geography_basis": basis,
        "study_count": len(studies), "study_ids": "; ".join(s["id"] for s in studies),
        "authors": " | ".join(s["authors"] for s in studies), "year": " | ".join(s["year"] for s in studies),
        "title": " | ".join(s["title"] for s in studies), "sector": " | ".join(s["sector"] for s in studies),
        "organism": " | ".join(s["organism"] for s in studies), "doi": " | ".join(s["doi"] for s in studies),
        "geography_note": note}}

def point(key):
    lon, lat, _l, _s = POINTS[key]
    return {"type": "Point", "coordinates": [round(lon, 6), round(lat, 6)]}

def place_basis(key, text):
    return f"{text} {POINTS[key][3]}"

def merge(geoms):
    if len(geoms) == 1:
        return geoms[0]
    polys = []
    for g in geoms:
        polys.extend([g["coordinates"]] if g["type"] == "Polygon" else g["coordinates"])
    return {"type": "MultiPolygon", "coordinates": polys}

def main():
    catalog = load_json(ROOT / "public/data/literature-catalog.json")
    by_id = {r["id"]: r for r in catalog["records"]}
    miss = set(by_id) - set(ORGANISM)
    if miss:
        raise SystemExit("Organismo mancante: " + ", ".join(sorted(miss)))

    def card(sid):
        r = by_id[sid]; doi = r.get("doi") or ""
        return {"id": sid, "authors": r["authors"], "year": str(r["year"]), "title": r["title"].rstrip("."),
                "sector": SECTOR[r["scope"]], "organism": ORGANISM[sid],
                "doi": f"https://doi.org/{doi}" if doi else r["source_url"]}

    mun = {f["properties"]["name"]: f["geometry"] for f in load_json(ROOT / "public/geography/atlas_municipalities.geojson")["features"]}
    prov = {f["properties"]["name"]: f["geometry"] for f in load_json(ROOT / "public/geography/atlas_provinces.geojson")["features"]}
    region = load_json(ROOT / "public/geography/atlas_region.geojson")["features"][0]["geometry"]

    layers = {k: [] for k in ["human", "veterinary", "food", "environment", "wildlife", "regional"]}
    placed = {}

    def add(layer, ids, geometry, place, level, basis, extra=""):
        for sid in ids:
            placed[sid] = placed.get(sid, "") + f"{level}: {place}; "
        layers[layer].append(feature(geometry, place, level, basis, [card(s) for s in ids], extra))

    P = lambda *ids: [f"pubmed_{i}" for i in ids]
    add("human", P("21820758", "26464061", "33401591", "36551480", "38186699", "31466372", "34201722", "21155410"),
        point("san_martino"), POINTS["san_martino"][2], "struttura",
        place_basis("san_martino", "Ospedale San Martino nominato nell'abstract o nel testo integrale (per lo studio multicentrico, dati per centro in tabella)."))
    add("human", P("23524898", "23906074", "25812459", "27558493", "33021597", "35740127", "40142500", "38360651", "39204275",
                   "38641615", "36710161", "36830127", "42090283", "41597159", "30589074"),
        point("gaslini"), POINTS["gaslini"][2], "struttura",
        place_basis("gaslini", "Istituto Gaslini nominato nell'abstract o nel testo integrale."))
    add("human", P("37627698"), point("galliera"), POINTS["galliera"][2], "struttura",
        place_basis("galliera", "Terapia intensiva degli E.O. Galliera nominata nell'abstract."))
    add("human", P("29229880"), point("lavagna"), POINTS["lavagna"][2], "struttura",
        place_basis("lavagna", "Ceppi forniti dall'Ospedale di Lavagna, ASL4 Liguria, nominato nell'abstract."))
    add("human", P("32490767"), point("albenga"), POINTS["albenga"][2], "struttura",
        place_basis("albenga", "Ospedale di Albenga nominato nell'abstract."))
    add("human", P("24906230", "35690266"), mun["Genova"], "Genova", "comune",
        "Gli autori dichiarano un ospedale di Genova senza nominarlo: si usa il poligono ISTAT del comune.")
    add("human", P("28668656"), prov["Genova"], "Città metropolitana di Genova", "provincia",
        "Tre principali ospedali per acuti dell'area metropolitana di Genova, non nominati: poligono ISTAT della Città metropolitana.")
    add("regional", P("29253622", "29273072", "29600324", "22418605", "30988332", "33801613", "34067207", "36558780", "39057803"),
        region, "Liguria", "regione",
        "Gli autori dichiarano la Liguria, ospedali o distretti non nominati, o campioni di fauna raccolti in regione senza scala più fine. Il contorno regionale non è un punto di misura.")

    if set(placed) != set(by_id):
        raise SystemExit(f"Copertura incompleta. Mancanti: {sorted(set(by_id)-set(placed))}. Extra: {sorted(set(placed)-set(by_id))}")
    names = {"human": "human_amr_evidence.geojson", "veterinary": "veterinary_amr_evidence.geojson",
             "food": "food_chain_amr_evidence.geojson", "environment": "environmental_amr_evidence.geojson",
             "wildlife": "wildlife_amr_evidence.geojson", "regional": "regional_study_outline.geojson"}
    for k, fn in names.items():
        (ROOT / "public/data" / fn).write_text(json.dumps({"type": "FeatureCollection", "features": layers[k]}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        print(fn, len(layers[k]), sum(f["properties"]["study_count"] for f in layers[k]))
    print("studi collocati:", len(placed))

if __name__ == "__main__":
    main()
