/*
    https://leetcode.com/problems/binary-tree-level-order-traversal/
    LeetCode 102 : Binary Tree Level Order Traversal (Difficulty : Medium)

    [문제]
    binary tree의 root가 주어질 때, level(층)을 순서대로 value를 2차원 배열로 리턴하라.
    순서 : left to right, level by level

    [풀이]
    먼저, root가 null이면 빈 배열을 리턴한다.
    큐를 생성하여 한 층씩 확인하도록 한다.
    너비우선탐색과 같은 탐색 순서로, 1층->2층->3층 .. 순서로 확인한다.
    while문을 한번씩 실행할 때 마다 현재 큐의 크기만큼 반복하며, 확인하는 노드의 left,right를 다시 큐에 저장한다.
*/

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class leetcode_102 {
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

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> answer = new ArrayList<>();
        if (root == null)
            return answer;

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty()) { // 노드를 모두 확인
            int size = q.size(); // 현재 큐에 들어있는 노드 수 (한 층의 노드 수)
            ArrayList<Integer> values = new ArrayList<>();
            while (size > 0) {
                TreeNode node = q.poll();
                values.add(node.val);
                if (node.left != null)
                    q.add(node.left);
                if (node.right != null)
                    q.add(node.right);
                size--;
            }
            answer.add(values);
        }

        return answer;
    }

}
