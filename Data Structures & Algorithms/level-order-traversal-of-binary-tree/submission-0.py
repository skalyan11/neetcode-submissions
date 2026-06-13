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
        r = defaultdict(list)
        while q:
            node, depth = q.popleft()
            r[depth].append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            
            if node.right:
                q.append((node.right, depth + 1))
        return [r[i] for i in range(len(r))]