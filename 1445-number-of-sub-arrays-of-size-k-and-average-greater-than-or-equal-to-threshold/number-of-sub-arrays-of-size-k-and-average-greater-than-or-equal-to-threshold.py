class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarray = sum(arr[:k-1])
        L = 0
        res = 0

        for i in range(k-1, len(arr)):
            subarray += arr[i]
            if subarray/k >= threshold:
                res += 1
            # subarray -= arr[i + 1 -k]
            subarray -= arr[L]
            L += 1
        
        return res
