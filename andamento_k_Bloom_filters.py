#Bloom filters
#sono costrutti utilizzati per sintetizzare un set S in modo tale da avere una rappresentazione succinta dell'insieme.
#E' composto da un array binario F  di m elementi e k hash function indimendenti che mappano un elemento x ad un intero [0,...m-1]
#Un elemento potrebbe essere presente in S se tutti gli F[h(x)]==1

#NOTA
#Potrebbero esserci casi in cui seppur un elemento x non appartiene a S, il bloom filter lo classifica come appartentne (per via di conflitti)
#SI hanno in questo caso FALSI POSITIVI

#Per alleviare il problema dei falsi Positivi si analizza la probabilità di averne e si minimizza la funzione per k
#PROB_false_neg=(1-1/e^(k*n/M))^k

#Poichè su m vi è un vincolo fisico, si ragiona su k

#possibili k
import math
import matplotlib.pyplot as plt
all_k=list(range(1,10))
m=4000000000
n=500000000

def get_probabilit(k):
    exp=(k*n)/m
    out=(1-1/math.exp(exp))**k
    return out


prob_for_k=[]
for i in all_k:
    prob_for_k.append(get_probabilit(i))

fig=plt.plot(all_k,prob_for_k)
plt.show()

