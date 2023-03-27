# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

for el in ['разработка', 'администрирование', 'protocol', 'standard']:
    b = el.encode('utf-8', 'replace')
    s = b.decode('utf-8')
    print(el, b, s)