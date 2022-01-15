def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[min_index], array[i] = array[i], array[min_index]
    return array


if __name__ == "__main__":
    g_list = [1, 56, 41, 78, 7, 9, 1546, 3512, 651655, 301]
    result = selection_sort(g_list)
    print(result)
