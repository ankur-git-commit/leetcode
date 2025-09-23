class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # clean solution
        s_list = s.split(" ")
        output = []
        if len(pattern) != len(s_list):
            return False

        pattern_map = {}
        s_map = {}
        for char,word in zip(pattern, s_list):
            # if pattern_map.get(char, word) != word or s_map.get(word, char) != char:
                # return False

            if pattern_map.get(char, word) != word or s_map.get(word, char) != char:
                print("no word pattern")
                return False
            pattern_map[char] = word
            s_map[word] = char


        
        print(s)
        return True
