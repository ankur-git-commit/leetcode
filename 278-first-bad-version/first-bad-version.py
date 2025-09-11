# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        L, R = 0, n
        first_bad_version = 0
        while L <= R:
            mid = (L + R) // 2
            
            if isBadVersion(mid):
                first_bad_version = mid
                R = mid - 1
            else:
                L = mid + 1
        return first_bad_version