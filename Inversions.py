#MergeSortTree
#
# Напишите программу, которая для заданного массива A = a1, a2, . . . , an находит количество
# пар (i, j) таких, что i < j и ai > aj.
# Обратите внимание на то, что ответ может не влезать в int.
#
# Формат входных данных
# Первая строка входного файла содержит натуральное число n (1 < n < 100 000) — количество
# элементов массива. Вторая строка содержит n попарно различных элементов массива A — целых
# неотрицательных чисел, не превосходящих 10^9.
#
# Формат выходных данных
# В выходной файл выведите одно число — ответ на задачу.

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        middle = int(len(array)/2)
        left = merge_sort(array[:middle])
        right = merge_sort(array[middle:])

        print(f'left:', left, 'right: ', right)
        sort = merge(left, right)
        return sort

def merge(left, right):
    result = []
    inversions = 0
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            inversions += len(left) - i
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    print('res: ', result)
    print('inv', inversions)
    return result



n = input()
arr = [int(x) for x in input().split()]
print(arr)
print(merge_sort(arr))