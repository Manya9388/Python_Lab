
def fact(num):
 factorial = 1
 if num < 0:
   print("factorial does not exist for negative numbers")
 else:
   for i in range(1,num + 1):
      factorial = factorial*i
 print("The factorial of", num, "is", factorial)

num = int(input("enter the number"))

fact(num)
