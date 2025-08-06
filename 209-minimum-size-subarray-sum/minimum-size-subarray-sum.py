class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = math.inf
        total = 0
        L = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                result = min((R - L + 1), result)
                total -= nums[L]
                L += 1

        return 0 if result == math.inf else result
