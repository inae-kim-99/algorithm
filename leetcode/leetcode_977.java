// https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/
// Problem : Squares of a Sorted Array

class Solution {
    public int[] sortedSquares(int[] nums) {

        int[] list = new int[nums.length];

        for (int i = 0; i < nums.length; i++)
            list[i] = nums[i] * nums[i];

        Arrays.sort(list);

        return list;
    }
}