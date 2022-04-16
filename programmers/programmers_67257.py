# https://programmers.co.kr/learn/courses/30/lessons/67257#
# programmers 67257 : 2020 카카오 인턴십 - 수식 최대화
# LEVEL 2

from itertools import permutations

def calculate(priority, n, expression):
    if n == len(priority):
        return str(eval(expression))
    elif priority[n] == '+':
        return str(eval("+".join([calculate(priority, n+1, e) for e in expression.split('+')])))
    elif priority[n] == '-':
        return str(eval("-".join([calculate(priority, n+1, e) for e in expression.split('-')])))
    elif priority[n] == '*':
        return str(eval("*".join([calculate(priority, n+1, e) for e in expression.split('*')])))

def solution(expression):
    operators = []
    result = 0
    
    if '+' in expression:
        operators.append('+')
    if '-' in expression:
        operators.append('-')
    if '*' in expression:
        operators.append('*')
    
    priorities = permutations(operators, len(operators))
    
    for priority in priorities:
        result = max(result, abs(int(calculate(priority, 0, expression))))
        
    return result