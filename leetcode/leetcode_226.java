/*
    https://leetcode.com/problems/invert-binary-tree/
    LeetCode 226 : Invert Binary Tree (Difficulty : Easy)

    [문제]
    binary tree의 root 노드가 주어질 때,
    tree를 좌우 대칭하여 바꾸고 다시 루트를 리턴하라.

    [풀이]
    간단하게 생각하면 확인하는 노드의 left, right를 서로 바꾸면 된다.
    1) Queue에 root를 저장한다.
    2) Queue에서 맨 앞에 있는 노드를 하나 꺼내어 그것의 left, right를 서로 바꾼다.
    3) 꺼낸 노드의 left, right가 각각 null이 아니라면 Queue에 저장한다.
    4) Queue가 비었을 때까지 (2,3)을 반복한다.
*/

import java.util.LinkedList;
import java.util.Queue;

public class leetcode_226 {
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

    public TreeNode invertTree(TreeNode root) {
        if (root == null)
            return null;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;
            if (node.left != null)
                queue.add(node.left);
            if (node.right != null)
                queue.add(node.right);
        }

        return root;
    }
}
