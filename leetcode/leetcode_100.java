/*
    https://leetcode.com/problems/same-tree/
    LeetCode 100 : Same Tree (Difficulty : Easy)

    [문제]
    binary tree p, q가 주어질 때
    p와 q가 같은 트리이면 true, 다른 트리이면 false를 리턴하라.

    [풀이]
    1) p의 노드는 pStack, q의 노드는 qStack에 저장한다. 먼저 root 노드를 각각 저장한다.
    2) 너비우선탐색으로 Queue에 맨 앞에 있는 노드를 꺼내어 그것이 null이라면 다음 것을 꺼내고
       아니라면 val을 비교한다.
    3) 꺼낸 노드의 left, right를 Queue에 저장한다.
    4) Queue가 비었을 때까지 (2,3)을 반복한다.
*/

import java.util.LinkedList;
import java.util.Queue;

public class leetcode_100 {
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

    public boolean isSameTree(TreeNode p, TreeNode q) {

        Queue<TreeNode> pQueue = new LinkedList<>();
        Queue<TreeNode> qQueue = new LinkedList<>();
        pQueue.add(p);
        qQueue.add(q);

        while (!pQueue.isEmpty()) {
            TreeNode pNode = pQueue.poll();
            TreeNode qNode = qQueue.poll();
            if (pNode == null && qNode == null)
                continue;
            if (pNode != null && qNode != null) {
                if (qNode.val != pNode.val) // value가 다른 경우
                    return false;
                pQueue.add(pNode.left);
                pQueue.add(pNode.right);
                qQueue.add(qNode.left);
                qQueue.add(qNode.right);
            } else { // 둘 중 하나만 null인 경우
                return false;
            }
        }
        return true;
    }
}
