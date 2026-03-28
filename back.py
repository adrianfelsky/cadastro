import sqlite3 as sql

class Database:
    def __init__(self, db_name="clientes.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sql.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def execute(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)

    def fetchall(self):
        return self.cursor.fetchall()

    def commit(self):
        if self.conn:
            self.conn.commit()


class ClienteDAO:

    def __init__(self):
        self.db = Database()

    def create_table(self):
        self.db.connect()

        self.db.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                user TEXT,
                email TEXT,
                cpf TEXT
            )
        """)

        self.db.commit()
        self.db.disconnect()

    def insert(self, nome, user, email, cpf):
        self.db.connect()

        self.db.execute(
            "INSERT INTO clientes (nome, user, email, cpf) VALUES (?, ?, ?, ?)",
            (nome, user, email, cpf)
        )

        self.db.commit()
        self.db.disconnect()

    def view(self):
        self.db.connect()

        self.db.execute("SELECT * FROM clientes")
        rows = self.db.fetchall()

        self.db.disconnect()
        return rows

    def search(self, nome="", sobrenome="", email="", cpf=""):
        self.db.connect()

        self.db.execute("""
            SELECT * FROM clientes 
            WHERE nome=? OR user=? OR email=? OR cpf=?
        """, (nome, sobrenome, email, cpf))

        rows = self.db.fetchall()

        self.db.disconnect()
        return rows

    def update(self, id, nome, sobrenome, email, cpf):
        self.db.connect()

        self.db.execute("""
            UPDATE clientes 
            SET nome=?, user=?, email=?, cpf=? 
            WHERE id=?
        """, (nome, sobrenome, email, cpf, id))

        self.db.commit()
        self.db.disconnect()

    def delete(self, id):
        self.db.connect()

        self.db.execute("DELETE FROM clientes WHERE id=?", (id,))

        self.db.commit()
        self.db.disconnect()


if __name__ == "__main__":
    dao = ClienteDAO()
    dao.create_table()