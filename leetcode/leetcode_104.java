/*
    https://leetcode.com/problems/maximum-depth-of-binary-tree/
    LeetCode 104 : Maximum Depth of Binary Tree (Difficulty : Easy)

    [문제]
    binary tree 가 주어질 때, 그것의 최대 depth를 구하여라.

    [풀이]
    treenode가 null이면 0을 리턴하고,
    null이 아니라면
    (그 노드의 left와 right 노드의 깊이 중 긴 것) + 1
    을 리턴한다.
*/

public class leetcode_104 {
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;
        else
            return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}
