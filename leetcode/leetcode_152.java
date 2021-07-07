/*
    https://leetcode.com/problems/maximum-product-subarray/
    LeetCode 152 : Maximum Product Subarray (Difficulty : Medium)

    [문제]
    1차원 배열 nums가 주어질 때,
    원소의 곱이 최대 값이 되는 연속 부분 배열을 찾아서
    그 곱한 값을 리턴하라.

    [풀이]
    기본적으로 첫번째 원소부터 하나씩 product 변수에 곱한다.

    처음으로 음수를 만나게 되면 그 수까지의 곱을 firstNegative에 저장한다.
    (만약 그 이후의 곱이 항상 음수라면 product는 점점 최소값이 되어가기 때문에
    첫번째 음수까지의 곱을 나눈 값을 max와 비교한다.)

    만약 0을 만나게 되면 곱을 초기화하고, 다음 수 부터 다시 곱한다.
    최대값(max)가 0보다 작다면 0으로 저장한다. 처음 음수를 만나는 경우도 다시 저장한다.
    (부분 배열 중에 0을 포함할 수 없기 때문에! -> 최대값 X)
*/

public class leetcode_152 {
    public int maxProduct(int[] nums) {
        int max = nums[0];
        int product = 1, firstNegative = 1;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                firstNegative = 1;
                product = 1;
                if (max < 0)
                    max = 0;
            } else {
                product *= nums[i];
                if (product < 0)
                    max = Math.max(product / firstNegative, max);
                else
                    max = Math.max(product, max);
                if (firstNegative == 1 && nums[i] < 0)
                    firstNegative = product;
            }
        }

        return max;
    }
}
