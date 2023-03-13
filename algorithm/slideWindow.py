"""
滑动窗口思路（找最长）
1、左右双指针在起点，右指针向右开始循环
2、每次滑动过程中，元素满足条件则移动右指针扩大范围，更新最优结果，
    如果不满足移动左指针缩小范围
滑动窗口思路（找最短）
1、左右双指针在起点，右指针向右开始循环
2、每次滑动过程中，元素满足条件则移动左指针缩小范围，更新最优结果，
    如果不满足移动右指针扩大范围

例子：寻找长度最小的子数组
"""
def minSubArrayLength(target, nums):
    left = 0
    right = 0
    curSum = 0
    min_length = 0
    while right < len(nums):
        curSum = curSum + nums[right]
        while curSum >= target:
            if right - left + 1 < min_length or min_length == 0:
                min_length = right - left + 1
            curSum = curSum - nums[left]
            left += 1
        right += 1
    return min_length