class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = 0
        freq_count = set(nums)

        for i in freq_count:
            # count = 0
            if i-1 not in freq_count:
                # current_element = i
                count = 1 
                while i + count in freq_count:
                    count += 1
                    # current_element += 1
                res = max(res, count)
        
        return res