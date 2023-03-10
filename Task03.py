# Задание 3.

# Определить, какие из слов «attribute», «класс», «функция», «type»
# невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

# Подсказки:
# --- используйте списки и циклы, не дублируйте функции
# --- обязательно!!! усложните задачу, "отловив" и обработав исключение,
# придумайте как это сделать

my_dict =\
    {
        'класс': 'class',
        'функция': 'function'
    }

my_list = ['attribute', 'класс', 'функция', 'type']
my_list_2 = []

for i in my_list:

    try:
        i = i.encode('ascii')
        my_list_2.append(i)

    except:
        print(f'{i} в кириллице, перевожу в латиницу!')

        i = my_dict[i].encode('ascii')
        my_list_2.append(i)

print(my_list_2)
