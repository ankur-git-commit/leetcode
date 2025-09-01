class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        pair = []
        stack = []
        for i in zip(position, speed):
            pair.append(i)

        pair = sorted(pair)[::-1]

        for p, s in pair:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
