# import random
class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []        
        s = 0
        for weight in w:
            s += weight
            self.prefix_sum.append(s)
        self.total = s
        
    def pickIndex(self) -> int:
        r = random.randint(1, self.total)
        for i,p in enumerate(self.prefix_sum):
            if r <=p:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()