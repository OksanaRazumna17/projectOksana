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
        query_counts = {}

        # Открываем файл логов и читаем его построчно
        with open('search_logs.txt', 'r') as f:
            for line in f:
                # Разбираем строку лога, чтобы извлечь ключевое слово
                if "Search keyword:" in line:
                    keyword = line.replace("Search keyword:", "").strip()
                    if keyword in query_counts:
                        query_counts[keyword] += 1
                    else:
                        query_counts[keyword] = 1

        # Сортируем запросы по частоте и возвращаем список
        sorted_queries = sorted(query_counts.items(), key=lambda item: item[1], reverse=True)
        return sorted_queries









