class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        current_max = nums[0]
        max_sum = nums[0]
        current_min = nums[0]
        min_sum = nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], current_max+nums[i])
            max_sum = max(max_sum, current_max)
            current_min = min(nums[i], current_min+nums[i])
            min_sum = min(min_sum, current_min)
        return max(max_sum, abs(min_sum))    

        