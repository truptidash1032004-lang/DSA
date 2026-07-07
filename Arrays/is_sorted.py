def is_sorted(arr,n):
    for i in range(1,n):
     if arr[i]>=arr[i-1]:
        print("sorted:")
        continue
     else:
        return False
     return True