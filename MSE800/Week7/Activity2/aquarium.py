from database import create_connection
from factory import FishFactory


class AquariumManager:

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def add_fish(self, fish_name):
        fish = FishFactory.create_fish(fish_name)
        if fish is None:
            print("Invalid Fish")
            return
        conn = create_connection()
        cursor = conn.cursor()

        # Insert fish into fish table
        cursor.execute("""
            INSERT INTO fish(name, category)
            VALUES (?, ?)
        """, (fish_name, fish.category()))
        conn.commit()
        conn.close()

        print(f"{fish_name} added successfully")