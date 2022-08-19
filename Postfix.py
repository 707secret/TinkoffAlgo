str = input().split()

stek = []
result = 0

for i in range(0, len(str)):
    if str[i].isdigit:
        stek.append(str[i])
    if str[i] == "+":
        result = int(stek[0]) + int(stek[1])
        stek.clear()
        stek.append(result)
    if str[i] == "-":
        result = int(stek[0]) - int(stek[1])
        stek.clear()
        stek.append(result)
    if str[i] == "*":
        result = int(stek[0]) * int(stek[1])
        stek.clear()
        stek.append(result)
    if str[i] == "/":
        result = int(stek[0]) / int(stek[1])
        stek.clear()
        stek.append(result)

print(stek)