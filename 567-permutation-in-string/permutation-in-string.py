class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        m = len(s1)
        for start in range(0, len(s2) - m + 1):     # include last window
            window = need.copy()                    # make a fresh copy
            ok = True
            for i in range(start, start + m):
                c = s2[i]
                if window[c] == 0:                  # not needed / overused
                    ok = False
                    break
                window[c] -= 1
            if ok:                                  # all counts consumed
                return True
        return False


        
        
        
        # Brute Force
        # Works but takes too much time O(n) Solution
        sorted_s1 = sorted(s1)
        length_s1 = len(s1)

        for i in range(0, len(s2)):
            if i + length_s1 > len(s2):
                break
            per = (sorted(s2[i : i + length_s1]))
            # print(per)
            # if per in hash_map:
            if per == sorted_s1:
                return True

        return False