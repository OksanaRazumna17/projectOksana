class MovieQueries:
    def __init__(self, connection):
        self.connection = connection

    def search_movies_by_keyword(self, keyword):
        cursor = self.connection.cursor()
        query = f"SELECT title FROM film WHERE title LIKE '%{keyword}%'"
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def get_popular_movies(self):
        cursor = self.connection.cursor()
        query = "SELECT title FROM film ORDER BY rental_rate DESC LIMIT 10"
        cursor.execute(query)
        results = cursor.fetchall()
        return results

    def get_popular_queries(self):
        query_count = {}
        try:
            with open('search_logs.txt', 'r') as f:
                for line in f:
                    keyword = line.strip().replace("Search keyword: ", "")
                    if keyword in query_count:
                        query_count[keyword] += 1
                    else:
                        query_count[keyword] = 1
        except FileNotFoundError:
            return ["No logs found."]

        # Сортировка по частоте использования и выборка топ-5
        sorted_queries = sorted(query_count.items(), key=lambda item: item[1], reverse=True)
        top_queries = sorted_queries[:5]
        return top_queries







