def bubble_sort(arr):
    n = len(arr)
    for i in range(n):  # i : 0부터 n-1까지
        for j in range(1, n-i): # j : 1부터 n-i까지 (1회전 할때마다 끝 원소를 하나씩 제외한다.)
            if arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp
    
    print(arr)

bubble_sort([5,4,3,2,1])
