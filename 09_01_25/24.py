#Swap two values
a = float(input("first enter a:"))
b = float(input("second enter b:"))
#temp = a
#a = b
#b = temp
#print("now a is",a,"and b is",b)

#without extra variable
a = a+b
b = a-b
a = a-b
print("now a is",a,"and b is",b)
