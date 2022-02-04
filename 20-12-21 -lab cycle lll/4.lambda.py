#Area of square
a=int(input("enter the side of the square:"))
print("area of the square is:")
x=lambda a : a**2
print(x(a))
#Area of triangle
l=int(input("enter the length of triangle:"))
h=int(input("enter the height of the triangle:"))
print("area of the triangle is:")
x=lambda l,h: 1/2*l*h
print(x(l,h))
#Area of rectangle
b=int(input("enter the breadth of rectangle:"))
m=int(input("enter the length of the rectangle:"))
print("area of rectangle:")
x=lambda b,m:b*m
print(x(b,m))
