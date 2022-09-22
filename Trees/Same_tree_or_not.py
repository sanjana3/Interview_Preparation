# Q3. Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
**************************************************************************************************************************

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Approach 1: using BFS (iterative method)
#         q1 = collections.deque([(p)])
#         q2 = collections.deque([(q)])

#         while q1 or q2:
#             n1 = q1.popleft()
#             n2 = q2.popleft()
#             if not n1 and not n2:
#                 continue
#             elif not n1 or not n2:
#                 return False
#             else:
#                 if n1.val != n2.val:         return False
#                 q1.append(n1.left)
#                 q1.append(n1.right)
#                 q2.append(n2.left)
#                 q2.append(n2.right)
#         return True

        # Approach 2: using DFS (iterative method)
        stack = [(p,q)]

        while stack:
            n1, n2 = stack.pop()
            if not n1 and not n2:
                continue
            elif not n1 or not n2:
                return False
            else:
                if n1.val != n2.val:         
                    return False
                stack.append((n1.left, n2.left))
                stack.append((n1.right, n2.right))
        return True
    
        # Approach 3: using recursion
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
        
        
        
