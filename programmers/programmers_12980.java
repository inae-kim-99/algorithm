import java.util.*;

public class programmers_12980 {
    public int solution(int n) {
        int ans = 0;

        while(n>0){
            if(n%2 == 1)
                ans+=1;
            n=n/2;
        }

        return ans;
    }
}