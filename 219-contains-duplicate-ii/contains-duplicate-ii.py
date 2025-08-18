class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_set = {}

        for i in range(len(nums)):
            if nums[i] in hash_set and abs(hash_set[nums[i]] - i) <=k:
                return True
            hash_set[nums[i]] = i
        return False