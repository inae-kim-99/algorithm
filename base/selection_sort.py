def selection_sort(arr):
    n = len(arr)
    index_min = 0

    for i in range(n):
        index_min = i
        for j in range(i+1, n): # 최소 값의 위치를 찾는다.
            if arr[j] < arr[index_min]:
                index_min = j
        
        temp = arr[index_min]   # 최소값을 해당 자리에 넣는다.
        arr[index_min] = arr[i]
        arr[i] = temp

    print(arr)

selection_sort([5,4,3,2,1])