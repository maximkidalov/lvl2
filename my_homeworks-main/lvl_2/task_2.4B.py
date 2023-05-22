# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s.endswith("!"):
        return s[:-1]
    else:
        return s

# Примеры использования:
print(remove_last_em("Hi!"))     # Ожидаемый результат: "Hi"
print(remove_last_em("Hi!!!"))   # Ожидаемый результат: "Hi!!"
print(remove_last_em("!Hi"))     # Ожидаемый результат: "!Hi"
