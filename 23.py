min = int(raw_input())
def smallest(arr,h) :
	min = arr[0]
	for i in range(1,h) :
		if arr[i] < min :
			min = arr[i]
	return min
arr = [1,2,3]
h = len(arr)
ans = smallest(arr,h)
print(ans)
