class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        result = -1
        if len(nums) == 1:
            return result
        
        nums.sort()

        L = 0
        R = len(nums) - 1
        while L < R:
            sum_nums = nums[L] + nums[R]
            result = max(sum_nums, result) if sum_nums < k else result
            if sum_nums < k:
                L += 1
            else:
                R -= 1
        return result if result < k else -1
