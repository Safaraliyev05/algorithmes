import psycopg2
from psycopg2 import pool


class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def __init__(self, db_name, user, password, host, port):
        if not hasattr(self, 'connection_pool'):
            self.connection_pool = psycopg2.pool.SimpleConnectionPool(
                1, 10,
                database=db_name,
                user=user,
                password=password,
                host=host,
                port=port
            )

#     def get_connection(self):
#         return self.connection_pool.getconn()
#
#     def release_connection(self, connection):
#         self.connection_pool.putconn(connection)
#
#
# db = Database("vazifa", "postgres", "1337", "localhost", "5432")
# conn = db.get_connection()
#
# with conn.cursor() as cursor:
#     cursor.execute("SELECT version();")
#     print(cursor.fetchone())
#
# db.release_connection(conn)

db1 = Database("vazifa", "postgres", "1337", "localhost", "5432")
db2 = Database("vazifa", "postgres", "1337", "localhost", "5432")

print(db1 is db2)
