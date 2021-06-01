// https://programmers.co.kr/learn/courses/30/lessons/42626
// 프로그래머스 42626번 : 힙(Heap) - 더 맵게

import java.util.PriorityQueue;

public class programmers_42626 {

    PriorityQueue<Integer> pq;

    public int solution(int[] scoville, int K) {
        int answer = 0;
        pq = new PriorityQueue<>();
        for (int level : scoville)
            pq.add(level);

        while (pq.peek() < K) {
            if (pq.size() >= 2) {
                int first = pq.poll();
                int second = pq.poll();
                pq.add(first + second * 2);
                answer += 1;
            } else {
                answer = -1;
                break;
            }
        }

        return answer;
    }

    public static void main(String[] args) {

    }
}
