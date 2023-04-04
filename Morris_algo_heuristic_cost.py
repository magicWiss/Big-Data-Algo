import random
import math
import matplotlib as mtp
real_count=100000
epochs=100
stream=[1]*real_count
counter=0
d=0

for i in stream:
        r=random.random()
        d=1/(math.exp(counter+1)-math.exp(counter))
        
        if r>=d:
            counter=counter
        else:
            
            counter+=1



print('Originale value:',real_count)
print('Computed value: ',(math.exp(counter)))