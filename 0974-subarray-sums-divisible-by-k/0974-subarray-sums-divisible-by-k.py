class Solution:
    def subarraysDivByK(self, nums, k):
        prefix = 0
        count = 0
        mp = {0: 1}

        for num in nums:
            prefix += num
            rem = prefix % k

            count += mp.get(rem, 0)
            mp[rem] = mp.get(rem, 0) + 1

        return count