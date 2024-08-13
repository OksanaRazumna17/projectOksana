class ConsoleInterface:
    def get_user_input(self) -> str:
        return input("Enter command: ")

    def display_results(self, results):
        if results:
            for result in results:
                print(result[0])
        else:
            print("Фільми не знайдені.")

    def display_popular_queries(self, queries):
        print("Популярні запити:")
        for query in queries:
            print(f"{query[0]} - {query[1]} запитів")
