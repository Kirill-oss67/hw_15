
query_1 = """"CREATE TABLE colors ( id INTEGER PRIMARY KEY AUTOINCREMENT , color VARCHAR(50) )"""
# Coздаем таблицу для связки один ко многим с цветами
query_2 = """CREATE TABLE breeds ( id INTEGER PRIMARY KEY AUTOINCREMENT , breed VARCHAR(50) ) """
# Coздаем таблицу для связки один ко многим с породами
query_3 = """ CREATE TABLE animal_type ( id INTEGER PRIMARY KEY AUTOINCREMENT , animal_type VARCHAR(50) )"""
# Coздаем таблицу для связки один ко многим с типами животных
query_4 = """ CREATE TABLE new_animals ( id INTEGER PRIMARY KEY AUTOINCREMENT , 
                animal_id VARCHAR(50), animal_type_id INTEGER, name VARCHAR(50), breed_id INTEGER,
                color_1_id INTEGER, color_2_id INTEGER, date_of_birth DATETIME,  FOREIGN KEY(animal_type_id) REFERENCES animal_type(id),
                 FOREIGN KEY(breed_id) REFERENCES breeds(id), FOREIGN KEY(color_1_id) REFERENCES colors(id),
                 FOREIGN KEY(color_2_id) REFERENCES colors(id))   """
# Создаем таблицу с характеристиками животных, которая будем ссылаться на таблицы с цветами , породами и типами животных
query_5 = """ CREATE TABLE outcome (id INTEGER PRIMARY KEY AUTOINCREMENT, animal_id INTEGER, subtype VARCHAR(50),
                `type` VARCHAR(50), month INTEGER, year INTEGER, age_upon_outcome VARCHAR(50),
                FOREIGN KEY(animal_id) REFERENCES new_animals(id) ) """
# Создаем основную таблицу которая ссылается на таблицу "new_animals"
query_6 = """ INSERT INTO colors (color)
                SELECT DISTINCT trim(color1) FROM animals
                UNION ALL
                SELECT DISTINCT trim(color2) FROM animals """
# заполняем данными из стандартной таблицы 'animals' таблицу с цветами
query_7 = """INSERT INTO breeds (breed)
            SELECT DISTINCT breed FROM animals """
# заполняем данными из стандартной таблицы 'animals' таблицу с породами
query_8 = """ INSERT INTO animal_type (animal_type)
            SELECT DISTINCT animal_type FROM animals """
# заполняем данными из стандартной таблицы 'animals' таблицу с видами животных
query_9 = """INSERT INTO outcome (animal_id, subtype, "type", "month", year, age_upon_outcome)
                SELECT animal_id, outcome_subtype, outcome_type, outcome_month, outcome_year, age_upon_outcome 
                FROM animals """
# заполняем данными из стандартной таблицы 'animals' таблицу с данными о отбытия из приюта и характериками события
query_10 = """INSERT INTO new_animals (animal_id, name, date_of_birth)
                SELECT DISTINCT animal_id, name, date_of_birth 
                FROM animals"""
# заполняем данными из стандартной таблицы новую таблицу с характеристиками животных
query_11 = """UPDATE new_animals SET(animal_type_id) = (
            SELECT animal_type.id
            FROM animal_type
            JOIN animals ON animals.animal_type = animal_type.animal_type 
            WHERE animals.animal_id  = new_animals.animal_id   )  """
# заполняем колонку вид животного айди в новой таблице с характеристиками животных , объединив со стандартной таблицей
query_12 = """UPDATE new_animals SET(breed_id) = (
            SELECT breeds.id 
            FROM breeds 
            JOIN animals ON animals.breed  = breeds.breed  
            WHERE animals.animal_id  = new_animals.animal_id  ) """
# заполняем колонку порода животного айди в новой таблице с характеристиками животных , объединив со стандартной таблицей
query_13 = """ UPDATE new_animals SET(color_1_id) = (
            SELECT colors.id 
            FROM colors 
            JOIN animals ON trim(animals.color1)  = colors.color
            WHERE animals.animal_id  = new_animals.animal_id  ) """
# заполняем колонку цвет животного1 айди в новой таблице с характеристиками животных , объединив со стандартной таблицей
query_14 = """UPDATE new_animals SET(color_2_id) = (
            SELECT colors.id 
            FROM colors 
            JOIN animals ON trim(animals.color2)  = colors.color
            WHERE animals.animal_id  = new_animals.animal_id  )"""
# заполняем колонку цвет животного2 айди в новой таблице с характеристиками животных , объединив со стандартной таблицей