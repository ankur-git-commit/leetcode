class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        max_size = 0
        L, R = 0, 0

        while R < len(s):
            while s[R] in window:
                window.remove(s[L])
                L += 1
            # print("current element:", s[R], " window: ", window)
            window.add(s[R])
            max_size = max(max_size, len(window))
            R += 1

        return max_size
