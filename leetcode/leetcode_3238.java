// https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
// Problem : Max Consecutive Ones

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {

        int count = 0, max = 0;

        for (int n : nums) {
            if (n == 1) {
                count++;
                if (count > max)
                    max = count;
            } else {
                count = 0;
            }
        }

        return max;
    }
}