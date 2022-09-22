# Q2. Given the root of a binary tree, return its maximum depth.
**************************************************************************************************************************
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Way 1: Using recursion
#         if not root:
#             return 0
        
#         depth = 1
#         depth += max(self.maxDepth(root.left), self.maxDepth(root.right))        
        
#         return depth

        # way 2: using BFS(Queue)
        queue = collections.deque([])
        if root is not None:
            queue.append((1,root))
        depth = 0
        
        while queue:
            c_depth, root = queue.popleft()
            if root:
                depth = max(c_depth, depth)
                queue.append((c_depth+1, root.left))
                queue.append((c_depth+1, root.right))
        return depth
        
        
        # way 3: using DFS(stacks)
#         stack = []
#         if root is not None:
#             stack.append((1, root))
        
#         depth = 0
#         while stack != []:
#             current_depth, root = stack.pop()
#             if root is not None:
#                 depth = max(depth, current_depth)
#                 stack.append((current_depth + 1, root.left))
#                 stack.append((current_depth + 1, root.right))
        
#         return depth
        
        
