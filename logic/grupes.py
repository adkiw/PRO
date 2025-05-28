import sqlite3
from typing import List, Dict, Any

def get_grupes(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    cur = conn.execute("""
        SELECT id, numeris, pavadinimas, aprasymas
        FROM grupes
        ORDER BY numeris
    """)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in rows]

def insert_grupe(conn: sqlite3.Connection, data: Dict[str, Any]) -> None:
    conn.execute("""
        INSERT INTO grupes (numeris, pavadinimas, aprasymas)
        VALUES (?, ?, ?)
    """, (
        data["numeris"],
        data["pavadinimas"],
        data["aprasymas"]
    ))
    conn.commit()

def update_grupe(conn: sqlite3.Connection, grupe_id: int, data: Dict[str, Any]) -> None:
    conn.execute("""
        UPDATE grupes
        SET numeris = ?, pavadinimas = ?, aprasymas = ?
        WHERE id = ?
    """, (
        data["numeris"],
        data["pavadinimas"],
        data["aprasymas"],
        grupe_id
    ))
    conn.commit()
