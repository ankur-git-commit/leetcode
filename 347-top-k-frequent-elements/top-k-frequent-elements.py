class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # with counter dictionary
        elements_freq = Counter(nums)
        # print(elements_freq)

        sort_by_values = sorted(elements_freq.items(), key=lambda item: item[1], reverse=True)
        print(sort_by_values)
        result = []
        for i in range(k):
            result.append(sort_by_values[i][0])

        return result