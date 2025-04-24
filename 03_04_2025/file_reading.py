f = open("C:\\Users\\lab\\Desktop\\Prince058_CSV.csv",'r')
#content = f.readlines()
#print(content)
i=0
while(i<3):
    cont = f.readline()
    print(cont)
    i+=1
f.close()
