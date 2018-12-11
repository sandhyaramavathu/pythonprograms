max=int(raw_input())
def largest(arr,m):
    max=arr[0]
    for i in range(1, m):
        if arr[i]>max:
            max=arr[i]
    return max
arr=[2,3,1,45,5]
m=len(arr)
answer=largest(arr,m)
print (answer)
