// https://programmers.co.kr/learn/courses/30/lessons/60057
#include <string>
#include <vector>
#include<iostream>
using namespace std;

int solution(string s) {
    int min = 1000; // 최소 문자열의 길이 저장
    if(s.length() < 3)
        return s.length();
    for(int cut=1;cut<=s.length()/2;cut++){ // 단위 : 1 ~ 문자열의길이/2 까지
        int now = 0;
        int count = 1;
        string str = s.substr(0,cut);
        for(int start=cut;start<s.length()-s.length()%cut;start+=cut){ // 단위 개수씩 확인
            if(str != s.substr(start,cut)){ // 현재 substr이랑 앞 문자열이 일치하지 않을 경우
                str = s.substr(start,cut);
                if(count == 1){ // 앞 문자열이 압축되지 않은 경우
                    now+=cut;
                }else{  // 앞 문자열이 압축되었을 경우
                    now+=(cut+to_string(count).length());
                }
                count = 1;
            }else{ // 현재 substr이랑 앞 문자열이 일치할 경우
                count++;
            }
        }
        
        if(count != 1) // 마지막에 압축된 문자가 없다면
            now+=(cut+to_string(count).length())+s.length()%cut;
        else // 있다면
            now+=cut+s.length()%cut;
        
        if(min > now){ // 현재 문자열이 최소 길이라면
            min = now;
        }
    }
    return min;
}