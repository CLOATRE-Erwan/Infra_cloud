import psycopg2


class Data:

    @classmethod
    def open_db(cls):
        cls.conn = psycopg2.connect(database="change to your db name", user="change to your username", password="change to your password", host="change to your endpoint", port='5432')
        cls.cur = cls.conn.cursor()

    @classmethod
    def close_db(cls):
        cls.cur.close()
        cls.conn.close()

    @classmethod
    def name(cls):
        cls.open_db()
        cls.cur.execute('select name, membercost from cd.facilities;')
        query_results = cls.cur.fetchall()
        cls.close_db()
        return query_results

    @classmethod
    def tennis(cls):
        cls.open_db()
        cls.cur.execute("""select * from cd.facilities where name like '%Tennis%';""")
        query_results = cls.cur.fetchall()
        cls.close_db()
        return query_results
        