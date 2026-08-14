class Solution:
    def maxDistance(self, position, m):
        position.sort()

        low = 1
        high = position[-1] - position[0]
        answer = 0

        while low <= high:
            mid = (low + high) // 2

            balls = 1
            last_position = position[0]

            for i in range(1, len(position)):
                if position[i] - last_position >= mid:
                    balls += 1
                    last_position = position[i]

            if balls >= m:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1

        return answer
        