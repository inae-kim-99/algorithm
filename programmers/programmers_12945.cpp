// https://programmers.co.kr/learn/courses/30/lessons/12945#qna

#include <string>
#include <vector>
#include <map>

using namespace std;

map<long long,long long> m;

long long fb(long long n){
    if(n == 0) return 0;
    else if(n==1) return 1;

    map<long long,long long>::iterator iter1 = m.find(n-1);
    map<long long,long long>::iterator iter2 = m.find(n-2);

    return iter1->second + iter2->second;
}

int solution(int n) {
    // 반복해서 같은 값을 구해야 하므로 미리 모든 값을 연산하여 저장한다.
    for(int i=0;i<n;i++){
        m.insert(make_pair(i,fb(i) % 1234567));
    }
    long long answer = fb(n) % 1234567;
    return answer;
}