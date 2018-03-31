def selectionSort(data):
    for index in range(0, len(data)-1):
        aux_minor = data[index]
        for minor in range(index+1, len(data)):
            if data[minor] < aux_minor:
                aux_minor = data[minor]
        data[index] = aux_minor
    return data


input = [25, 40, 55, 20, 44, 35, 38, 99, 10, 65, 50]
result = selectionSort(input)
print(result)
