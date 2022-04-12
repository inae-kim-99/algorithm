def solution(n, arr1, arr2):
    answer = []
    length = len(arr1)
    for n1, n2 in zip(arr1, arr2):
        row = bin(n1 | n2)[2:]
        row = row.rjust(length, '0')
        row = row.replace('1', '#')
        row = row.replace('0', ' ')
        answer.append(row)
    return answer
