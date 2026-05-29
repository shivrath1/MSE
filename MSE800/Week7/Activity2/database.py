import sqlite3


def create_connection():
    conn = sqlite3.connect("aquarium.db")
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    
    # Fish Table
    cursor.execute('''

        CREATE TABLE IF NOT EXISTS fish (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL

        )

    ''')
    # Aquarium Details Table
    cursor.execute('''

        CREATE TABLE IF NOT EXISTS aquariumDetails (

            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL

        )

    ''')
    # Aquarium Fish Mapping Table
    cursor.execute('''

        CREATE TABLE IF NOT EXISTS aquariumFish (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            aquarium_id INTEGER,
            fish_id INTEGER,
            count INTEGER,

            FOREIGN KEY(aquarium_id)
            REFERENCES aquariumDetails(id),

            FOREIGN KEY(fish_id)
            REFERENCES fish(id)
        )

    ''')

    conn.commit()
    conn.close()


create_table()