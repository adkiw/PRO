# logic/darbuotojai.py
import sqlite3
from typing import List, Dict

def get_all(conn: sqlite3.Connection) -> List[Dict]:
    result = conn.execute("""
        SELECT id, vardas, pavarde, pareigybe, el_pastas, telefonas, grupe
        FROM darbuotojai
        ORDER BY id DESC
    """).fetchall()
    return [
        {
            "id": r[0],
            "vardas": r[1],
            "pavarde": r[2],
            "pareigybe": r[3],
            "el_pastas": r[4],
            "telefonas": r[5],
            "grupe": r[6],
        }
        for r in result
    ]

def insert(conn: sqlite3.Connection, data: Dict[str, str]) -> None:
    conn.execute("""
        INSERT INTO darbuotojai (
            vardas, pavarde, pareigybe, el_pastas, telefonas, grupe
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["vardas"],
        data["pavarde"],
        data["pareigybe"],
        data["el_pastas"],
        data["telefonas"],
        data["grupe"],
    ))
    conn.commit()

