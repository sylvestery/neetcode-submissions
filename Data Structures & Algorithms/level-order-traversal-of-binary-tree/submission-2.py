# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        output = []
        # Typical BFS
        #  1 -> (2, 3)
        #  2 -> (3, 4, 5)
        #  3 -> (4, 5, 6, 7)
        #  If we want to print for a level
        # 1 -> []
        # 2, 3 
        # 4, 5, 6, 7
        prev_level = 0

        while q:
            level = []
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if level:
                output.append(level)
                
        return output
        