maximum = int(raw_input())
def largest(arr,s):
    maximum = arr[0]
    for i in range(1, s):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum
arr = [2,3,1,45,5]
s = len(arr)
Ans = largest(arr,s)
print (Ans)
