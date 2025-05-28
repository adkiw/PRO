import sqlite3
from typing import List, Dict, Any

def get_all_klientai(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """
    Grąžina visus klientus kaip žodynų sąrašą.
    """
    cur = conn.execute("""
        SELECT 
            id, 
            pavadinimas, 
            kontaktai, 
            salis, 
            miestas, 
            regionas, 
            vat_numeris 
        FROM klientai
        ORDER BY pavadinimas
    """)
    rows = cur.fetchall()
    cols = [description[0] for description in cur.description]
    return [dict(zip(cols, row)) for row in rows]

def insert_klientas(conn: sqlite3.Connection, data: Dict[str, Any]) -> None:
    """
    Įrašo naują klientą į DB.
    Laukia laukų: pavadinimas, kontaktai, salis, miestas, regionas, vat_numeris
    """
    conn.execute("""
        INSERT INTO klientai (
            pavadinimas, kontaktai, salis, miestas, regionas, vat_numeris
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["pavadinimas"].strip(),
        data.get("kontaktai", "").strip(),
        data.get("salis", "").strip(),
        data.get("miestas", "").strip(),
        data.get("regionas", "").strip(),
        data.get("vat_numeris", "").strip(),
    ))
    conn.commit()
