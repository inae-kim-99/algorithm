import java.util.Scanner;

public class baekjoon_1152 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();
        input = input.trim();
        if(input.length() == 0)
            System.out.println(0);
        else {
            String[] words = input.split(" ");
            System.out.print(words.length);
        }
    }
}
