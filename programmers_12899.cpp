// https://programmers.co.kr/learn/courses/30/lessons/12899

#include <string>
using namespace std;

string solution(int n) {
    string answer = "";
    while(n > 0){
        int remain = n%3;
        n = n/3;
        if(remain == 0){ // 3���� ���������� ��� �� -1�� ���ش�.
            answer = "4" + answer;
            n--;
        }else if(remain == 1){ // �������� 1�� ���
            answer = "1" + answer;
        }else{ // �������� 2�� ���
            answer = "2" + answer;
        }
    }
    return answer;
}