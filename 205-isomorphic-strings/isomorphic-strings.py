class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # cleaner version
        s2t, t2s = {}, {}
        for a, b in zip(s, t):
            if s2t.get(a, b) != b or t2s.get(b,a) != a:
                return False
            s2t[a] = b
            t2s[b] = a
        return True
        
        
        
        # Working solution, optimal
        # s_to_t = {}
        # t_to_s = {}
        
        # for i in range(len(s)):
        #     if s[i] not in s_to_t and t[i] not in t_to_s:
        #         s_to_t[s[i]] = t[i]
        #         t_to_s[t[i]] = s[i]
        #     elif s[i] in s_to_t and t[i] in t_to_s:
        #         if s_to_t[s[i]] != t[i] or t_to_s[t[i]] != s[i]:
        #             return False
        #     else:
        #         return False
        
        # return True