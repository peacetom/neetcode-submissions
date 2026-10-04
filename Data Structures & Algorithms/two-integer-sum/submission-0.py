class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen_numbers = {}

        for i in range(len(nums)):

            complement = target - nums[i]
            if complement in seen_numbers:
                return [seen_numbers[complement],i]

            seen_numbers[nums[i]] = i