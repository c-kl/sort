def selection_sort(array):
    """
    选择排序
    :param array: 一个乱序数列
    :return: 一个从小到大排序的数列
    """
    # 外层循环遍历(每次找到当前未遍历的最小值)
    for i in range(len(array) - 1):
        # min_index记录当前的最小值
        min_index = i
        for j in range(i+1, len(array)):
            # 如果当前的值比min_index记录的最小值小
            if array[j] < array[min_index]:
                # 交换当前值(更小)和min_index的索引
                min_index = j
        # 如果过min_index发生过变化
        if min_index != i:
            # 将min_index(记录当前最小值的索引）和i的值进行交换
            array[min_index], array[i] = array[i], array[min_index]
    return array


if __name__ == "__main__":
    g_list = [1, 56, 41, 78, 7, 9, 1546, 3512, 651655, 301]
    result = selection_sort(g_list)
    print(result)
