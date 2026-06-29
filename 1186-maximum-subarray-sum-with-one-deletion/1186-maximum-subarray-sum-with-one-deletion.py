class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        forward = [0] * n
        forward[0] = arr[0]

        for i in range(1, n):
            forward[i] = max(arr[i], forward[i - 1] + arr[i])
        backward = [0] * n
        backward[n - 1] = arr[n - 1]

        for i in range(n - 2, -1, -1):
            backward[i] = max(arr[i], backward[i + 1] + arr[i])

        ans = max(forward)
        for i in range(1, n - 1):
            ans = max(ans, forward[i - 1] + backward[i + 1])

        return ans
        