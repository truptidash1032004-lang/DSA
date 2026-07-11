def remove_duplicate(arr,n):
    if n==0:
        return 0
    i=0
    for j in range(1,n):
        if arr[j]!=arr[i]:
            i=i+1
            arr[i]=arr[j]
    return i+1
arr = [1, 1, 2, 2, 2, 3, 3]
n = len(arr)

k = remove_duplicate(arr, n)

print("Number of unique elements =", k)
print("Unique elements =", arr[:k])