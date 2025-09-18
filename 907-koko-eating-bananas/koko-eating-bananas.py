class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L, R = 1, max(piles)
        min_speed = 0
        while L <= R:
            k = (L+R)// 2
            
            total = 0
            for pile in piles:
                total += math.ceil(pile / k)
                if total > h:
                    break
            if total <= h:
                min_speed = k
                R = k - 1
            else:
                L = k + 1
        return min_speed