
import sqlite3

def init_db():
    conn = sqlite3.connect("dispo_new.db", check_same_thread=False)
    c = conn.cursor()

    # Universali lookup lentelė (markės, pareigos, būsena ir pan.)
    c.execute("""
        CREATE TABLE IF NOT EXISTS lookup (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            kategorija TEXT,
            reiksme TEXT UNIQUE
        )
    """)

    # Priekabos
    c.execute("""
        CREATE TABLE IF NOT EXISTS priekabos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numeris TEXT UNIQUE,
            marke TEXT,
            pagaminimo_metai INTEGER,
            tech_apziura DATE
        )
    """)

    # Vilkikai
    c.execute("""
        CREATE TABLE IF NOT EXISTS vilkikai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numeris TEXT UNIQUE,
            marke TEXT,
            pagaminimo_metai INTEGER,
            tech_apziura DATE,
            vadybininkas TEXT,
            vairuotojai TEXT,
            priekaba TEXT
        )
    """)

    # Galim pridėti daugiau lentelių čia vėliau (kroviniai, klientai, darbuotojai)

    conn.commit()
    return conn, c
