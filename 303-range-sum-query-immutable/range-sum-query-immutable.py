class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0] * len(nums)
        self.total = 0
        for i in range(len(nums)):
            self.total += nums[i]
            self.prefix[i] = self.total
        print(self.prefix)


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        preLeft = self.prefix[left -1] if left > 0 else 0
        perRight = self.prefix[right]
        return (perRight - preLeft)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)