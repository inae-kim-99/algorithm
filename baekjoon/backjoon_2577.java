import java.util.Scanner;

public class backjoon_2577 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        int sum = A * B * C;
        int[] frequency = new int[10];

        while (sum > 0) {
            frequency[sum % 10] += 1;
            sum = sum / 10;
        }

        for(int i=0;i<10;i++){
            System.out.println(frequency[i]);
        }
    }
}
