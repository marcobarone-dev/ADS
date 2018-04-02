def sequentialSearch(data, item):
    for value in data:
        if item == value:
            return True, 'Found {}'.format(item)
    return False, 'Not found {}'.format(item)


input = [12, 7, 5, 9, 51, 8, 1, 10]
item_1 = 5
item_2 = -4

bol, result = sequentialSearch(input, item_1)
print(result)

bol, result = sequentialSearch(input, item_2)
print(result)
