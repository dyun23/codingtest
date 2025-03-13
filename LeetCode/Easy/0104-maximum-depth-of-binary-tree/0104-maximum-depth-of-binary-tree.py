# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# postorder 사용
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

# level order 방식
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if root is None: return 0
#         q = deque()
#         depth = 0
#         q.append((root,1))

#         while q:
#             cur_node, cur_depth = q.popleft()
#             depth = cur_depth
#             if cur_node.left:
#                 q.append((cur_node.left, cur_depth + 1))
#             if cur_node.right:
#                 q.append((cur_node.right, cur_depth + 1))
                
#         return depth