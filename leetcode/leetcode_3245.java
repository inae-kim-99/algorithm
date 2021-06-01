// https://leetcode.com/explore/learn/card/fun-with-arrays/525/inserting-items-into-an-array/3245/
// Problem : Duplicate Zeros

class Solution {
    public void duplicateZeros(int[] arr) {

        int len = arr.length;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0) {
                for (int j = len - 1; j > i + 1; j--) {
                    arr[j] = arr[j - 1];
                }
                if (i != len - 1)
                    arr[i + 1] = 0;
                i++;
            }
        }

    }
}