class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

class Singly_LL_Queue:
    def __init__(self):
        self.head=None
        self.size=0
        
    def enqueue(self,val):
        
        new=node(val)
        if self.size==5:
            print("list overflow")
            return
        if self.head is None:
            self.head=new
            self.size+=1
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new
            self.size+=1
            
    def dequeue(self):
         if self.size==0:
             print("list underflow")
             return
         if self.head is None:
             return None
         temp=self.head
         self.head=temp.next
         temp=None
         self.size-=1
         
         
      
    def show(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print(None)
    
listt=Singly_LL_Queue()   
l=[10,20,30,40,50]    
for i in l:
    listt.enqueue(i)
listt.dequeue()
listt.show()