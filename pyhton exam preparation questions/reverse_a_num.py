num = int(input("enter the number: "))
reversed_num = 0

while num != 0:
    # to get the last digit(remainder) of the number
    digit = num % 10 
    reversed_num = reversed_num * 10 + digit
    num //= 10

print("Reversed Number: " + str(reversed_num))