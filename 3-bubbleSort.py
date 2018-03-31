def bubbleSort(data):
    changes = 0
    for i in reversed(range(1, len(data))):
        for j in range(1, i+1):
            if data[j-1] > data[j]:
                data[j-1], data[j] = data[j], data[j-1]
                changes = 1
        if changes == 0:
            break
    return data


input = [25, 40, 55, 20, 44, 35, 38, 99, 10, 65, 50]
result = bubbleSort(input)
print(result)
