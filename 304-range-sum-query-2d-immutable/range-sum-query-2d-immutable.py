class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        for row in matrix:
            total = 0
            curr_list = []
            for col in row:
                total += col
                curr_list.append(total)
            self.prefix.append(curr_list)
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        right, left = 0, 0
        for i in range(row2 - row1 + 1):
            right += self.prefix[row1 + i][col2]
            left += self.prefix[row1 + i][col1 - 1] if col1 > 0 else 0
        return right - left
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)