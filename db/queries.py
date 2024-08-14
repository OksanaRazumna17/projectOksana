class MovieQueries:
    def __init__(self, connection):
        self.connection = connection

    def search_movies_by_keyword(self, keyword: str):
        cursor = self.connection.cursor()
        query = "SELECT title FROM film WHERE title LIKE %s LIMIT 10"
        cursor.execute(query, ('%' + keyword + '%',))
        return cursor.fetchall()

    def get_popular_movies(self):
        cursor = self.connection.cursor()
        query = """
        SELECT title, COUNT(*) as popularity
        FROM film
        GROUP BY title
        ORDER BY popularity DESC
        LIMIT 10
        """
        cursor.execute(query)
        return cursor.fetchall()

    def get_popular_queries(self):
        cursor = self.connection.cursor()
        query = """
        SELECT query, COUNT(*) as count
        FROM 310524ptm_oksana.search_log
        GROUP BY query
        ORDER BY count DESC
        LIMIT 5
        """
        cursor.execute(query)
        return cursor.fetchall()

    def log_search_query(self, query: str):
        cursor = self.connection.cursor()
        insert_query = "INSERT INTO 310524ptm_oksana.search_log (query) VALUES (%s)"
        cursor.execute(insert_query, (query,))
        self.connection.commit()





