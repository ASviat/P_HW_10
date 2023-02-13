# Задание 4.

# Преобразовать слова «разработка», «администрирование», «protocol»,
# «standard» из строкового представления в байтовое и выполнить
# обратное преобразование (используя методы encode и decode).

# Подсказки:
# --- используйте списки и циклы, не дублируйте функции

my_dict =\
    {
        'разработка': 'development',
        'администрирование': 'administration'
    }

my_list = ['разработка', 'администрирование', 'protocol', 'standard']
my_list_2 = []

for i in my_list:

    try:
        i = i.encode('ascii')
        my_list_2.append(i)

    except:
        print(f'"{i}" в кириллице, перевожу в латиницу!\n')

        i = my_dict[i].encode('ascii')
        my_list_2.append(i)

print(my_list_2)
print()

for i in my_list_2:

    i = i.decode('ascii')
    print(i, end=' ')
    print(type(i))
