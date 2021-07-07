/*
    https://leetcode.com/problems/maximum-subarray/
    LeetCode 53 : Maximum Subarray (Difficulty : Medium)

    [문제]
    Integer 형태의 값들이 들어있는 1차원 배열이 주어질 때,
    최대 합이 되는 연속적인 부분 배열을 찾아 그 합을 리턴하라.

    [풀이]
    연속적인 부분 배열을 찾는 것이기 때문에 첫 번째 숫자부터 하나씩 더한다.
    i번 째까지의 합이 최대 값인 경우 max에 저장하고,
    만약 음수인 경우 sum을 다시 0으로 만들어 준다. (-> 최대 합을 구하기 위해 음수를 더할 필요가 없음)

*/

public class leetcode_53 {
    public int maxSubArray(int[] nums) {
        int max = Integer.MIN_VALUE;
        int sum = 0;

        for (int num : nums) {
            sum += num;
            if (sum > max)
                max = sum;
            if (sum < 0)
                sum = 0;
        }

        return max;
    }
}
