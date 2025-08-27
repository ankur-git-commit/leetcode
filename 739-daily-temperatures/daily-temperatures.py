class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        res = [0] * n
        L = 0
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # print(temperatures[R])
                j = stack.pop()       # index of a cooler day
                res[j] = i - j  
            stack.append(i)
        
        return res
            