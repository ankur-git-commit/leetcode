class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R = 0, len(height) - 1
        max_water_storage = 0
        while L < R:
            min_height = min(height[L], height[R])
            max_water_storage = max(max_water_storage, min_height * abs(L - R))

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return max_water_storage