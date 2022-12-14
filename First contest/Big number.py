# Формат входных данных
# Входной файл содержит одну или более строк, каждая из которых содержит последовательность
# цифр. Количество строк во входном файле не превышает 10000, каждая строка содержит от 1 до
# 100 цифр. Гарантируется, что хотя бы в одной строке первая цифра отлична от нуля.
#
# Формат результата
# Выведите в выходной файл одну строку — максимальное число, которое могло быть написано
# на полоске перед разрезанием.
#
# Ограничение времени:	1 с
# Ограничение памяти:	256M

from functools import cmp_to_key

def max_number(x, y):
    return 1 if x + y > y + x else -1

numbers_list = [int(i) for i in iter(input, '')]
numbers_list.sort(key=cmp_to_key(max_number), reverse=True)

print(numbers_list)
