l = int(raw_input())
number = [1,2,3]
number.sort()
length = len(number)
if (length % 2 == 0):
    median = (number[(length)//2] + number[(length)//2-1]) / 2
else:
    median = number[(length-1)//2]
print(median)
