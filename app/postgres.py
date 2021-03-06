# installed
import psycopg2
from psycopg2 import extras


class PostgresClient(object):
    def __init__(self, host: str, db_name: str = "", user: str = "", password: str = "", port: int = 5432):
        self.connection = self.connect(host, db_name, user, password, port)
        self.cursor = self.connection.cursor(
            cursor_factory=extras.NamedTupleCursor)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.close()

    def connect(self, host: str, db_name: str, user: str, password: str, port: int):
        try:
            if user and password:
                return psycopg2.connect(
                    f"host={host} dbname={db_name} user={user} password={password} port={port}"
                )

            return psycopg2.connect(host, sslmode="require")
        except Exception as e:
            raise e

    def commit(self):
        try:
            self.connection.commit()
        except Exception as e:
            raise e

    def close(self):
        self.cursor.close()
        self.connection.close()

    def query(self, query: str, values: tuple = ()) -> None:
        self.cursor.execute(query, values)

    def find_all(self, query: str, values: tuple = ()) -> list:
        self.cursor.execute(query, values)
        return self.cursor.fetchall()

    def find_one(self, query: str, values: tuple = ()) -> object:
        self.cursor.execute(query, values)
        return self.cursor.fetchone()

    def find_many(self, query: str, values: tuple(), limit: int = 25) -> list:
        self.cursor.execute(query, values)
        return self.cursor.fetchmany(limit)
