class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for item in nums:
            if item not in num_set:
                num_set.add(item)
            else:
                return True

        return False
