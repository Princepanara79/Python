s1 = {'adtiya', 'ame', 'bhide', 'bhavya', 'ashit', 'bunty'}
s2 = set()
s3 = set()
for ele in s1:
    if ele[0] == 'a':
        s2.add(ele)
    else:
        s3.add(ele)
print(s2)
print(s3)
