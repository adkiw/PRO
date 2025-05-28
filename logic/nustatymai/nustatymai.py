import sqlite3
from typing import List

def get_categories(conn: sqlite3.Connection) -> List[str]:
    return [r[0] for r in conn.execute(
        "SELECT DISTINCT kategorija FROM lookup"
    ).fetchall()]

def get_values(conn: sqlite3.Connection, kategorija: str) -> List[str]:
    return [r[0] for r in conn.execute(
        "SELECT reiksme FROM lookup WHERE kategorija = ?", (kategorija,)
    ).fetchall()]

def insert_value(conn: sqlite3.Connection, kategorija: str, reiksme: str) -> None:
    conn.execute(
        "INSERT INTO lookup(kategorija,reiksme) VALUES(?,?)",
        (kategorija, reiksme.strip())
    )
    conn.commit()

def delete_value(conn: sqlite3.Connection, kategorija: str, reiksme: str) -> None:
    conn.execute(
        "DELETE FROM lookup WHERE kategorija = ? AND reiksme = ?",
        (kategorija, reiksme)
    )
    conn.commit()
