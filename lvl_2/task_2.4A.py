# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    return s.replace("!", "")


# Примеры использования:
print(remove_exclamation_marks("Hi! Hello!"))  # Ожидаемый результат: "Hi Hello"
print(remove_exclamation_marks(""))           # Ожидаемый результат: ""
print(remove_exclamation_marks("Oh, no!!!"))   # Ожидаемый результат: "Oh, no"
