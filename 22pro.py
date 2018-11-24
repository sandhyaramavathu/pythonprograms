maximum = int(raw_input())
def largest(arr,m):
    maximum = arr[0]
    for i in range(1, m):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum
arr = [2,3,1,45,5]
m = len(arr)
ans = largest(arr,m)
print (ans)
