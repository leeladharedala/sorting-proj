def srtarray(arr):
    for i in range(len(arr)):
        j=i+1
        for j in range(len(arr)):
            if arr[j]>arr[i]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
    return arr


