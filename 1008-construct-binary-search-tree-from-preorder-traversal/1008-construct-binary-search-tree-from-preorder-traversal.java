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
    public void insertion(TreeNode root,int val){
        TreeNode t=root;
        TreeNode p=null;
        TreeNode nw=new TreeNode(val,null,null);
        while(t!=null){
            p=t;
            if(t.val>val) t=t.left;
            else t=t.right;
        }
        if(p.val>val) p.left=nw;
        else p.right=nw;
    }
    public TreeNode bstFromPreorder(int[] preorder) {
        TreeNode root=new TreeNode(preorder[0],null,null);
        for(int i=1;i<preorder.length;i++){
            insertion(root,preorder[i]);
        }
        return root;
    }
}