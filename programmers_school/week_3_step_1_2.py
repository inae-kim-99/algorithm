def solution(N, number):
    s = [set() for _ in range(8)]
    s[0].add(N)

    for i in range(1, 8):
        s[i].add(int(str(N)*(i+1)))
        for j in range(0, i):
            for n1 in s[j]:
                for n2 in s[i-j-1]:
                    s[i].add(n1 + n2)
                    s[i].add(n1 - n2)
                    s[i].add(n1 * n2)
                    if n2 != 0:
                        s[i].add(n1 // n2)

    for i in range(len(s)):
        if number in s[i]:
            return i+1

    return -1
