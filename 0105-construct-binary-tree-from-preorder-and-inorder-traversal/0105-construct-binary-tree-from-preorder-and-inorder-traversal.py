# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        pre_idx = 0

        def arrayToTree(left: int,right: int) -> Optional[TreeNode]:
            nonlocal pre_idx

            if left > right:
                return None

            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            inorder_idx = inorder_map[root_val]

            root.left = arrayToTree(left, inorder_idx - 1)
            root.right = arrayToTree(inorder_idx + 1,right)

            return root

        return arrayToTree(0, len(inorder) - 1)