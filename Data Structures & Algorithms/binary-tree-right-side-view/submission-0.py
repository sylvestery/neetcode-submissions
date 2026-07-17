# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # basicaly the rightmost node.
        # 1 -> yes
        # 2 n 3 y
        # 4 null null null 
        # you can discard 
        q = deque([root])
        result =[]
        while q:
            n = len(q)
            for i in range(n):
                # We need to find the right most right here.
                node = q.popleft()
                if i == n-1:
                    result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return result





        