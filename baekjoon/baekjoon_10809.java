import java.util.Scanner;

public class baekjoon_10809 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();

        for(char ch='a';ch<='z';ch++){
            System.out.print(input.indexOf(ch)+" ");
        }
    }
}
