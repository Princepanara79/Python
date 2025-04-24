import random
lst1 = []
while len(lst1)<10:
    num = random.randint(15,45)
    if num not in lst1:
        lst1.append(num)
print(lst1)
s1 = set(lst1)
count = 0
for ele in s1:
    if ele<30:
        count += 1
print(s1)
print("number less than 30 are:", count)
sdemo = {15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34}
s3 = sdemo & s1
print(s3)
        

 
