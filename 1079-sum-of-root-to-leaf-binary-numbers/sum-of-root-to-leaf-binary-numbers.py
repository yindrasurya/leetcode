# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, r: Optional[TreeNode]) -> int:
        return (f:=lambda n,q=0:n and (f(n.left,q:=q*2+n.val)+f(n.right,q) or q) or 0)(r)  