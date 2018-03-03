a=int(input("enter upto which "))
if a < 1:
    print("Please, enter a positive number...")
else:
    sum = 0
while a > 0:
    sum += a
    a -= 1
    print("Sum = ", sum)
