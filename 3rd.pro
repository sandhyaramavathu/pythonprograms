nature = int(raw_input())
reverse = 0
while(nature>0):
    remainder = nature%10
    reverse=reverse*10+remainder
    nature = nature/10
print reverse
