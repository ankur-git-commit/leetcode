class Solution:
    def trap(self, height: List[int]) -> int:
        # initial thought - don't know how to start the algorithm or even loop through it
        # obviously the answer lies between the walls, if the height is 0 or lower value compared to the height of the enclosing walls then that is the amount of water that is stored.
        # formula =  min(L, R) - height[i] 

        # solution 1
        # Time complexity: O(n)
        # Space complexity: O(n) - creating 2 extra arrays to store the max_left and max_right height for each element
        L, R = 0, len(height) - 1
        n = len(height)
        left_array, right_array = [0] * n, [0] * n
        max_left_val, max_right_val = 0, 0

        for i in range(1, n):
            max_left_val = max(max_left_val, height[i - 1])
            left_array[i] = (max_left_val)
        
        for i in range(n-2, -1, -1):
            max_right_val = max(max_right_val, height[i + 1])
            right_array[i] = (max_right_val)
        

        res = 0
        print(left_array, right_array)

        for i in range(len(height)):
            curr_val = min(left_array[i], right_array[i]) - height[i] 
            res += curr_val if curr_val > 0 else 0
        
        return res
