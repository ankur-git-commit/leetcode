class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        L, R = 0, 0
        window = set()
        res = 0
        while R < len(s):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            window.add(s[R])
            res = max(res, len(window))
            R += 1
        
        return res
