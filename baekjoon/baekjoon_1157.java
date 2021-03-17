import java.util.Locale;
import java.util.Scanner;

public class baekjoon_1157 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        input = input.toLowerCase(Locale.ROOT);

        int CHARACTER_NUM = 26;
        int[] count = new int[CHARACTER_NUM];

        for (int i = 0; i < input.length(); i++) {
            count[input.charAt(i) - 'a'] += 1;
        }

        int maxIndex = 0;
        boolean isSame = false;
        for (int i = 1; i < CHARACTER_NUM; i++) {
            if (count[i] > count[maxIndex]) {
                maxIndex = i;
                isSame = false;
            } else if (count[i] == count[maxIndex]) {
                isSame = true;
            }
        }

        if (isSame)
            System.out.println("?");
        else
            System.out.println((char)('A'+maxIndex));
    }
}
