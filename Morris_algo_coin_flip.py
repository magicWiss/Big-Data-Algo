import random
import matplotlib.pyplot as plt
real_count=1000000
epochs=100
stream=[1]*real_count
counter=0
evolution_of_counters=[]
diff_of_counters=[]
sum_counters=0
counter_true=0
for i in stream:
        coin=random.randint(0,1)
        if coin>0.5:
            counter+=1
        else:
            counter=counter
        evolution_of_counters.append(counter)
        counter_true+=1
        diff_of_counters.append(counter_true-counter)
        


elements=list(range(1,real_count+1))


plt.plot(evolution_of_counters, elements)
plt.xlabel('contatore')
plt.ylabel('stream')
plt.show()

plt.plot(diff_of_counters,elements)
plt.xlabel('contatore')
plt.ylabel('stream')
plt.show()

