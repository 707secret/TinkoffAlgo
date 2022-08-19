# # В постфиксной записи (или обратной польской записи) операция записывается после двух операндов.
#
# Формат входных данных
# В единственной строке записано выражение в постфиксной записи, содержащее цифры и операции +, −, ∗.
# Числа и операции разделяются пробелами. В конце строки может быть произвольное количество пробелов.
#
# Формат выходных данных
# Необходимо вывести значение записанного выражения.

def postfix_record(postfix):
    result = []

    for i in postfix:
        if i.isdigit():
            result.append(int(i))
            continue

        y = result.pop()
        x = result.pop()

        if i == "+":
            result.append(int(x) + int(y))
        elif i == "-":
            result.append(int(x) - int(y))
        elif i == "*":
            result.append(int(x) * int(y))

    return result[0]

string = input().split()
print(postfix_record(string))