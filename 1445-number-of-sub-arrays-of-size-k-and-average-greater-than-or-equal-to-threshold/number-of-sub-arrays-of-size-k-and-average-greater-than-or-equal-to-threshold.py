class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarray = sum(arr[:k-1])
        res = 0

        for i in range(k-1, len(arr)):
            subarray += arr[i]
            if subarray/k >= threshold:
                res += 1
            print(i)
            subarray -= arr[i + 1 -k]
        
        return res
