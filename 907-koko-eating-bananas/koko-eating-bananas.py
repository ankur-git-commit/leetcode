class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # n = number of piles of bananas
        # i-th pile which is the index has piles[i] number of bananas
        # h = hours
        # k = speed of eating banaas per hour

        
        L, R = 1, max(piles)

        while L<=R:
            k = (L + R) // 2 
            total_time = 0
            
            for p in piles:
                total_time += math.ceil(p / k)
            if total_time <= h:
                res = k
                R =  k - 1
            else:
                L = k + 1

        return res


        # brute force solution
        # k = 1
        # while True:
        #     total_time = 0
        #     for pile in piles:
        #         total_time += math.ceil(pile / k)
        #         if total_time > h:
        #             break

        #     if total_time <= h:
        #         return k
        #     k += 1
