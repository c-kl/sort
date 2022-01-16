def bubble_sort(array):
    """
    冒泡排序
    :param array:一个乱序数列
    :return:一个从小到大排序的数列
    """
    # 因为是array[i]和array[i+1]比较
    # 所以length为len(array) - 1
    length = len(array) - 1
    is_sorted = False
    # 未排序完则继续while循环
    while not is_sorted:
        is_sorted = True
        # 每次for循环只能确定最后一个没排序的数字
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
