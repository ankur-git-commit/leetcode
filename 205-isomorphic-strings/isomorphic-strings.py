class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}

        for i,j in zip(s, t):
            if s2t.get(i, j) != j or t2s.get(j, i) != i:
                return False
            s2t[i] = j
            t2s[j] = i
        
        return True