class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hash_map = {"".join(sorted(s1)): 1}
        length_s1 = len(s1)

        for i in range(0, len(s2)):
            # print(s2[i:i+length_s1])
            per = "".join(sorted(s2[i : i + length_s1]))
            if per in hash_map:
                return True

        return False
