lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())
lst.append(ele)
if all(i>100 for i in lst):
    print("over")
else:
    print("no")