#! python3
# -*- coding:utf-8 -*-


def bubble_sort(nums):
    """
    冒泡排序,两两比较比较到最后，重复len-1次
    比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
    :param nums:
    :return:
    """
    for i in range(len(nums)-1):
        for j in range(len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def selection_sort(nums):
    """
    选则排序，选中第一个数，后面的数一次与之比较，然后选择第二个数
    首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
    然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。 选择排序的思想其实和冒泡排序有点类似，
    都是在一次排序后把最小的元素放到最前面。但是过程不同， 冒泡排序是通过相邻的比较和交换。而选择排序是通过对整体的选择。
    :return:
    """
    for i in range(len(nums)-1):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


def insert_sort(nums):
    """
    插入排序（英语：Insertion Sort）是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，
    在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，通常采用in-place排序 （即只需用到O(1)的额外空间的排序），
    因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位， 为最新元素提供插入空间。
    1.从第一个元素开始，该元素可以认为已经被排序
    2.取出下一个元素，在已经排序的元素序列中从后向前扫描
    3.如果该元素（已排序）大于新元素，将该元素移到下一位置
    4.将新元素插入到该位置后
    :param nums:
    :return:
    """
    n = len(nums)
    for i in range(0, n):
        for j in range(i, 0, -1):
            if nums[j] < nums[j - 1]:
                nums[j], nums[j - 1] = nums[j - 1], nums[j]
            else:
                break
    return nums


def quick_sort(nums, start, end):
    """
    快速排序
    :param nums:
    :return:
    """
    # 判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = nums[i]
        while i < j:
            # 如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (nums[j] >= base):
                j = j - 1
            # 如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            nums[i] = nums[j]
            # 同样的方式比较前半区
            while (i < j) and (nums[i] <= base):
                i = i + 1
            nums[j] = nums[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        nums[i] = base
        # 递归前后半区
        quick_sort(nums, start, i - 1)
        quick_sort(nums, j + 1, end)
    return nums


if __name__ == '__main__':
    nums = [22, 34, 3, 32, 82, 55, 89, 50, 37, 5, 64, 35, 9, 70]
    print(quick_sort(nums, 0, len(nums)-1))
