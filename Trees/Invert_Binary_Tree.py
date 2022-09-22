# Q1. Given the root of a binary tree, invert the tree, and return its root. left node becomes right vice versa
**************************************************************************************************************************

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Way 1 : swap left nodes to right vice versa (O(n)) using recursion
        if not root:
            return
        
        temp1 = root.left
        temp2 = root.right
        
        root.left = temp2
        root.right = temp1
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
        # # Way 2: using BFS  (O(n))
        # queue = collections.deque([(root)])
        # while len(queue) > 0:
        #     node = queue.popleft()
        #     if node:
        #         node.left, node.right = node.right, node.left
        #         queue.append(node.left)
        #         queue.append(node.right)
        # return root
        
        # Way 3: DFS using stacks O(n)
#         stack = [root]
#         while stack:
#             node = stack.pop()
#             if node:
#                 node.left, node.right = node.right, node.left
#                 # stack.extend([node.left, node.right])
#                 stack.append(node.left)
#                 stack.append(node.right)
#         return root
                
        
