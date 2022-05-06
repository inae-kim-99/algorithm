# https://programmers.co.kr/learn/courses/30/lessons/81303
# programmers 71303 : 2021 카카오 채용연계형 인턴십 - 표 편집
# LEVEL : 3

def solution(n, k, cmd):
    answer = ['O'] * n
    table = {i : [i-1, i+1] for i in range(n)}
    remove = []
    
    for c in cmd:
        if c == "C":
            remove.append([k, table[k][0], table[k][1]])
            if table[k][0] != -1:
                table[table[k][0]][1] = table[k][1]
            if table[k][1] != n:
                table[table[k][1]][0] = table[k][0]
                k = table[k][1]
            else:
                k = table[k][0]
        elif c == 'Z':
            removed, left, right = remove.pop()
            if left != -1:
                table[left][1] = removed
            if right != n:
                table[right][0] = removed
        else:
            c = c.split(' ')
            if c[0] == 'U':
                for _ in range(int(c[1])):
                    k = table[k][0]
            else:
                for _ in range(int(c[1])):
                    k = table[k][1]

    for i in range(len(remove)):
        answer[remove[i][0]] = 'X'
    
    return ''.join(answer)


cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]	
n = 8
k = 2

print(solution(n, k, cmd))