class Solution:
    def subarraySum(self, nums, k):
        count = 0
        prefix_sum = 0
        mp = {0: 1}

        for num in nums:
            prefix_sum += num
            count += mp.get(prefix_sum - k, 0)
            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1

        return count
        