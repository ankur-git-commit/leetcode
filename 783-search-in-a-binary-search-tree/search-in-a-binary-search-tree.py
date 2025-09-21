# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # iterative
        if not root:
            return None
        
        cur = root
        while cur:
            if cur.val == val:
                return cur
            
            if cur.val > val:
                cur = cur.left
            else:
                cur = cur.right
        
        return None



        # recursive
        # if not root:
        #     return None

        # if root.val < val:
        #     return self.searchBST(root.right, val)
        # elif root.val > val:
        #     return self.searchBST(root.left, val)
        # else:
        #     return root
        
        