class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        L, R = 0, len(height) - 1

        while L < R:
            max_height_storage = min(height[L], height[R])
            water_stored = max_height_storage * (R - L)

            result = max(result, water_stored)

            if height[R] > height[L]:
                L += 1
            else:
                R -= 1

        return result
