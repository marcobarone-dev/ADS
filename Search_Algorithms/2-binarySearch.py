def binarySearch(data, item):
    data_size = len(data)
    middle = data_size//2
    if item == data[middle]:
        return True, 'Found {}'.format(item)
    elif item < data[middle] and data_size > 1:
        return binarySearch(data[:middle], item)
    elif item > data[middle] and data_size > 1:
        return binarySearch(data[middle+1:], item)
    else:
        return False, 'Not found {}'.format(item)


input = [1, 2, 4, 7, 8, 10, 13, 15, 17, 18, 29, 32, 35]
item_1 = 4
item_2 = 33

bol, result = binarySearch(input, item_1)
print(result)

bol, result = binarySearch(input, item_2)
print(result)
