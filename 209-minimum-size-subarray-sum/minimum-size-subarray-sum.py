class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0, 0
        sizeMin = float('inf')
        curr_sum = 0
        while R < len(nums):
            curr_sum += nums[R]
            while curr_sum >= target:
                sizeMin = min(sizeMin, R - L + 1)
                curr_sum -= nums[L]
                L += 1
            R += 1
        
        return 0 if sizeMin == float('inf') else sizeMin
