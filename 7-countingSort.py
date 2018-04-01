def countingSort(data, start_range, end_range):
    diff_values = end_range - start_range + 1
    counting = [0] * diff_values
    data_aux = [None] * len(data)
    for value in data:
        index = value - start_range
        counting[index] += 1

    aux = 0
    for index in range(0, diff_values):
        aux += counting[index]
        counting[index] = aux

    for value in reversed(data):
        index_count = value - start_range
        index_aux = counting[index_count] - 1
        counting[index_count] -= 1
        data_aux[index_aux] = value

    return data_aux


input = [5, 4, 7, 10, 8, 9, 2, 1, 3, 6]
result = countingSort(input, min(input), max(input))
print(result)
