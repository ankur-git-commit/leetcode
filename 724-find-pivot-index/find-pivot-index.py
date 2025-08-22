class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # most optimal
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum = total - nums[i] - left_sum
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


        # not optimal 
        prefix = []
        output = 0
        for i in range(len(nums)):
            output += nums[i]
            prefix.append(output)

        for i in range(len(nums)):
            left = prefix[i - 1] if i != 0 else 0
            right = prefix[-1] - prefix[i]

            if left == right:
                return i
        return -1


        # below is not the optimal way to do it, it works though
        if len(nums) <= 1:
            return 0

        n = len(nums)
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        pre, post = 0, 0
        for i in range(n):
            pre += nums[i]
            prefix[i] = pre

            j = n - i - 1
            post += nums[j]
            postfix[j] = post
        
        # if postfix[1] == 0:
        #     return 0
        # elif prefix[n-1] == 0:
        #     return n-1

        for i in range(n):
            if i == 0 and 0 == postfix[i + 1]:
                return i
            elif i == n - 1 and prefix[i - 1] == 0:
                return i 
            elif 1 <= i < n - 1 and prefix[i - 1] == postfix[i + 1]:
                return i


            # left = i - 1 if i != 0 else 0
            # right = i + 1 if i < n - 1 else 0
            # print(left, right)
            # if prefix[left] == postfix[right]:
            #     return i

        return -1