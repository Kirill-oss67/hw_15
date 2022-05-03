import sqlite3


def sqlite3_start_connection(sqlite_query, params):
    """устанавливаем соединение и делаем запрос с параметром аргумента функции"""
    with sqlite3.connect("animal.db") as connection:
        cursor = connection.cursor()
        sqlite_query = sqlite_query  # используем наш запрос
        cursor.execute(sqlite_query, params)
        result = cursor.fetchall()
        return result


def get_data(id):
    """"формируем запрос и получаем данные, которые возвращаем"""
    sqlite_query = """SELECT outcome.animal_id, new_animals.name, new_animals.date_of_birth 
                            FROM outcome 
                            JOIN new_animals ON outcome.animal_id = new_animals.animal_id 
                            WHERE outcome.id == :id
                                """
    gotten_data = sqlite3_start_connection(sqlite_query, {'id': f'{id}'})
    dict_animal = {}
    for i in gotten_data:
        dict_animal["id"] = i[0]
        dict_animal["name"] = i[1]
        dict_animal["date_of_birth"] = i[2]

    return dict_animal
