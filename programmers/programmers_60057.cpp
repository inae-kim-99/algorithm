// https://programmers.co.kr/learn/courses/30/lessons/60057
#include <string>
#include <vector>
#include<iostream>
using namespace std;

int solution(string s) {
    int min = 1000; // �ּ� ���ڿ��� ���� ����
    if(s.length() < 3)
        return s.length();
    for(int cut=1;cut<=s.length()/2;cut++){ // ���� : 1 ~ ���ڿ��Ǳ���/2 ����
        int now = 0;
        int count = 1;
        string str = s.substr(0,cut);
        for(int start=cut;start<s.length()-s.length()%cut;start+=cut){ // ���� ������ Ȯ��
            if(str != s.substr(start,cut)){ // ���� substr�̶� �� ���ڿ��� ��ġ���� ���� ���
                str = s.substr(start,cut);
                if(count == 1){ // �� ���ڿ��� ������� ���� ���
                    now+=cut;
                }else{  // �� ���ڿ��� ����Ǿ��� ���
                    now+=(cut+to_string(count).length());
                }
                count = 1;
            }else{ // ���� substr�̶� �� ���ڿ��� ��ġ�� ���
                count++;
            }
        }
        
        if(count != 1) // �������� ����� ���ڰ� ���ٸ�
            now+=(cut+to_string(count).length())+s.length()%cut;
        else // �ִٸ�
            now+=cut+s.length()%cut;
        
        if(min > now){ // ���� ���ڿ��� �ּ� ���̶��
            min = now;
        }
    }
    return min;
}