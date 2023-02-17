def maxsum_subarray(arr):
    maxsum = arr[0]
    currsum = 0
    for i in range(len(arr)):
        currsum = max(currsum+arr[i],arr[i])
        maxsum = max(maxsum,currsum)
    return maxsum


arr = [-2,1,-3,4,-1,2,1,-5,4] 
print(maxsum_subarray(arr))
