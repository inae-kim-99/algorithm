// https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
// Problem : Find Numbers with Even Number of Digits

class Solution {
    public int findNumbers(int[] nums) {

        int answer = 0;

        for (int n : nums) {

            // Solve 1)
            // if(Integer.toString(n).length() % 2 == 0)
            //     answer++;

            // Solve 2)
            int digits = 0;
            while (n > 0) {
                n /= 10;
                digits++;
            }

            if (digits % 2 == 0)
                answer++;
        }

        return answer;
    }
}