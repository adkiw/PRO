import sqlite3
from typing import List, Dict, Any
import pandas as pd

def get_all(conn: sqlite3.Connection) -> pd.DataFrame:
    return pd.read_sql_query("SELECT * FROM vilkikai", conn)

def get_all_with_priekabos(conn: sqlite3.Connection) -> pd.DataFrame:
    return pd.read_sql_query("""
        SELECT vilkikai.*,
               priekabos.marke AS priekabos_marke,
               priekabos.tech_apziura AS priekabos_tech_apziura
        FROM vilkikai
        LEFT JOIN priekabos ON vilkikai.priekaba = priekabos.numeris
    """, conn)

def get_all_priekabos(conn: sqlite3.Connection) -> List[str]:
    result = conn.execute("SELECT numeris FROM priekabos").fetchall()
    return [r[0] for r in result]

def insert(conn: sqlite3.Connection, data: Dict[str, Any]) -> None:
    conn.execute("""
        INSERT INTO vilkikai (
            numeris, marke, pagaminimo_metai, tech_apziura,
            vadybininkas, vairuotojai, priekaba
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["numeris"],
        data["marke"],
        int(data["pagaminimo_metai"]),
        data["tech_apziura"],
        data["vadybininkas"],
        data["vairuotojai"],
        data["priekaba"]
    ))
    conn.commit()

def update_priekaba(conn: sqlite3.Connection, vilkiko_id: int, nauja_priekaba: str) -> None:
    conn.execute("""
        UPDATE vilkikai SET priekaba = ? WHERE id = ?
    """, (nauja_priekaba, vilkiko_id))
    conn.commit()
