class Queue:
    def __init__(self,size):
        self.items=[]
        self.size=size
        
    def enqueue(self,val):
        if len(self.items)==self.size:
            print("Queue Overflow")
        else:
            self.items+=[val]
           
    def dequeue(self):
        if len(self.items)==0:
            print("Queue Underflow")
        else:
            self.items=self.items[1:]
            
    def show(self):
            for j in range(0,len(self.items)):
                print(self.items[j],end=" ")
            
            
q=Queue(5)
l=[10,20,30,40,50]
for i in l:
        q.enqueue(i)
q.dequeue()
q.show()
        
        
        
