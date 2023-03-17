"""
50.Pow(x, n)
"""

def myPow(x: float, n: int) -> float:
    if x == 0.0: return 0.0
    res = 1
    if n < 0: x, n = 1 / x, -n
    while n:
        if n & 1: res *= x
        x *= x
        n >>= 1
    return res

"""
69. x的平方根
"""

def mySqrt(x: int) -> int:
    if x == 0: return 0
    if x == 1: return 1
    left, right, res = 0, x // 2, -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    return res

"""
704.二分查找
"""

def search(nums: list[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while (l <= r):
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif target <= nums[mid]:
                r = mid - 1
            else: l = mid + 1
        return -1