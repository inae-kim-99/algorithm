// https://programmers.co.kr/learn/courses/30/lessons/60058

#include <string>
#include <vector>
using namespace std;

string recursive(string str){
    string u,v;
    
    if(str.empty()){ // 빈 문자열인 경우
        return "";
    }
    int check = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == '(') check++;
        else check--;
        if(check == 0){ // 균형잡힌 괄호 문자열인 경우
            u = str.substr(0,i+1);
            v = str.substr(i+1,str.length()-i-1);
            for(int j=0;j<u.length();j++){
                if(str[j] == '(') check++;
                else check--;
                if(check < 0){ // u가 "올바른 괄호 문자열"이 아닐 경우
                    v = "("+recursive(v)+")";
                    for(int k=1;k<u.length()-1;k++){
                        if(u[k] == '(') v += ')';
                        else v += '(';
                    }
                    return v;
                }
            }
            // u가 "올바른 괄호 문자열"인 경우
            return u+recursive(v);
        }
    }
}

string solution(string p){
    return recursive(p);
}