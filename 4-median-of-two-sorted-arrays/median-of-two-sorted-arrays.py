class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2  # Number of elements in left partition
        
        left, right = 0, m
        while left <= right:
            # Partition in nums1
            i = (left + right) // 2
            # Partition in nums2 is simply total_left - i
            j = total_left - i
            
            # Boundaries: use infinity as sentinel for edges
            nums1_left_max = float('-inf') if i == 0 else nums1[i - 1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j - 1]
            nums2_right_min = float('inf') if j == n else nums2[j]
            
            # Check if partitions are correct
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # Odd total length: median is max of left partition
                if (m + n) % 2 == 1:
                    return max(nums1_left_max, nums2_left_max)
                # Even total length: median is avg of max left & min right
                return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min)) / 2
            elif nums1_left_max > nums2_right_min:
                # Move partition in nums1 to the left
                right = i - 1
            else:
                # Move partition in nums1 to the right
                left = i + 1
