class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            L = i + 1
            R = len(nums) - 1
            first_element = nums[i]
            while L < R:
                sum_nums = first_element + nums[L] + nums[R]
                if sum_nums > 0:
                    R -= 1
                elif sum_nums < 0:
                    L += 1
                else:
                    result.append([first_element, nums[L], nums[R]])
                    L += 1
                    R -= 1

                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1

        return result
