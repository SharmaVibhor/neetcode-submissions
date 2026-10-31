class Solution:
    def mySqrt(self, x: int) -> int:
        right = x
        left = 0

        while left < right:
            mid = (left + right + 1)//2

            if mid*mid <= x:
                left = mid
            else:
                right = mid - 1
        
        return left
        