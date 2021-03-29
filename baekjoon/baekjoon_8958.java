import java.util.Scanner;

public class baekjoon_8958 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testcase = Integer.parseInt(sc.nextLine());

        for (int i = 0; i < testcase; i++) {
            String input = sc.nextLine();
            int score = 1;
            int total = 0;
            for (int j = 0; j < input.length(); j++) {
                if (input.charAt(j) == 'O') {
                    total += score;
                    score++;
                } else {
                   score = 1;
                }
            }
            System.out.println(total);
        }

    }
}
