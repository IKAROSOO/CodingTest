def bubble_sort(arr):
    n = len(arr)
    temp = 0

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr

n = int(input())
arr = [int(input()) for i in range(n)]

arr = bubble_sort(arr)

for i in range(n):
    print(arr[i])