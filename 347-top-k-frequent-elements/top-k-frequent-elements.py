class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Solution 1
        # with counter dictionary and list comprehension
        elements_freq = Counter(nums)
        sort_by_values = sorted(elements_freq.items(), key=lambda item: item[1], reverse=True)
        return [sort_by_values[i][0] for i in range(k)]

        # Solution 2
        # without counter dictionary and list comprehension
        ele_freq = {}
        for i in range(len(nums)):
            ele_freq[nums[i]] = 1 + ele_freq.get(nums[i], 0)

        sort_by_value = sorted(ele_freq.items(), key=lambda item: item[1], reverse=True)

        result = []
        for i in range(k):
            result.append(sort_by_value[i][0])

        return result

        # Solution 3
        ele_freq = {}
        for i in range(len(nums)):
            ele_freq[nums[i]] = 1 + ele_freq.get(nums[i], 0)
        arr = []
        for element, count in ele_freq.items():
            arr.append([count, element])
        arr.sort()  # can also do arr.sort(reverse=True)
        print(arr)
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
