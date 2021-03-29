import java.util.Scanner;

public class baekjoon_9012 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int testcase = Integer.parseInt(sc.nextLine());
        for(int i=0;i<testcase;i++){
            String input = sc.nextLine();
            int temp = 0;
            boolean isVPS = true;
            for(int j=0;j<input.length();j++){
                if(input.charAt(j) == '(')
                    temp++;
                else{
                    if(temp==0){
                        isVPS = false;
                        break;
                    }else{
                        temp--;
                    }
                }
            }
            if(temp != 0)
                isVPS = false;

            if(isVPS)
                System.out.println("YES");
            else
                System.out.println("NO");
        }


    }
}
