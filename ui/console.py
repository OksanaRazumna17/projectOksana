
class ConsoleInterface:
    def get_user_input(self) -> str:
        return input("Enter command: ")

    def display_results(self, results):
        if results:
            for result in results:
                print(result[0])
        else:
            print("Фильмы не найдены.")

    def display_popular_queries(self, queries):
        print("Популярные запросы:")
        for query in queries:
            print(f"{query[0]} - {query[1]} запросов")

    def display_help(self):
        """Выводит список доступных команд."""
        print("\nAvailable commands:")
        print("1. search <ключевое слово> - Поиск фильмов по ключевому слову.")
        print("2. popular_movies - Вывод 10 самых популярных фильмов.")
        print("3. popular_queries - Вывод 5 наиболее популярных запросов.")
        print("4. exit - Выход из программы.")

    def display_message(self, message):
        """Выводит сообщение в консоль."""
        print(message)
