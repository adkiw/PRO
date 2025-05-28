import sqlite3
from typing import List, Dict, Any

def get_vilkikai(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    cur = conn.execute("""
        SELECT v.id, v.numeris, v.marke, v.pagaminimo_metai,
               v.tech_apziura, v.vadybininkas, v.vairuotojai,
               v.priekaba, p.tech_apziura AS priekabu_tech_apziura
        FROM vilkikai v
        LEFT JOIN priekabos p ON v.priekaba = p.numeris
        ORDER BY v.numeris
    """)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in rows]

def get_all_priekabos(conn: sqlite3.Connection) -> List[str]:
    result = conn.execute("SELECT numeris FROM priekabos ORDER BY numeris").fetchall()
    return [r[0] for r in result]

def insert_vilkikas(conn: sqlite3.Connection, data: Dict[str, Any]) -> None:
    conn.execute("""
        INSERT INTO vilkikai (
            numeris, marke, pagaminimo_metai, tech_apziura,
            vadybininkas, vairuotojai, priekaba
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["numeris"],
        data.get("marke", ""),
        int(data.get("pagaminimo_metai", 0) or 0),
        data.get("tech_apziura", ""),
        data.get("vadybininkas", ""),
        data.get("vairuotojai", ""),
        data.get("priekaba", "")
    ))
    conn.commit()

def update_priekaba(conn: sqlite3.Connection, vilkiko_id: int, nauja_priekaba: str) -> None:
    conn.execute("UPDATE vilkikai SET priekaba = ? WHERE id = ?", (nauja_priekaba, vilkiko_id))
    conn.commit()

def delete_vilkikas(conn: sqlite3.Connection, vilkiko_id: int) -> None:
    conn.execute("DELETE FROM vilkikai WHERE id = ?", (vilkiko_id,))
    conn.commit()
