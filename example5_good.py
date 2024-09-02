# Вариант 1
file = open('example.txt', 'r')
print(file.read())

file.close()

# Вариант 2

with open("example.txt", "r") as file:
    print(file.read())
