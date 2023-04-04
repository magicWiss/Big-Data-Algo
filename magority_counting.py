import random
import matplotlib.pyplot as plt

def prepare_elements(max_number_of_elements):
    
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

def reservois_algo(stream):
    c=0
    m=None
    operations=[]
    for i in stream:
        if c==0:
            m=i
            c+=1
            
        else:
            if m==i:
                c+=1
            else:
                c-=1
        operations.append(c)
    return (c,m,operations)

def prepare_false_elements(max_number_of_elements):
    tokens=[0,1,2,3,4,5,6]
    min_index=0
    elements=[]
    max_index=len(tokens)-1
    for i in range(0,max_number_of_elements):
        index=random.randint(0,max_index)
        elements.append(tokens[index])

    return elements



if __name__=='__main__':
    max_number_of_elements=1000
    #stream buono

    #elements=prepare_elements(max_number_of_elements)
    #stream cattivo
    elements=prepare_false_elements(max_number_of_elements)
    majority_element=reservois_algo(elements)

    element=majority_element[1]
    counter=majority_element[0]
    operations=majority_element[2]
    print("Element with majority:",element)
    print("Occor:",counter)

    progressive_elements=[x for x in range(0,max_number_of_elements)]

    plt.plot(progressive_elements, operations)
    plt.xlabel('elementi_stream')
    plt.ylabel('andamento_contatore')
    plt.show()


    


