/*
    https://leetcode.com/problems/valid-parentheses/
    LeetCode 20 : Valid Parentheses (Difficulty : Easy)

    [문제]
    '(', ')', '{', '}', '[', ']' 의 문자만을 포함하는 문자열 s가 주어진다.
    이때, 유효한 문자열인지 true/false로 반환하라.
    1) 여는 괄호는 같은 종류의 괄호로 닫아야 한다.
    2) 올바른 순서로 괄호가 닫혀야 한다.

    [풀이]
    Stack을 활용하여 가장 먼저 닫아야 하는 괄호를 top으로 확인해나간다.
    HashMap을 활용하여 올바른 괄호로 닫는지 확인한다.

    같은 괄호에 대해,
    '('의 key를 1이라고 하고, ')'의 key를 10이라고 하여
    닫는 괄호에 10을 나누어 같은지 확인한다.
 */

import java.util.HashMap;
import java.util.Stack;

public class leetcode_20 {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap<Character, Integer> map = new HashMap<>();
        map.put('(', 1);
        map.put(')', 10);
        map.put('{', 2);
        map.put('}', 20);
        map.put('[', 3);
        map.put(']', 30);

        for (int i = 0; i < s.length(); i++) {
            char now = s.charAt(i);
            if (map.get(now) < 10) {
                stack.add(now);
            } else if (!stack.isEmpty() && map.get(stack.peek()).equals(map.get(now) / 10)) {
                stack.pop();
            } else {
                return false;
            }
        }

        return stack.isEmpty();
    }
}
