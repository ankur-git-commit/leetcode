class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        result = 0
        L, R = 0, 0

        while R < len(s):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            result = max((R - L + 1), result)
            window.add(s[R])
            R += 1
        return result
