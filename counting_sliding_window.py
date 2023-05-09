class Bucket:
    def __init__(self):
        self.timestamp=0
        self.number_of_ones=1
    
    def update(self, bucket_new):
        self.timestamp=bucket_new.timestamp
        self.number_of_ones+=bucket_new.number_of_ones

    def print_stats(self):
        print('Bucket')
        print('Number elements:',self.number_of_ones)
        print('Timestap:',self.timestamp)
    

class ListBukets:
    def __init__(self, N):
        self.set_of_buckets=dict()
        #ogni entry puo avere al massimo 2 elementi nell'array
        self.set_of_buckets={0:[],1:[],2:[],3:[],4:[]}

        self.LIMIT=N
    
    def update_timestamps(self):
        for k in self.set_of_buckets.keys():
            buckets=self.set_of_buckets[k]
            for b in buckets:
                b.timestamp+=1

                if b.timestamp>self.LIMIT:
                    self.set_of_buckets[k].pop(len(self.set_of_buckets[k])-1)
                
    def update_bukcets(self):

        for k in self.set_of_buckets.keys():
            dim_bukets=len(self.set_of_buckets[k])
            if dim_bukets>2:
                if k+1 in self.set_of_buckets:
                    self.set_of_buckets[k][1].update(self.set_of_buckets[k][2])
        
                


    def inset_element(self,x):
        self.update_timestamps()
        if x==0:
            return
        
        else:
            bucket_new=Bucket()

            self.set_of_buckets[0].append(bucket_new)
            self.update_bukcets()

        
    
    def get_number_of_one(self):
        sum=0
        for k in self.set_of_buckets.keys():
            if k==max(self.set_of_buckets.keys()) and (len(self.set_of_buckets[k])!=0):
                old_element=self.set_of_buckets[k][len(self.set_of_buckets)-1]
                if old_element.number_of_ones+old_element.timestamp>self.N:
                    sum=sum+old_element.number_of_ones/2
            for e in self.set_of_buckets[k]:
                sum=sum+e.number_of_ones

        return sum
    

    def print_state(self):
        for k in self.set_of_buckets.keys():
            for e in self.set_of_buckets[k]:
                e.print_stats()
    
import random
if __name__=='__main__':

    create_stream_0=[0]*5000
    create_stream_1=[1]*30002
    stream=create_stream_0+create_stream_1
    
    random.shuffle(stream)
    sum_true=0
    buckets=ListBukets(N=1000)
    n=1000
    for i in range(0,n):
        if stream[i]==1:
            sum_true+=1
        
    print(sum_true)
        

    for i in stream:
        buckets.inset_element(i)

    sum=buckets.get_number_of_one()
    print(sum)

    buckets.print_state()

    



