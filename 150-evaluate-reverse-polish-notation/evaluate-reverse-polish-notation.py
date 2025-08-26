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
                second_element = nums.pop()
                first_element = nums.pop()
                res = hash_map[i](first_element, second_element)
                nums.append(res) 
            else:
                nums.append(int(i))

        return nums[0]