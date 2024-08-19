class ConsoleInterface:
    def display_help(self):
        """Выводит список доступных команд."""
        print("\nAvailable commands:")
        print("1. search <ключевое слово> - Поиск фильмов по ключевому слову.")
        print("2. popular_movies - Вывод 10 самых популярных фильмов.")
        print("3. popular_queries - Вывод 5 наиболее популярных запросов.")
        print("4. exit - Выход из программы.")

    def get_user_input(self):
        """Получает ввод пользователя."""
        return input("Enter command: ")

    def display_results(self, results):
        """Выводит результаты запросов."""
        if results:
            for result in results:
                print(result[0])  # Предполагается, что result[0] содержит название фильма
        else:
            print("No results found.")

    def display_popular_queries(self, results):
        """Выводит результаты популярных запросов."""
        if results:
            for result in results:
                print(f"{result[0]}: {result[1]} times")
        else:
            print("No popular queries found.")

    def display_message(self, message):
        """Выводит сообщение в консоль."""
        print(message)

