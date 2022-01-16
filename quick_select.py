from quick_sort import partition


def quick_select(array, kth, left_index, right_index):
    """
    快速选择
    :param array: 一个乱序数列
    :param kth: 所求的第k小的值
    :param left_index: 左指针
    :param right_index: 右指针
    :return: 当前第k小的值
    """
    # 基准情形：当分出的子数组长度为1或者0
    if left_index >= right_index:
        # 返回左指针的值
        return array[left_index]
    # 用index记录partition中的轴的索引，以此为中点
    index = partition(array, left_index, right_index)
    # 如果中点在k的右侧
    if index > kth:
        # 在中点左侧继续
        return quick_select(array, kth, left_index, index - 1)
    # 如果中点在k的左侧
    elif index < kth:
        # 在中点右侧继续
        return quick_select(array, kth, index + 1, right_index)
    # 如果中点和k重合
    else:
        # 返回中点的值，即为k值
        return array[index]


if __name__ == "__main__":
    g_list = [7, 5, 6, 9, 31, 20, 140, 320, 1, 0, 3]
    result = quick_select(g_list, 2, 0, len(g_list) - 1)
    print(result)
