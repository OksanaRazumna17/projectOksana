from db.connection import DatabaseConnection
from db.queries import MovieQueries


def print_results(results):
    if results:
        for result in results:
            print(result)
    else:
        print("No results found.")


def main():
    # Подключаемся к базе данных sakila для выполнения запросов
    db_conn = DatabaseConnection(
        host="ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com",
        user="ich1",
        passwd="password",
        database="sakila"
    )
    connection = db_conn.connect()
    queries = MovieQueries(connection)

    try:
        while True:
            # Ввод команды
            print("\nAvailable commands:")
            print("1. search <ключевое слово> - Поиск фильмов по ключевому слову.")
            print("2. popular_movies - Вывод 10 самых популярных фильмов.")
            print("3. popular_queries - Вывод 5 наиболее популярных запросов.")
            print("4. exit - Выход из программы.")
            command = input("Enter command: ")

            if command == "exit":
                break
            elif command.startswith("search "):
                keyword = command.split("search ", 1)[1]
                results = queries.search_movies_by_keyword(keyword)
                queries.log_search_query(keyword)  # Записываем запрос в другую базу данных
                print_results(results)
            elif command == "popular_movies":
                results = queries.get_popular_movies()
                print_results(results)
            elif command == "popular_queries":
                results = queries.get_popular_queries()
                print_results(results)
            else:
                print("Unknown command. Please try again.")
    finally:
        db_conn.close()  # Закрываем соединение с базой данных


if __name__ == "__main__":
    main()





