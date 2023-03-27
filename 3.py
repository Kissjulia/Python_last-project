# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
# байтовом типе.

for el in ['attribute', 'класс', 'функция', 'type']:
    try:
        print(el, type(el), el.encode('ascii'), ' - encoding to bytes successful ')
    except:
        print(el, type(el), ' - not valid input for bytes string')