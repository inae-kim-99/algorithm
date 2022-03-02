# https://programmers.co.kr/learn/courses/30/lessons/72411
# programmers : 2021 KAKAO BLIND RECRUITMENT - 메뉴 리뉴얼
# LEVEL 2

from itertools import combinations


def solution(orders, course):
    answer = []

    for i in range(len(orders)):
        order = list(orders[i])
        order.sort()
        orders[i] = ''.join(order)

    for food_num in course:
        food_dict = {}
        for order in orders:
            for combination in list(combinations(order, food_num)):
                foods = ''.join(combination)
                if foods in food_dict.keys():
                    food_dict[foods] += 1
                else:
                    food_dict[foods] = 1
                # print(foods)
        print(food_dict)
        selected = []
        num = 1
        for food, count in food_dict.items():
            if count > num:
                # print(food, end=", ")
                selected.clear()
                selected.append(food)
                num = count
            elif count != 1 and count == num:
                # print(food, end=", ")
                selected.append(food)
        print(selected)
        answer.extend(selected)

    answer.sort()
    return answer


def find_same_order(first, second):
    order = ""
    for c1 in first:
        for c2 in second:
            if c1 == c2:
                order += c1
    return order


orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
solution(orders, course)
