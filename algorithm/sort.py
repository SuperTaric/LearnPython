import time
def cost_time(func):
    def fun(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        print(f'func {func.__name__} cost time:{time.perf_counter() - t:.8f} s')
        return result
    return fun

"""
冒泡排序
"""
@cost_time
def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

"""
选择排序
"""
@cost_time
def selectSort(nums):
    n = len(nums)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]

"""
插入排序
"""
@cost_time
def insertSort(nums):
    n = len(nums)
    for i in range(1, n):
        j = i - 1
        cur = nums[i]
        while j >= 0 and cur < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = cur

"""
快速排序
"""
@cost_time
def sort(nums):
    quickSort(0, len(nums) - 1, nums)

def quickSort(start, end, arr):
    if start < end:
        mid = partition(start, end, arr)
        quickSort(start, mid - 1, arr)
        quickSort(mid + 1, end, arr)
    return arr

def partition(start, end, arr):
    base = arr[start]
    left = start
    right = end
    while left is not right:
        while arr[right] >= base and right > left:
            right -= 1
        arr[left] = arr[right]
        while arr[left] <= base and right > left:
            left += 1
        arr[right] = arr[left]
    arr[left] = base
    return left

if __name__ == '__main__':
    nums = [100, 30, 20, 82, 78, 48, 70]
    bubbleSort(nums)
    print(nums)
    nums = [100, 30, 20, 82, 78, 48, 70]
    selectSort(nums)
    print(nums)
    nums = [100, 30, 20, 82, 78, 48, 70]
    selectSort(nums)
    print(nums)
    nums = [100, 30, 20, 82, 78, 48, 70]
    sort(nums)
    print(nums)