# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []

        def dfs(
            node: Optional[TreeNode], remaining_sum: int, path: list[int]
        ):
            if not node:
                return

            path.append(node.val)
            remaining_sum -= node.val

            if not node.left and not node.right and remaining_sum == 0:
                result.append(path[:])

            dfs(node.left, remaining_sum, path)
            dfs(node.right, remaining_sum, path)

            path.pop()

        dfs(root, targetSum, [])
        return result