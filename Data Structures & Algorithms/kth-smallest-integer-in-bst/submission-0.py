# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        min = left most, 
        in order traversal will preserve sorted order in a bst
        """
        if not root:
            return 0
        s = []
        curr = root
        n = 0
        while curr or s:
            #keep going left till you cant
           while curr:
                s.append(curr)
                curr = curr.left
            
           curr = s.pop()
           n += 1
           if n == k:
               return curr.val
           curr = curr.right




        