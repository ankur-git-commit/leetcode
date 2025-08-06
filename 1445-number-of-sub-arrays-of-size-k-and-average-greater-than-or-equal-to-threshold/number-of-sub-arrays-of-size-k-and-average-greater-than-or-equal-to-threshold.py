class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_arr = sum(arr[: k - 1])
        L = 0
        result = 0
        for R in range(k - 1, len(arr)):
            sum_arr += arr[R]
            average = sum_arr / k
            if average >= threshold:
                result += 1
            sum_arr -= arr[L]
            L += 1
        return result
