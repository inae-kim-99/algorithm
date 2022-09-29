# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    letters = ""

    while A > 0 or B > 0:
        if A > B:
            if letters[-2:] == 'aa':
                letters += 'b'
                B -= 1
            else:
                letters += 'a'
                A -= 1
        else:
            if letters[-2:] == 'bb':
                letters += 'a'
                A -= 1
            else:
                letters += 'b'
                B -= 1

    return letters
