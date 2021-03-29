class Solution {

    static String calculate(String str) {

        // 단계 1
        if (str.isEmpty())
            return "";

        // 단계 2
        String u = "", v = "";
        int count = 0;
        boolean isCorrect = true;
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(')
                count += 1;
            else
                count -= 1;
            if (count == 0) {
                u = str.substring(0, i+1);
                v = str.substring(i+1);
                break;
            }
            if (count < 0)
                isCorrect = false;
        }

        // 단계 3, 4
        String calculateV = calculate(v);
        if (isCorrect)
            return u + calculateV;
        else {
            String newStr = "(" + calculateV + ")";
            for (int i = 1; i < u.length() - 1; i++)
                if (u.charAt(i) == '(')
                    newStr += ')';
                else
                    newStr += '(';
            return newStr;
        }
    }

    public String solution(String p) {
        return calculate(p);
    }
}