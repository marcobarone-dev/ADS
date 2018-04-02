def merge_merge(data, l_start, l_end, r_start, r_end):
    l_aux, r_aux, data_aux = l_start, r_start, []
    if l_start == l_end and r_start == r_end:
        if data[l_aux] > data[r_aux]:
            data[l_aux], data[r_aux] = data[r_aux], data[l_aux]

    elif r_start == r_end:
        r_added = 0
        while r_added == 0:
            if data[r_aux] > data[l_aux]:
                data_aux.append(data[l_aux])
                l_aux += 1
            else:
                data_aux.append(data[r_aux])
                r_added = 1
        data_aux += data[l_aux:l_end+1]
        data[l_start:r_end+1] = data_aux

    else:
        while l_aux < l_end+1 and r_aux < r_end+1:
            if data[l_aux] <= data[r_aux]:
                data_aux.append(data[l_aux])
                l_aux += 1
            else:
                data_aux.append(data[r_aux])
                r_aux += 1
        if l_aux == l_end+1:
            data_aux += data[r_aux:r_end+1]
        else:
            data_aux += data[l_aux:l_end+1]
        data[l_start:r_end+1] = data_aux


def merge_division(data, start, middle, end):
    if start < end:
        l_start, l_middle, l_end = start, (start+middle)//2, middle
        middle += 1
        r_start, r_middle, r_end = middle, (middle+end)//2, end
        merge_division(data, l_start, l_middle, l_end)
        merge_division(data, r_start, r_middle, r_end)
        merge_merge(data, l_start, l_end, r_start, r_end)


def mergeSort(data):
    start, middle, end = 0, (len(data)-1)//2, len(data)-1
    if len(data) > 1:
        merge_division(data, start, middle, end)
    return data


input = [25, 40, 55, 20, 44, 35, 38, 99, 10, 65, 50]
result = mergeSort(input)
print(result)
