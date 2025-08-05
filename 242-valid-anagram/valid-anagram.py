class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hashmap = {}
        t_hashmap = {}

        for i in range(len(s)):
            s_hashmap[s[i]] = 1 + s_hashmap.get(s[i], 0)
            t_hashmap[t[i]] = 1 + t_hashmap.get(t[i], 0)

        for item in s_hashmap:
            if item not in t_hashmap or s_hashmap[item] != t_hashmap[item]:
                return False

        return True
