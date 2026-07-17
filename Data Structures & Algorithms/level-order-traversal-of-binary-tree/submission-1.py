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
        q = deque([(root, 0)])
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

        level = []
        while q:
            node, height = q.popleft() 
            if height != prev_level:
                output.append(level[:])
                level.clear()
                prev_level = height
            
            level.append(node.val)
            # Every range is a level, we need t
            if node.left:
                q.append((node.left, height + 1))
            if node.right:
                q.append((node.right, height + 1))
        if level:
            output.append(level)
                
        return output
        