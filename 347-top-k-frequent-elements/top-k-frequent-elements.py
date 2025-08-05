class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # with counter dictionary and list comprehension
        # elements_freq = Counter(nums)
        # sort_by_values = sorted(elements_freq.items(), key=lambda item: item[1], reverse=True)
        # return [sort_by_values[i][0] for i in range(k)]

        # without counter dictionary and list comprehension
        ele_freq = {}
        for i in range(len(nums)):
            ele_freq[nums[i]] = 1 + ele_freq.get(nums[i], 0)

        sort_by_value = sorted(ele_freq.items(), key=lambda item: item[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sort_by_value[i][0])

        return result
