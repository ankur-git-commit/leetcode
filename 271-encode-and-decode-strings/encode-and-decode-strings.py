class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        output = ""
        for item in strs:
            output += str(len(item)) + "#" + item

        return output

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        
        res, i = [], 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = length + i
            res.append(s[i:j])
            i = j

        return res
        # return s


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
