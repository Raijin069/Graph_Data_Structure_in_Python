from random import randint as rd

def quick_sort(arr,left,right):
    if left<right:
        partation_pos = partation(arr,left,right)
        quick_sort(arr,left,partation_pos-1)
        quick_sort(arr,partation_pos+1,right)

def partation(arr,left,right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i+=1
        while j > left and arr[j] >= pivot:
            j-=1

        if i<j:
            arr[i] , arr[j]  = arr[j] , arr[i]

    if arr[i] > pivot:
        arr[i] , arr[right]  = arr[right] , arr[i]

    return i

arr = [rd(10,60) for i in range(12)]
print(arr)
quick_sort(arr,0,len(arr)-1)
print(arr)



