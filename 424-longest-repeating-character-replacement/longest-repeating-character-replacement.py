class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = {}
        result = 0
        L, R = 0, 0

        while R < len(s):
            hash_map[s[R]] = 1 + hash_map.get(s[R], 0)

            while (R - L + 1) - max(hash_map.values()) > k:
                hash_map[s[L]] -= 1
                L += 1
            result = max(R - L + 1, result)
            R += 1

        return result
