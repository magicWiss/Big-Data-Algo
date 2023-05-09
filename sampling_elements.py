import random
import matplotlib.pyplot as plt
def prep_elements(max_number_of_elements):
    
    majority_elements=1
    minority_elements=[0,2,5,6,7]
    min_index=0
    max_index=len(minority_elements)-1

    majority_thershold=int((max_number_of_elements/2))+1
    elements=[majority_elements]*majority_thershold

    minority_threshold=int(max_number_of_elements/2)-1
    for i in range (0,minority_threshold):
        index=random.randint(min_index,max_index)
        elements.append(minority_elements[index])

    random.shuffle(elements)
    return elements

def create_sample(sample_size,stream):
    sample=[]
    i=0
    for i in range (0,len(stream)):
        if i<sample_size:
            sample.append(stream[i])
        
        else:
            d=random.randint(0,i)
            if d<sample_size:
                
                sample[d]=stream[i]
                


    return sample

from collections import Counter

def get_stats(elements):
    N=len(elements)
    coutner=Counter(elements)
    
    for k in coutner.keys():
        coutner[k]=coutner[k]/N*100
    
    print(coutner)


if __name__=='__main__':
    max_number_of_elements=1000
    elements=prep_elements(max_number_of_elements)
    stats=get_stats(elements)
    sample_size=int(0.1*(max_number_of_elements))
    sample=create_sample(sample_size,elements)
    stats=get_stats(sample)
    


    #si nota che la poporzione di elementi nello stram iniziale è molto simile a quella presente nel sample