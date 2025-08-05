class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in num_hashmap:
                return [i, num_hashmap[complement]]

            num_hashmap[nums[i]] = i
