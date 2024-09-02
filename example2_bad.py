def greet(name):
    print(name.upper())  # НЕТ ПРОВЕРКИ НА None


if __name__ == "__main__":
    greet("python")  # Все ок
    greet(None)  # AttributeError: 'NoneType' object has no attribute 'upper'
