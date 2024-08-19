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

            if command == "exit":
                break
            elif command.startswith("search "):
                keyword = command.split("search ", 1)[1]
                results = queries.search_movies_by_keyword(keyword)
                console.display_results(results)
            elif command == "popular_movies":
                results = queries.get_popular_movies()
                console.display_results(results)
            elif command == "popular_queries":
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








