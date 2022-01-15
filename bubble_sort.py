def bubble_sort(array):
    length = len(array) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(length):
            if array[i] > array[i + 1]:
                is_sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
        length = length - 1
    return array


if __name__ == "__main__":
    g_list = [9, 5, 7, 65, 48, 120, 6, 0]
    result = bubble_sort(g_list)
    print(result)
