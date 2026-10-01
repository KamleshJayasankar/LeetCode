/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int sumEvenGrandparent(TreeNode root) {
        int sum = 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        while (!q.isEmpty()) {
            TreeNode curr = q.poll();
            if (curr.val % 2 == 0) {
                if (curr.left != null) {
                    if (curr.left.left != null) {
                        sum += curr.left.left.val;
                    }
                    if (curr.left.right != null) {
                        sum += curr.left.right.val;
                    }
                }
                if (curr.right != null) {
                    if (curr.right.left != null) {
                        sum += curr.right.left.val;
                    }
                    if (curr.right.right != null) {
                        sum += curr.right.right.val;
                    }
                }
            }
            if (curr.left != null) {
                q.add(curr.left);
            }
            if (curr.right != null) {
                q.add(curr.right);
            }
        }
        return sum;
    }
}