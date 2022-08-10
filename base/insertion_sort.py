def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        temp = arr[i]
        prev = i-1

        while prev >= 0 and arr[prev] > temp: # 이전 원소가 temp보다 크면 오른쪽으로 이동시킨다.
            arr[prev+1] = arr[prev]
            prev -= 1

        arr[prev+1] = temp # temp보다 큰 값을 모두 왼쪽으로 이동시킨 후 값을 삽입한다.
    
    print(arr)

insertion_sort([5,4,3,2,1])