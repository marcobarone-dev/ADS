def radixSort(data):
    num_digits = len(str(max(data)))
    data = [str(x).zfill(num_digits) for x in data]

    for digit in reversed(range(0, num_digits)):
        data_aux = [None] * len(data)
        counting, aux = [0] * 10, 0
        for value in data:
            counting[int(value[digit])] += 1

        for index in range(0, 10):
            aux += counting[index]
            counting[index] = aux

        for value in reversed(data):
            index_aux = counting[int(value[digit])] - 1
            counting[int(value[digit])] -= 1
            data_aux[index_aux] = value
        data = data_aux

    return [int(x) for x in data]


input = [5, 4, 7, 100, 8, 9, 2, 1, 3, 6]
result = radixSort(input)
print(result)
