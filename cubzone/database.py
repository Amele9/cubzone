import sqlite3


class Database:
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    def __init__(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            number_of_scrambles INTEGER,
            puzzle_type TEXT,
            account INTEGER
        )
        """)

    @property
    def tables(self):
        return Tables(self)

    def __del__(self):
        self.cur.close()
        self.con.close()


class Tables:
    def __init__(self, database: Database):
        self.database = database

    @property
    def settings(self):
        return Settings(self.database)


class Table:
    def __init__(self, database: Database):
        self.database = database


class Settings(Table):
    def get_number_of_scrambles(self, account: int):
        self.database.cur.execute("""
        SELECT number_of_scrambles FROM settings WHERE account = ? 
        """, [account])

        return self.handle_response(1)

    def get_puzzle_type(self, account: int):
        self.database.cur.execute("""
        SELECT puzzle_type FROM settings WHERE account = ?
        """, [account])

        return self.handle_response("333")

    def handle_response(self, default_value):
        response = self.database.cur.fetchone()
        if not response:
            return default_value
        return response[0]

    def update_settings(
            self, number_of_scrambles: str, puzzle_type: str, account: int
    ):
        self.database.cur.execute(
            "SELECT * FROM settings WHERE account = ?", [account]
        )

        response = self.database.cur.fetchone()
        if not response:
            self.database.cur.execute(
                "INSERT INTO settings (account) VALUES (?)", [account]
            )

        self.database.cur.execute("""
        UPDATE settings
        SET number_of_scrambles = ?,
            puzzle_type = ?
        WHERE account = ? 
        """, [number_of_scrambles, puzzle_type, account])

        self.database.con.commit()


__all__ = ["Database"]
