def insertionSort(data):
    for index in range(1, len(data)):
        value = data[index]
        aux_index = index - 1
        while value < data[aux_index] and aux_index > -1:
            data[aux_index + 1] = data[aux_index]
            aux_index -= 1
        data[aux_index + 1] = value
    return data


input = [25, 40, 55, 20, 44, 35, 38, 99, 10, 65, 50]
result = insertionSort(input)
print(result)
