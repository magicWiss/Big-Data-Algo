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
                print('Old value:',sample[d])
                print('New val:',stream[d])
                sample[d]=stream[i]
                print('Inserito elemento in sample in pos ',d)


    return sample
if __name__=='__main__':
    max_number_of_elements=1000
    elements=prep_elements(max_number_of_elements)

    sample_size=int(0.1*(max_number_of_elements))
    sample=create_sample(sample_size,elements)

    print(sample)