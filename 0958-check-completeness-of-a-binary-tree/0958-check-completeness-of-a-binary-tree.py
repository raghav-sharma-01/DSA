from collections import deque

class Solution:
    def isCompleteTree(self, root):
        if not root:
            return True

        queue = deque([root])
        null_found = False

        while queue:
            node = queue.popleft()

            if node is None:
                null_found = True
            else:
                if null_found:
                    return False

                queue.append(node.left)
                queue.append(node.right)

        return True
        