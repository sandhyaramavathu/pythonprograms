# your code goes here
l,h = map(int,raw_input().split())
for num in range(l,h):
    order =len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)
