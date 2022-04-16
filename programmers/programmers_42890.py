# https://programmers.co.kr/learn/courses/30/lessons/42890
# programmers 42890 : 2019 KAKAO BLIND RECRUITMENT - 후보키
# LEVEL : 2

from itertools import combinations


def solution(relation):
    length = len(relation)
    keys = []
    columns = [str(i) for i in range(len(relation[0]))]

    for i in range(1, len(relation[0])+1):
        cols_combination = combinations(columns, i)

        for cols in cols_combination:
            if is_minimality(set(cols), keys):
                joined_cols = set()

                for tup in relation:
                    new_tup = ""
                    for col in cols:
                        new_tup += tup[int(col)]
                    joined_cols.add(new_tup)

                if len(joined_cols) == length:
                    keys.append(set(cols))

    return len(keys)


def is_minimality(cols, keys):
    for key in keys:
        if len(key - cols) == 0:
            return False
    return True
