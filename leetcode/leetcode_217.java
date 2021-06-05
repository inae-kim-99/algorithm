/*
    https://leetcode.com/problems/contains-duplicate/
    LeetCode 217 : Contains Duplicate (Difficulty : Easy)

    [문제]
    주어진 배열에서 중복된 값이 들어있으면 true, 모두 다르면 false를 return 해라.
    [간단 풀이]
    nums 배열을 정렬하고, 순서대로 2개씩 값을 비교한다.
    [시간 복잡도]
    sort는 O(nlogn), 비교는 O(n)
*/

import java.util.Arrays;

public class leetcode_217 {

    public boolean containsDuplicate(int[] nums) {

        Arrays.sort(nums);

        for (int i = 0; i < nums.length - 1; i++) {
            if (nums[i] == nums[i + 1])
                return true;
        }

        return false;
    }

}
