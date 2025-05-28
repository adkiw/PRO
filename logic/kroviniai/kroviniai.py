import sqlite3
from typing import List, Dict, Any

def get_all_kroviniai(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """
    Grąžina visų krovinių sąrašą su pagrindine informacija.
    """
    cur = conn.execute("""
        SELECT
            id,
            klientas,
            uzsakymo_numeris,
            pakrovimo_data,
            pakrovimo_laikas_nuo,
            pakrovimo_laikas_iki,
            iskrovimo_data,
            iskrovimo_laikas_nuo,
            iskrovimo_laikas_iki,
            pakrovimo_salis,
            pakrovimo_miestas,
            iskrovimo_salis,
            iskrovimo_miestas,
            vilkikas,
            priekaba,
            atsakingas_vadybininkas,
            kilometrai,
            frachtas,
            svoris,
            paleciu_skaicius,
            busena
        FROM kroviniai
        ORDER BY pakrovimo_data DESC, pakrovimo_laikas_nuo
    """)
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in cur.fetchall()]

def insert_krovinys(conn: sqlite3.Connection, data: Dict[str, Any]) -> None:
    """
    Įrašo naują krovinį į DB.
    Privalomi laukai: klientas, uzsakymo_numeris, pakrovimo_data, iskrovimo_data.
    """
    conn.execute("""
        INSERT INTO kroviniai (
            klientas, uzsakymo_numeris, pakrovimo_numeris,
            pakrovimo_data, pakrovimo_laikas_nuo, pakrovimo_laikas_iki,
            iskrovimo_data, iskrovimo_laikas_nuo, iskrovimo_laikas_iki,
            pakrovimo_salis, pakrovimo_miestas,
            iskrovimo_salis, iskrovimo_miestas,
            vilkikas, priekaba, atsakingas_vadybininkas,
            kilometrai, frachtas, svoris, paleciu_skaicius, busena
        ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    """, (
        data["klientas"].strip(),
        data["uzsakymo_numeris"].strip(),
        data.get("pakrovimo_numeris","").strip(),
        data["pakrovimo_data"],
        data["pakrovimo_laikas_nuo"],
        data["pakrovimo_laikas_iki"],
        data["iskrovimo_data"],
        data["iskrovimo_laikas_nuo"],
        data["iskrovimo_laikas_iki"],
        data["pakrovimo_salis"].strip(),
        data["pakrovimo_miestas"].strip(),
        data["iskrovimo_salis"].strip(),
        data["iskrovimo_miestas"].strip(),
        data.get("vilkikas","").strip(),
        data.get("priekaba","").strip(),
        data.get("atsakingas_vadybininkas","").strip(),
        int(data.get("kilometrai",0)),
        float(data.get("frachtas",0)),
        int(data.get("svoris",0)),
        int(data.get("paleciu_skaicius",0)),
        data.get("busena","").strip()
    ))
    conn.commit()

def update_krovinys(conn: sqlite3.Connection, krovinio_id: int, data: Dict[str, Any]) -> None:
    """
    Atnaujina esamo krovinio informaciją.
    Galima atnaujinti visus laukus po pageidavimu.
    """
    fields = []
    params = []
    for key in [
        "klientas","uzsakymo_numeris","pakrovimo_numeris",
        "pakrovimo_data","pakrovimo_laikas_nuo","pakrovimo_laikas_iki",
        "iskrovimo_data","iskrovimo_laikas_nuo","iskrovimo_laikas_iki",
        "pakrovimo_salis","pakrovimo_miestas",
        "iskrovimo_salis","iskrovimo_miestas",
        "vilkikas","priekaba","atsakingas_vadybininkas",
        "kilometrai","frachtas","svoris","paleciu_skaicius","busena"
    ]:
        if key in data:
            fields.append(f"{key} = ?")
            val = data[key]
            # konvertuojam skaitmeninius laukus
            if key in ("kilometrai","svoris","paleciu_skaicius"):
                val = int(val or 0)
            if key == "frachtas":
                val = float(val or 0)
            params.append(val)
    if not fields:
        return
    params.append(krovinio_id)
    sql = f"UPDATE kroviniai SET {', '.join(fields)} WHERE id = ?"
    conn.execute(sql, params)
    conn.commit()

def delete_krovinys(conn: sqlite3.Connection, krovinio_id: int) -> None:
    """
    Ištrina krovinį pagal ID.
    """
    conn.execute("DELETE FROM kroviniai WHERE id = ?", (krovinio_id,))
    conn.commit()
