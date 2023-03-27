# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Проверить кодировку файла по умолчанию.
# Принудительно открыть файл в формате Unicode и вывести его содержимое.
import csv
import locale
with open('test_file.txt') as f:
    for el_str in f:
        print(el_str)

f = open("test_file.txt", "w")
f.write('сетевое программирование\n', 'сокет\n', 'декоратор\n')

print(f)
f.close()
print(f)
with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str, end='')