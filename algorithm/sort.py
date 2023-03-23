"""
冒泡排序
"""
def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

if __name__ == '__main__':
    nums = [100, 30, 20, 82, 78, 48, 70]
    bubbleSort(nums)
    print(nums)