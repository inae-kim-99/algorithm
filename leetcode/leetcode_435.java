/*
    https://leetcode.com/problems/non-overlapping-intervals/
    LeetCode 435 : Non-overlapping Intervals

    [문제]
    intervals[i] = [start(i), end(i)] 형태로 주어지는 2차원 배열(intervals)가 주어질 때,
    겹치는 구간이 발생하지 않도록 하기 위해 삭제해야 하는 구간의 최소 수를 구하여라.

    [풀이]
    intervals를 start(i)를 기준으로 오름차순 정렬한다.
    구간이 -20000 ~ 20000 이기 때문에 인덱스 참조를 위해 20000을 더해준다.

    - start가 비어있다면 해당 구간을 저장한다.

    - start가 비어있지 않다면 겹치는 구간이 발생한 것이므로,
      1) end가 가장 큰 값이라면 해당 구간을 삭제한다.
      2) 아니라면 해당 구간 대신 가장 긴 값을 삭제한다. (현재 구간과 겹치는 구간)
         여기서, intervals는 start를 기준으로 정렬되어 있기 때문에
         (해당 구간의 start, 가장 긴 end) 사이의 구간만 삭제해도 무방하다.

      -> 삭제하는 경우의 수를 저장하여 반환한다.
 */

import java.util.Arrays;

public class leetcode_435 {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals, (o1, o2) -> o1[0] - o2[0]);
        boolean[] exist = new boolean[40002];

        int end = 0, count = 0;
        for (int i = 0; i < intervals.length; i++) {
            intervals[i][0] += 20000;
            intervals[i][1] += 20000;
            if (!exist[intervals[i][0]]) { // 존재하지 않으면
                for (int j = intervals[i][0]; j < intervals[i][1]; j++)
                    exist[j] = true;
                end = intervals[i][1];
            } else if (intervals[i][1] < end) { // 현재 interval이 전보다 더 짧으면
                for (int j = intervals[i][1]; j < end; j++)
                    exist[j] = false;
                count++;
            } else {
                count++;
            }
        }
        return count;
    }
}
