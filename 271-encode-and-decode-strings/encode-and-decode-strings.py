class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        output = ""
        for element in strs:
            output += str(len(element)) + "#" + element

        return output

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        i = 0
        result = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j + 1
            end = start + length
            result.append(s[start:end])
            i = end
            print(start, end)

        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
