
n1 = input('Enter First Number: ')
n2 = input('Enter Second Number: ')

print("Value of num1 before swapping: ", n1)
print("Value of num2 before swapping: ", n2)

# swapping two numbers using temporary variable
temp = n1
n1 = n2
n2 = temp

print("Value of num1 after swapping: ", n1)
print("Value of num2 after swapping: ", n2)
