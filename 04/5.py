#Generate all Pythagorean Triplets with side length <= 30.
def check(a):
    while(a<=30):
        for b in range(1,31):
            for c in range(1,31):
                if(a**2 + b**2 == c**2):
                    print(a,b,c)
        a+=1
a = 1
check(a)    