class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # with counter dictionary and list comprehension
        elements_freq = Counter(nums)
        sort_by_values = sorted(elements_freq.items(), key=lambda item: item[1], reverse=True)
        return [sort_by_values[i][0] for i in range(k)]