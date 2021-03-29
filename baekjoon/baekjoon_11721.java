import java.util.Scanner;

public class baekjoon_11721 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String input = sc.nextLine();
        int length = input.length();
        for(int i=0;i<=length-10;i+=10){
            System.out.println(input.substring(i,i+10));
        }
        System.out.println(input.substring(length/10*10));
    }
}
