# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:
import sqlite3

# Создаем подключение к базе данных
conn = sqlite3.connect('teacher.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем таблицу Students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Students (
        Student_Id INTEGER PRIMARY KEY,
        Student_Name TEXT,
        School_Id INTEGER
    )
''')

# Создаем таблицу Schools
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Schools (
        School_Id INTEGER PRIMARY KEY,
        School_Name TEXT
    )
''')

# Вставляем данные в таблицу Students
students_data = [
    (201, 'Иван', 1),
    (202, 'Петр', 2),
    (203, 'Анастасия', 3),
    (204, 'Игорь', 4)
]
cursor.executemany('REPLACE INTO Students VALUES (?, ?, ?)', students_data)

# Вставляем данные в таблицу Schools
schools_data = [
    (1, 'Школа 1'),
    (2, 'Школа 2'),
    (3, 'Школа 3'),
    (4, 'Школа 4')
]
cursor.executemany('REPLACE INTO Schools VALUES (?, ?)', schools_data)

# Сохраняем изменения
conn.commit()


# Функция для получения информации о студенте и его школе по ID студента
def get_student_info(student_id):
    cursor.execute('''
        SELECT Students.Student_Id, Students.Student_Name, Students.School_Id, Schools.School_Name
        FROM Students
        JOIN Schools ON Students.School_Id = Schools.School_Id
        WHERE Students.Student_Id = ?
    ''', (student_id,))
    student_info = cursor.fetchone()
    return student_info


# Пример использования функции
student_id = 203
student_info = get_student_info(student_id)

if student_info:
    print("ID студента:", student_info[0])
    print("Имя студента:", student_info[1])
    print("ID школы:", student_info[2])
    print("Название школы:", student_info[3])
else:
    print("Студент не найден")

# Закрываем соединение с базой данных
conn.close()
