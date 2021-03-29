import java.util.Scanner;

public class backjoon_1541 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();
        int original_num = num;
        int count = 0;

        do {
            int sum = num / 10 + num % 10;
            num = (num % 10) * 10 + sum % 10;
            count++;
        } while (num != original_num);

        System.out.println(count);
    }
}
