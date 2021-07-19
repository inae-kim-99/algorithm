/*
    https://leetcode.com/problems/clone-graph/
    LeetCode : Clone Graph (Difficulty : Medium)

    [문제]
    무방향 그래프 중 하나의 노드가 주어질 때,
    같은 그래프를 새로 생성하여 주어진 노드와 같은 노드를 리턴하라.

    [간단 풀이]
    확인할 노드를 큐에 저장하면서 새로운 노드에 복사를 진행한다. bfs로 진행한다.

    먼저 주어진 노드를 큐에 삽입하고, 맵에 저장한다.
    큐가 비어있을 때까지 다음을 진행한다.
    - 큐에서 노드(n)를 꺼내고, map에서 n.value인 노드(clone)를 찾는다.
    - 노드(n)의 neighbor들을 각각 확인한다.
    - neighbor가 방문된 노드이면 map에서 찾아 clone의 neighbors에 추가한다.
    - 방문되지 않은 노드이면 새로 생성하여 clone의 neighbors에 추가하고, map에 저장하고, 큐에 저장한다.
      (방문되지 않은 노드는 큐에 저장하여 그 neighbor들을 확인)
*/

import java.util.*;

public class leetcode_133 {

    class Node {
        public int val;
        public List<Node> neighbors;

        public Node() {
            val = 0;
            neighbors = new ArrayList<Node>();
        }

        public Node(int _val) {
            val = _val;
            neighbors = new ArrayList<Node>();
        }

        public Node(int _val, ArrayList<Node> _neighbors) {
            val = _val;
            neighbors = _neighbors;
        }
    }

    HashMap<Integer, Node> map;
    Queue<Node> q;

    public Node cloneGraph(Node node) {
        Node clonedNode = new Node();
        if (node == null)
            return null;

        map = new HashMap<>();
        q = new LinkedList<>();
        q.add(node);
        clonedNode.val = node.val;
        map.put(clonedNode.val, clonedNode);

        while (!q.isEmpty()) {
            Node n = q.poll();
            Node clone = map.get(n.val);
            for (Node neighbor : n.neighbors) {
                int value = neighbor.val;
                if (map.containsKey(value)) {
                    clone.neighbors.add(map.get(value));
                } else {
                    Node newNode = new Node(value);
                    clone.neighbors.add(newNode);
                    map.put(value, newNode);
                    q.add(neighbor);
                }
            }
        }

        return clonedNode;
    }
}
