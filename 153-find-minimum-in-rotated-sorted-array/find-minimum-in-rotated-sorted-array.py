class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L+R) // 2

            if nums[mid] >= nums[L]:
                if nums[mid] > nums[R]:
                    L = mid + 1
                else:
                    R = mid - 1
            elif nums[mid] >= nums[R]:
                if nums[mid] > nums[L]:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                R = mid
        
        return nums[L]
        