// https://programmers.co.kr/learn/courses/30/lessons/42583
// 프로그래머스 42583번 : 다리를 지나는 트럭

import java.util.LinkedList;
import java.util.Queue;

public class programmers_42583 {

    class Truck {
        int weight;
        int location;

        public Truck(int w, int l) {
            weight = w;
            location = l;
        }

        public void move() {
            location += 1;
        }

    }

    Queue<Truck> bridge;

    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        bridge = new LinkedList<>();

        int sum = 0, idx = 0, truck_num = truck_weights.length;
        for (int time = 0; ; time++) {
            // 제일 앞에 있는 트럭 위치 확인
            if (time != 0 && bridge.peek().location == bridge_length) {
                sum -= bridge.peek().weight;
                bridge.remove();
            }
            // 트럭들의 위치 + 1
            for (Truck t : bridge)
                t.move();
            // 트럭 추가
            if (idx < truck_num && sum + truck_weights[idx] <= weight) {
                sum += truck_weights[idx];
                bridge.add(new Truck(truck_weights[idx], 1));
                idx += 1;
            }
            // 트럭이 모두 지나간 경우
            if (bridge.isEmpty()) {
                answer = time + 1;
                break;
            }
        }

        return answer;
    }
}
