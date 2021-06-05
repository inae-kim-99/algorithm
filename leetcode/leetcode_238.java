/*
    https://leetcode.com/problems/product-of-array-except-self/
    LeetCode 238 : Product of Array Except Self (Difficulty : Medium)

    [문제]
    1차원 배열 nums 가 주어졌을 때, 아래 조건에 맞는 answer 배열을 return 한다.
    answer[i] 에는 nums[i]를 제외한 모든 요소를 곱한 값이 저장되어야 한다.

    [간단 풀이]
    answer[i]에 저장해야 하는 값은 nums[i]를 제외한 모든 요소를 곱한 값이다.
    다시 말해서, answer[i]의 (오른쪽 요소들의 곱) * (왼쪽 요소들의 곱) 이다.
    왼쪽 요소들을 곱한 값들은 answer[i] = answer[i-1] * nums[i-1] 이므로 반복문을 활용하여 곱하고,
    오른쪽 또한 같은 방법으로 곱한다.
*/

public class leetcode_238 {
    static public int[] productExceptSelf(int[] nums) {

        int len = nums.length;
        int[] answer = new int[len];

        answer[0] = 1;
        for (int i = 1; i < len; i++) {
            answer[i] = nums[i - 1] * answer[i - 1];
            System.out.println(answer[i]);
        }

        int right = 1;
        for (int i = len - 1; i >= 0; i--) {
            answer[i] *= right;
            right *= nums[i];
        }

        return answer;
    }

    public static void main(String[] args) {
        int[] temp = {1, 2, 3, 4};
        System.out.println();
        for (int num : productExceptSelf(temp)) {
            System.out.println(num);
        }
    }

}

