#baki chhe
import random
lst1 = []
for i in range(0,20):
    x=random.randint(1,100)
    lst1.append(x)

a = int(input("enter number you want to find in list:"))
for i in range(0,20):
    if (lst1[i] == a):
        print(i,"value found")
    else:
        print("value not found")
