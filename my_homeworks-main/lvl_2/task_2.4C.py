# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    words = s.split()  # Разбиваем строку на слова
    result = []
    for word in words:
        if word.count("!") != 1:  # Проверяем, содержит ли слово ровно один восклицательный знак
            result.append(word)
    return " ".join(result)

# Примеры использования:
print(remove_word_with_one_em("Hi!"))               # Ожидаемый результат: ""
print(remove_word_with_one_em("Hi! Hi!"))           # Ожидаемый результат: ""
print(remove_word_with_one_em("Hi! Hi! Hi!"))       # Ожидаемый результат: ""
print(remove_word_with_one_em("Hi Hi! Hi!"))        # Ожидаемый результат: "Hi"
print(remove_word_with_one_em("Hi! !Hi Hi!"))       # Ожидаемый результат: ""
print(remove_word_with_one_em("Hi! Hi!! Hi!"))      # Ожидаемый результат: "Hi!!"
print(remove_word_with_one_em("Hi! !Hi! Hi!"))      # Ожидаемый результат: "!Hi!"
