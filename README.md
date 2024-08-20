# ProjectOksana

## Приветствие

Добро пожаловать в ProjectOksana! Это учебный проект, направленный на создание консольного интерфейса для взаимодействия
с базой данных `sakila`. Проект представляет собой пример работы с базой данных MySQL и реализует функционал поиска 
фильмов и отображения статистики запросов.

## Описание проекта

ProjectOksana — это приложение с консольным интерфейсом, которое позволяет пользователю взаимодействовать с базой 
данных фильмов `sakila`. Приложение предоставляет возможность поиска фильмов по ключевому слову, отображения списка
самых популярных фильмов и запросов, а также записи выполненных поисковых запросов в отдельную таблицу базы данных.

### Основные компоненты проекта:

1. **DatabaseConnection**: Класс для управления подключением к базе данных.
2. **MovieQueries**: Класс для выполнения SQL-запросов к базе данных.
3. **ConsoleInterface**: Класс для взаимодействия с пользователем через консольный интерфейс.
4. **Основная программа (`main.py`)**: Объединяет все компоненты и обеспечивает основной рабочий процесс.

## Проделанная работа

В рамках проекта были выполнены следующие задачи:

1. **Создание и настройка подключения к базе данных**: Реализация класса `DatabaseConnection` для подключения к базе
данных MySQL.
2. **Разработка класса для выполнения запросов**: Класс `MovieQueries` был создан для выполнения SQL-запросов, таких 
как поиск фильмов по ключевому слову и получение популярных фильмов.
3. **Создание консольного интерфейса**: Разработка класса `ConsoleInterface`, который предоставляет удобный способ 
взаимодействия пользователя с приложением.
4. **Интеграция компонентов в основную программу**: В `main.py` была интегрирована логика, связывающая все части 
приложения, что позволило создать единое, рабочее приложение.

## Описание результата

Результатом работы является готовое консольное приложение, которое позволяет пользователям:

- Искать фильмы по ключевым словам.
- Получать список самых популярных фильмов на основе данных в базе.
- Отображать самые частые поисковые запросы пользователей.
- Вести лог поиска, записывая запросы в search_logs.txt файл.

Приложение успешно подключается к базе данных, выполняет запросы и предоставляет пользователю результаты через 
консольный интерфейс.

## Сложности, с которыми столкнулся

При разработке проекта возникли следующие сложности:

1. **Настройка базы данных**: В процессе разработки были проблемы с подключением к удаленной базе данных MySQL, а 
также с корректным выполнением запросов.
2. **Работа с правами доступа в Git**: Были сложности с настройкой и управлением доступом к репозиторию на GitHub, 
что потребовало исправления прав доступа и повторного ввода учетных данных.
3. **Отладка и тестирование**: Во время тестирования приложения возникали ошибки при выполнении SQL-запросов, что
потребовало дополнительного времени на их отладку и корректировку запросов.
4. **Организация кода**: Было необходимо правильно организовать код по модулям, чтобы обеспечить его читаемость и 
возможность дальнейшего расширения.

## Заключение

Проект предоставил ценный опыт работы с базами данных, интеграцией SQL-запросов в приложение и разработкой удобного 
пользовательского интерфейса для взаимодействия с данными. Надеюсь, этот проект будет полезен для дальнейшего изучения 
и улучшения навыков разработки.
# projectOksana