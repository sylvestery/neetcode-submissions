# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# If last node was good, then I am good if > last node
# curr.val > max(ancestors.val)

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxAncestors):
            if not node:
                return 0
            amIGood = node.val >= maxAncestors
            print(amIGood,  node.val, maxAncestors)

            nextMax = max(node.val, maxAncestors)

            return dfs(node.left, nextMax) + dfs(node.right, nextMax) + (1 if amIGood else 0)
    
        return dfs(root, root.val)
        