class Solution:
    def hasPathSum(self, root, targetSum):
        def fun(root, sum):
            if root is None:
                return False

            sum = sum + root.val

            if root.left is None and root.right is None:
                return sum == targetSum

            return (fun(root.left, sum) or
                    fun(root.right, sum))

        return fun(root, 0)
        