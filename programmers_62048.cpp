int gcd(int a, int b){ // �ִ����� return
    if(b==0)
        return a;
    else
        return gcd(b, a%b);
}

long long solution(int w,int h) {
    long long answer = 1;
    
    long long num = gcd(w,h); // �ִ����� ���ϱ�
    
    answer = (long long)w * (long long)h - ((w/num + h/num - 1) * num);
    return answer;
}