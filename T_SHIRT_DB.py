import sqlite3 as sq
with sq.connect("t_shirts.db") as con:
    con.row_factory = sq.Row
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY DEFAULT 1,
            t_shirt_photo BLOB DEFAULT 0,
            t_shirt_print_photo BLOB NOT NULL DEFAULT 0,
            price INTEGER NOT NULL DEFAULT 0,
            size_l_amount INTEGER NOT NULL DEFAULT 0,
            size_m_amount INTEGER NOT NULL DEFAULT 0,
            t_shirt_description TEXT
    )""")