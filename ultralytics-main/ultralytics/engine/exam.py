def find_closest_index(A, T):
    """
    在升序数组 A 中找到最接近目标整数 T 的元素的索引。
    如果存在相同距离，优先选择较小的数。
    :param A: 升序排列的数组
    :param T: 目标整数
    :return: 最接近 T 的数的索引
    """
    left, right = 0, len(A) - 1

    # 二分查找找到最接近的位置
    while left < right:
        mid = (left + right) // 2
        if A[mid] < T:
            left = mid + 1
        else:
            right = mid

    # 此时 left 和 right 应该相等，表示最接近 T 的候选位置
    # 现在要比较 A[left] 和 A[left-1] 看哪个更接近 T
    if left == 0:  # 如果 left 是第一个元素，直接返回它
        return left
    if abs(A[left] - T) < abs(A[left - 1] - T):  # 如果 A[left] 更接近 T
        return left
    elif abs(A[left] - T) == abs(A[left - 1] - T):  # 如果距离相等，返回较小的数
        return left - 1
    else:  # 否则返回 A[left-1]
        return left - 1


if __name__ == '__main__':
    A = [1, 3, 7, 9]
    T = 6
    print(find_closest_index(A, T))