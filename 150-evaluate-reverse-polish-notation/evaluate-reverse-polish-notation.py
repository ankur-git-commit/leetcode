class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        hash_map= {
            '+': operator.add,
            '-': operator.sub, 
            '*': operator.mul, 
            '/': lambda x, y: int(x / y),
        }
        res = 0

        for i in tokens:
            if i in hash_map:
                b = nums.pop()
                a = nums.pop()
                res = hash_map[i](a, b)
                nums.append(res) 
            else:
                nums.append(int(i))

        return nums[0]