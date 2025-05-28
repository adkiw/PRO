import sqlite3
from typing import List, Dict, Any

def get_all_vairuotojai(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    cur = conn.execute("""
        SELECT id, vardas, pavarde, gimimo_metai, tautybe, priskirtas_vilkikas
        FROM vairuotojai
        ORDER BY pavarde, vardas
    """)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in rows]

def insert_vairuotojas(conn: sqlite3.Connection, data: Dict[str, Any]) -> None:
    conn.execute("""
        INSERT INTO vairuotojai (
            vardas, pavarde, gimimo_metai, tautybe, priskirtas_vilkikas
        ) VALUES (?, ?, ?, ?, ?)
    """, (
        data["vardas"],
        data["pavarde"],
        int(data.get("gimimo_metai", 0) or 0),
        data.get("tautybe", ""),
        data.get("priskirtas_vilkikas", "")
    ))
    conn.commit()

def update_vairuotojas(conn: sqlite3.Connection, vairuotojo_id: int, data: Dict[str, Any]) -> None:
    conn.execute("""
        UPDATE vairuotojai
        SET vardas = ?, pavarde = ?, gimimo_metai = ?, tautybe = ?, priskirtas_vilkikas = ?
        WHERE id = ?
    """, (
        data["vardas"],
        data["pavarde"],
        int(data.get("gimimo_metai", 0) or 0),
        data.get("tautybe", ""),
        data.get("priskirtas_vilkikas", ""),
        vairuotojo_id
    ))
    conn.commit()

def delete_vairuotojas(conn: sqlite3.Connection, vairuotojo_id: int) -> None:
    conn.execute("DELETE FROM vairuotojai WHERE id = ?", (vairuotojo_id,))
    conn.commit()
