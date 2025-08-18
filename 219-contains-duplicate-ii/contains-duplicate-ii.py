class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # using hash set
        window = set()
        L = 0
        for R in range(len(nums)):
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False
        
        
        # using hash map
        hash_set = {}

        for i in range(len(nums)):
            if nums[i] in hash_set and abs(hash_set[nums[i]] - i) <=k:
                return True
            hash_set[nums[i]] = i
        return False