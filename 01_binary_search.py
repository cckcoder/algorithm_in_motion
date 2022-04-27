def binary_search(list, search_item):

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == search_item:
            return mid
        elif guess > search_item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_lists = [1, 3, 5, 7, 9, 11]
# my_lists = sorted(my_lists)
print(binary_search(my_lists, 3))
