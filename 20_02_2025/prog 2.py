import random
st1=set()
while len(st1)<10:
    num=random.randint(15,45)
    st1.add(num)

print(st1)
count = 0
for i in st1:
    if i<30:
        count+=1

s={15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34}
st1=s&st1


print("no less than 30 are: ",count)
print("Final set no less than 35" ,st1)
