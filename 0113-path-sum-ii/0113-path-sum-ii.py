class Solution:
    def pathSum(self, root, targetSum):
        if not root:
            return []

        result = []

        def dfs(node, remaining, path):
            if not node:
                return
            path.append(node.val)

            if not node.left and not node.right:
                if remaining == node.val:
                    result.append(path[:])
            else:
                new_remaining = remaining - node.val

                dfs(node.left, new_remaining, path)
                dfs(node.right, new_remaining, path)

            
            path.pop()

        dfs(root, targetSum, [])
        return result
        