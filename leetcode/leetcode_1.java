// https://leetcode.com/problems/two-sum/
// LeetCode : Two Sum (Difficulty : Easy)

// 간단 풀이
// 단순하게 이중 반복문을 활용하여 풀이.
// (i,j)로 모든 경우의 수를 확인하며 두 수의 합이 target이 되는 경우 answer에 저장하고 값을 리턴한다.

public class leetcode_1_two_sum {
    class Solution {
        public int[] twoSum(int[] nums, int target) {

            int[] answer = new int[2];

            for (int i = 0; i < nums.length - 1; i++) {
                for (int j = i + 1; j < nums.length; j++) {
                    if (nums[i] + nums[j] == target) {
                        answer[0] = i;
                        answer[1] = j;
                        return answer;
                    }
                }
            }

            return answer;
        }
    }
}
