str1=input("enter the str1=")
str2=input("enter the str2=")
print(str1.replace(str1[0],str2[0]+'   '+str2.replace(str2[0],str1[0])))