/*
    https://leetcode.com/problems/course-schedule/
    LeetCode 207 : Course Schedule

    [문제]
    numCourse개의 수업을 들어야하고, 그 중 [수업, 선행되어야 하는 수업]의 쌍들이 주어질 때
    numCourse개의 수업을 모두 들을수 있는지 리턴하라.
    [0, 1] : 1을 들어야 0을 들을 수 있다.

    [풀이]
    수업은 노드, 선행되어야 함의 유무는 방향이 있는 간선으로 나타낼 수 있다.
    따라서 수업을 모두 들을 수 없는 경우는 사이클의 유무와 같게 된다.
    ex) [0,1], [1,2]가 주어졌는데 [2, 0]도 주어진다면 사이클이 생겨 수강 순서를 정할 수 없다.

    dfs를 적용하여 사이클 유무를 판단한다.
    - visit[i]는 방문 유무, finish[i]는 경로가 진행중(false)인지 끝났는지(true) 저장한다. (진행 중에 연결이 되면 사이클)
    - 방문되지 않은 노드를 차례대로 탐색한다.
    - 현재 방문한 노드와 연결된 노드들을 확인하여 방문되지 않은 노드이면 탐색을 시작한다.
    - 방문된 노드인데 경로가 진행중이면 (finish[i] = false) 사이클이 생성된 것이므로 탐색을 종료한다.
 */

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class leetcode_207 {

    HashMap<Integer, List<Integer>> map;
    boolean[] visit, finish;
    boolean cycle = false;

    public void hasCycle(int node) {
        visit[node] = true;

        for (int i = 0; i < map.get(node).size(); i++) {
            int next = map.get(node).get(i);
            if (!visit[next]) { // 방문하지 않았으면
                hasCycle(next);
            } else if (!finish[next]) { // 방문한 곳인데 경로가 다시 이어진 경우 -> 사이클
                cycle = true;
                return;
            }
        }

        finish[node] = true;
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        map = new HashMap<>();
        for (int i = 0; i < numCourses; i++)
            map.put(i, new ArrayList<>());

        visit = new boolean[numCourses];
        finish = new boolean[numCourses];

        for (int i = 0; i < prerequisites.length; i++)
            map.get(prerequisites[i][0]).add(prerequisites[i][1]);

        for (int i = 0; i < numCourses; i++) {
            if (!visit[i])
                hasCycle(i);
        }

        return !cycle;
    }
}
