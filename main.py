def counting_sort(arr):
    count = []
    result = []

    for i in range(0, 10):
        count.append(0)

    for i in range(len(arr)):
        count[arr[i] - 1] += 1
        print(i, ' ', count)

    for i in range(len(count)):
        result.append(count[i]*(i+1))
        print(result)
        # 1 2 1 4 arr[i]
        # 0 1 2 3 i

    return result

arr = [int(x) for x in input().split()]

print(counting_sort(arr))