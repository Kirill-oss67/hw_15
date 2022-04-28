import sqlite3


def sqlite3_start_connection(sqlite_query):
    """устанавливаем соединение и делаем запрос с параметром аргумента функции"""
    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()
        sqlite_query = sqlite_query  # используем наш запрос
        cursor.execute(sqlite_query)
        result = cursor.fetchall()
        return result
