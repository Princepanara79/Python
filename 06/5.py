lst=[(), (13245),('xzcgsdgbdf')]
print(lst)
for i in lst:
    if not i:
        lst.remove(i)
print(lst)