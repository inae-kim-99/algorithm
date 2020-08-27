// https://programmers.co.kr/learn/courses/30/lessons/12899

#include <string>
using namespace std;

string solution(int n) {
    string answer = "";
    while(n > 0){
        int remain = n%3;
        n = n/3;
        if(remain == 0){ // 3으로 나누어지는 경우 몫에 -1을 해준다.
            answer = "4" + answer;
            n--;
        }else if(remain == 1){ // 나머지가 1인 경우
            answer = "1" + answer;
        }else{ // 나머지가 2인 경우
            answer = "2" + answer;
        }
    }
    return answer;
}