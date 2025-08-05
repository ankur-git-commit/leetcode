class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for item in strs:
            current_item = "".join(sorted(item))

            if current_item not in anagrams:
                anagrams[current_item] = [item]
            else:
                anagrams[current_item].append(item)

        result = []
        for key, value in anagrams.items():
            result.append(value)
        # without list comprehension
        return result

        # list comprehension
        return [value for key, value in anagrams.items()]
