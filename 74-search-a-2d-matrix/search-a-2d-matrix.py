class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1
        n = len(matrix[0]) - 1
        while L<=R:
            arr = (L + R) // 2
            if target < matrix[arr][0]:
                R = arr - 1
            elif target > matrix[arr][n]:
                L = arr + 1
            else:
                target_array = matrix[arr]
                low, high = 0, n
                while low<=high:
                    mid = (low + high) // 2
                    if target < target_array[mid]:
                        high = mid - 1
                    elif target > target_array[mid]:
                        low = mid + 1
                    else:
                        return True
                
                return False
        
        return False
                    
        
        
        
        # O(m * logn) - can do better: O(log(m * n))

        # for nums in matrix:
        #     L, R = 0, len(nums) - 1
        #     while L<=R:
        #         mid = (L + R) // 2

        #         if target > nums[mid]:
        #             L = mid + 1
        #         elif target < nums[mid]:
        #             R = mid - 1
        #         else:
        #             return True
        
        # return False