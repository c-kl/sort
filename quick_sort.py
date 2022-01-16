def partition(array, left_index, right_index):
    """
    快速排序
    :param array: 一个乱序数列
    :param left_index: 左指针
    :param right_index: 右指针
    :return: 左指针的索引
    """
    # 以最右边的一个数为轴，用变量记录轴的索引和值
    pivot_index = right_index
    pivot = array[pivot_index]
    # 除了轴以外，最右边的为右指针
    right_index -= 1
    while True:
        # 左指针指的值如果比轴小，左指针右移
        while left_index >= 0 and array[left_index] < pivot:
            left_index += 1
        # 右指针指的值如果比轴小，右指针左移
        while right_index >= 0 and array[right_index] >= pivot:
            right_index -= 1
        # 左指针和右指针重合，或者右指针在左指针左侧，停止循环
        if left_index >= right_index:
            break
        # 左指针和右指针停下，且左指针在左，右指针在右
        # 此时交换二者的值
        else:
            array[left_index], array[right_index] = array[right_index], array[left_index]
    # 退出循环后，左指针和轴交换值
    array[left_index], array[pivot_index] = array[pivot_index], array[left_index]
    # 返回左指针的索引(此时左指针的索引指向的是轴的值)
    return left_index


def quick_sort(array, left_index, right_index):
    # 基准情形：如果分出的子数组长度为1或者0
    if right_index - left_index <= 0:
        return
    # index为partition中的轴
    index = partition(array, left_index, right_index)
    # 以partition的轴(已换好位置的)为中点
    # 对中点左侧进行排序(小于index的值)
    quick_sort(array, left_index, index - 1)
    # 对中点右侧进行排序(大于index的值)
    quick_sort(array, index + 1, right_index)


if __name__ == "__main__":
    g_list = [4, 2, 9, 6, 8, 3, 5, 7, 1, 150, 12, 34]
    quick_sort(g_list, 0, len(g_list) - 1)
    print(g_list)
