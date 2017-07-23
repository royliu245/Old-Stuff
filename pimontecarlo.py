import random

def mcpi(n):
    count = 0
    for i in range(n):
        x = random.uniform(-1,1),random.uniform(-1,1)
        if(((x[0]**2)+(x[1]**2))<1):
            count += 1
    print((count/n)*4)

