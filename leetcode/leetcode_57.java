/*
    https://leetcode.com/problems/insert-interval/
    LeetCode 57 : Insert Interval (Difficulty : Medium)

    [문제]
    겹치지 않는 구간들을 정렬하여 나열한 2차원 배열(intervals)과 새로운 구간(newInterval)이 주어질 때,
    intervals에 newInterval을 삽입하라. 이때 겹치는 구간은 모두 병합하여 삽입하라.

    [풀이]
    intervals를 순서대로 확인하며 겹치지 않는 구간인지, 겹치는 구간인지 확인한다.
    1) newInterval 보다 앞에 있는 구간이라면 result에 추가한다.
    2) newInterval 보다 뒤에 있는 구간이라면 result에 추가한다.
    3) newInterval과 겹치는 구간이라면, 둘 중 시작값의 최소 값, 끝값의 최대 값을 저장한다.
       겹치는 구간이 나타나는 동안 계속 반복한다.

    - 2번이 해당되는 경우 더 이상 겹치는 구간이 발생하지 않기 때문에,
      지금까지 저장한 newInterval을 result에 추가한다.
      그리고 newInterval에 현재 interval를 저장하여 계속 반복 추가한다.
 */

import java.util.ArrayList;
import java.util.List;

public class leetcode_57 {

    public int[][] insert(int[][] intervals, int[] newInterval) {

        List<int[]> result = new ArrayList<>();

        for (int[] interval : intervals) {
            if (interval[1] < newInterval[0]) { // newInterval 앞에 있는 경우
                result.add(interval);
            } else if (interval[0] > newInterval[1]) {// newInterval 뒤에 있는 경우
                result.add(newInterval);
                newInterval = interval;
            } else {
                newInterval[0] = Math.min(newInterval[0], interval[0]);
                newInterval[1] = Math.max(newInterval[1], interval[1]);
            }
        }

        result.add(newInterval);

        return result.toArray(new int[result.size()][2]);
    }


}
