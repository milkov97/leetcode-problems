# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(root_left, root_right):
            if root_left is None and root_right is None:
                return True
            elif root_left is None or root_right is None:
                return False
            else:
                return root_left.val == root_right.val and isMirror(root_left.left, root_right.right) and isMirror(root_left.right, root_right.left)
        if root is None: 
            return "true"
        
        return isMirror(root.left, root.right)