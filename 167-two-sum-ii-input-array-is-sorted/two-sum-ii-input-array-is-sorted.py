class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            sum_numbers = numbers[L] + numbers[R]
            if sum_numbers == target:
                return [L + 1, R + 1]
            elif sum_numbers > target:
                R -= 1
            else: 
                L += 1