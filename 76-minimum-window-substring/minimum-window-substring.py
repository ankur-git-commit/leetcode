class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

    
        countT = Counter(t)
        window = {}
        have, need = 0, len(countT)
        L = 0
        resLen = float("inf")
        res = [-1, -1]

        for R in range(len(s)):
            window[s[R]] = 1 + window.get(s[R], 0)

            if s[R] in countT and window[s[R]] == countT[s[R]]:
                have += 1

            while have == need:
                if (R - L + 1) < resLen:
                    res = [L, R]
                    resLen = R - L + 1

                window[s[L]] -= 1
                if s[L] in countT and window[s[L]] < countT[s[L]]:
                    have -= 1
                L += 1
        L, R = res
        return s[L : R + 1] if resLen != float("inf") else ""
