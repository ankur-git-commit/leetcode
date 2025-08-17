class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            L, R = i+1, len(nums)- 1
            while L < R:
                sum_nums = nums[i] + nums[L] + nums[R]
                if sum_nums > 0:
                    R -= 1
                elif sum_nums < 0:
                    L += 1
                else:
                    result.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while L < R and nums[R] == nums[R-1]:
                        R -= 1
                    L+=1
                    R-=1
        return result