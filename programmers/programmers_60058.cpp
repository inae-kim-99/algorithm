// https://programmers.co.kr/learn/courses/30/lessons/60058

#include <string>
#include <vector>
using namespace std;

string recursive(string str){
    string u,v;
    
    if(str.empty()){ // �� ���ڿ��� ���
        return "";
    }
    int check = 0;
    for(int i=0;i<str.length();i++){
        if(str[i] == '(') check++;
        else check--;
        if(check == 0){ // �������� ��ȣ ���ڿ��� ���
            u = str.substr(0,i+1);
            v = str.substr(i+1,str.length()-i-1);
            for(int j=0;j<u.length();j++){
                if(str[j] == '(') check++;
                else check--;
                if(check < 0){ // u�� "�ùٸ� ��ȣ ���ڿ�"�� �ƴ� ���
                    v = "("+recursive(v)+")";
                    for(int k=1;k<u.length()-1;k++){
                        if(u[k] == '(') v += ')';
                        else v += '(';
                    }
                    return v;
                }
            }
            // u�� "�ùٸ� ��ȣ ���ڿ�"�� ���
            return u+recursive(v);
        }
    }
}

string solution(string p){
    return recursive(p);
}