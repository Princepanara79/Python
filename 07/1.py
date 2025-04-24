#lst1 = ['hitarth', 'prince', 'het']
#lst2 = []
#for ele in lst1:
#    lst2.append(ele.upper())
#s1 = set(lst2)
#print(s1)
str1 = input("enter space seprated names:")
print(set(str1.upper().split()))
