# https://programmers.co.kr/learn/courses/30/lessons/17680
# programmers 17680 : 2018 KAKAO BLIND RECRUITMENT - [1차]캐시
# LEVEL : 2

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5

    cities = [c.lower() for c in cities]
    cache = []
    time = 0
    
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.insert(0, city)
            time += 1
        else:
            if len(cache) < cacheSize:
                cache.insert(0, city)
            else:
                cache.pop()
                cache.insert(0, city)
            time += 5
    
    return time

solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])