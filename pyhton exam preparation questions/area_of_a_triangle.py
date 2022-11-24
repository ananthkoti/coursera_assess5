
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
# sum of three sides/3
s = (a + b + c) / 2

# calculate the area
# since area=(s*(s-a)*(s-b)*(s-c))^1/2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)