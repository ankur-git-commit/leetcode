class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        
        if len(pattern) != len(s_list):
            return False

        pattern_map = {}
        s_map = {}
        for char,word in zip(pattern, s_list):
            if pattern_map.get(char, word) != word or s_map.get(word, char) != char:
                return False
            pattern_map[char] = word
            s_map[word] = char
        
        return True
