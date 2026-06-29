class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum+nums[i])
            max_sum = max(max_sum, current_sum)
        current_min = nums[0]
        min_sum = nums[0]
        for i in range(1, len(nums)):
            current_min = min(nums[i], current_min+nums[i])
            min_sum = min(min_sum, current_min)
        if max_sum < 0:
            return max_sum
        return max(max_sum, total-min_sum)            
        