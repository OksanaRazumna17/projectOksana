#1.cd C:\Users\oksus\PycharmProjects\pythonProject6\projectOksana
#2. python main.py
#3.При нажатии на 1 предлагаеться ввести слово для поиска, после введения происходит поиск по ключевому слову
#4 Нажать на 2 отображаються  10 топ популярных фильмов
#5 Нажать 3 отображаються 5 наиболее популярных запросов.
#6 Нажать 4 и выйти из программы

from db.connection import DatabaseConnection
from db.queries import MovieQueries
from ui.console import ConsoleInterface

def main():
    """Основная логика программы."""
    db_conn = DatabaseConnection(
        host="ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com",
        user="ich1",
        passwd="password",
        database="sakila"
    )

    console = ConsoleInterface()

    try:
        connection = db_conn.connect()
        queries = MovieQueries(connection)

        while True:
            console.display_help()
            command = console.get_user_input()

            if command == "4":
                break
            elif command == "1":
                keyword = input("Enter a keyword for search: ")
                results = queries.search_movies_by_keyword(keyword)
                console.display_results(results)
            elif command == "2":
                results = queries.get_popular_movies()
                console.display_results(results)
            elif command == "3":
                results = queries.get_popular_queries()
                console.display_popular_queries(results)
            else:
                console.display_message("Unknown command. Please try again.")
    except Exception as e:
        console.display_message(f"An error occurred: {e}")
    finally:
        db_conn.close()

if __name__ == "__main__":
    main()






