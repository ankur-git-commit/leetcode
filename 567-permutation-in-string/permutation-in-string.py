class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Works but takes too much time O(n) Solution
        # hash_map = {"".join(sorted(s1)): 1}
        sorted_s1 = "".join(sorted(s1))
        length_s1 = len(s1)

        for i in range(0, len(s2)):
            if i + length_s1 > len(s2):
                break
            per = "".join(sorted(s2[i : i + length_s1]))
            # if per in hash_map:
            if per == sorted_s1:
                return True

        return False
