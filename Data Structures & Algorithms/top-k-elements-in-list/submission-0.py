from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        sorted_tuples = sorted(count.items(), key=lambda x: x[1], reverse = True)

        top_k_frequent_elements = []

        for i in range(0, k):
            top_k_frequent_elements.append(sorted_tuples[i][0])

        return top_k_frequent_elements
        