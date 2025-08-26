class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        hash_map = {")": "(", "}": "{", "]": "["}

        stack = []
        for item in s:
            if item in hash_map:
                if stack and stack[-1] == hash_map[item]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(item)

        return len(stack) == 0
