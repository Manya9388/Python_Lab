list1=[]
list2=[]
n = int(input("enter the limit of list 1 :"))
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
m = int(input("enter the limit of list 2:"))
for i in range(0,m):
    ele=int(input())
    list2.append(ele)
a1 = len(list1)
a2 = len(list2)
#Whether list are of same length
if a1==a2:
    print("same length")
else:
    print("not same length")
sum1=sum(list1)
sum2=sum(list2)
#whether list sums to same value
if sum1==sum2:
    print("sum to same value")
else:
    print("sum is not same")
#whether any value occur in both
for x in list1:
    for y in list2:
        if x==y :
        print("same value occur")
print("not sme values")