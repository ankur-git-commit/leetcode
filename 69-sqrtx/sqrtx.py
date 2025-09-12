class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        L = 2
        R = x // 2

        while L<=R:
            mid = (L+R)//2
            square_root = mid * mid

            if square_root > x:
                R = mid - 1
            elif square_root < x:
                L = mid + 1
            else:
                return mid

        return R