# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root, k):
        s1 = []
        s2 = []

        left = root
        right = root

        while left:
            s1.append(left)
            left = left.left

        while right:
            s2.append(right)
            right = right.right

        while s1 and s2:
            low = s1[-1]
            high = s2[-1]

            if low == high:
                break

            total = low.val + high.val

            if total == k:
                return True

            elif total < k:
                node = s1.pop()
                node = node.right

                while node:
                    s1.append(node)
                    node = node.left

            else:
                node = s2.pop()
                node = node.left

                while node:
                    s2.append(node)
                    node = node.right

        return False
        