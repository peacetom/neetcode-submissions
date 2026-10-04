class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        current_max = -1
        for i in range(n-1, -1, -1):
            current_val = arr[i]
            arr[i] = current_max
            current_max = max(current_val, current_max)
        return arr