class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = sum(arr[:k-1])
        L = 0
        res = 0

        for i in range(k-1, len(arr)):
            curr_sum += arr[i]
            
            if curr_sum/k >= threshold:
                res += 1

            curr_sum -= arr[L]
            L += 1
        
        return res
