def insertion_sort(array):
    """
    插入循环
    :param array: 一个乱序数列
    :return: 一个从小到大排序的数列
    """
    # 从索引1开始循环遍历
    for i in range(1, len(array)):
        # 用变量记录i的值和索引
        index = i
        value = array[i]
        # 如果上一个索引的值大于i的值，将其后移(可能移动不止一个值)
        # 例如索引5被取出来，索引234(前面的都是排序好的)的值都比索引5的大
        # 这时234都向后移动一格，将5的值插入到索引2
        while array[index - 1] > value:
            array[index] = array[index - 1]
            index = index - 1
        # 将value记录的值插入到index中
        array[index] = value
    return array


if __name__ == "__main__":
    g_list = [41, 6, 95, 11, 4, 65, 74, 4]
    result = insertion_sort(g_list)
    print(result)
