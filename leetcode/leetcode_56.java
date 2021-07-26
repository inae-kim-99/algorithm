/*
    https://leetcode.com/problems/merge-intervals/
    LeetCode 56 : Merge Intervals (Difficulty : Medium)

    [문제]
    겹치는 구간이 존재하는 2차원 배열(intervals)이 주어질 때,
    그 구간들을 모두 병합하여 다시 배열로 반환하라.

    [풀이]
    intervals를 시작값을 기준으로 정렬한다.
    병합할 구간을 저장할 mInterval을 만들어 첫번째 interval을 저장한다.
    - 다음, intervals를 순서대로 확인하며 mInterval과 겹치는지 확인한다.
    - 겹친다면 두 끝값 중에 max를 mInterval[1]에 저장한다. (시작값은 정렬된 상태이므로 이미 mInterval[0]이 최소값임)
    - 겹치지 않으면 지금까지 정한 mInterval을 result에 추가하고,
      mInterval을 현재 interval 값으로 갱신한다.
 */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class leetcode_56 {

    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (o1, o2) -> o1[0] - o2[0]);
        int[] mInterval = {intervals[0][0], intervals[0][1]};
        List<int[]> result = new ArrayList<>();

        for (int i = 1; i < intervals.length; i++) {
            if (intervals[i][0] <= mInterval[1]) {
                mInterval[1] = Math.max(mInterval[1], intervals[i][1]);
            } else {
                result.add(mInterval);
                mInterval = intervals[i];
            }
        }
        result.add(mInterval);

        return result.toArray(new int[result.size()][2]);
    }
}
