import sqlite3
from typing import List, Dict, Any

def get_all_priekabos(conn: sqlite3.Connection) -> List[Dict[str, Any]]:
    """
    Grąžina visų priekabų sąrašą kaip žodynų sąrašą.
    """
    cur = conn.execute("""
        SELECT 
            id,
            priekabu_tipas,
            numeris,
            marke,
            pagaminimo_metai,
            tech_apziura,
            priskirtas_vilkikas
        FROM priekabos
        ORDER BY numeris
    """)
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    return [dict(zip(cols, row)) for row in rows]

def insert_priekaba(conn: sqlite3.Connection, data: Dict[str, Any]) -> None:
    """
    Įrašo naują priekabą į DB.
    Laukia laukų: priekabu_tipas, numeris, marke, pagaminimo_metai, tech_apziura, priskirtas_vilkikas
    """
    conn.execute("""
        INSERT INTO priekabos (
            priekabu_tipas,
            numeris,
            marke,
            pagaminimo_metai,
            tech_apziura,
            priskirtas_vilkikas
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["priekabu_tipas"].strip(),
        data["numeris"].strip(),
        data.get("marke", "").strip(),
        int(data.get("pagaminimo_metai", 0)),
        data["tech_apziura"],  # tikimės str arba date objektas
        data.get("priskirtas_vilkikas", "").strip(),
    ))
    conn.commit()

def update_priekaba(conn: sqlite3.Connection, priekaba_id: int, data: Dict[str, Any]) -> None:
    """
    Atnaujina esamos priekabos laukus.
    data gali turėti bet kurį iš šių raktažodžių:
      priekabu_tipas, marke, pagaminimo_metai, tech_apziura, priskirtas_vilkikas
    """
    # Sudėliosime SET dalį pagal pateiktus laukus
    fields = []
    params = []
    for key in ("priekabu_tipas", "marke", "pagaminimo_metai", "tech_apziura", "priskirtas_vilkikas"):
        if key in data:
            fields.append(f"{key} = ?")
            # jei metai – į int
            val = int(data[key]) if key == "pagaminimo_metai" else data[key]
            params.append(val)
    if not fields:
        return  # nieko nereikia atnaujinti
    params.append(priekaba_id)
    sql = f"UPDATE priekabos SET {', '.join(fields)} WHERE id = ?"
    conn.execute(sql, params)
    conn.commit()
