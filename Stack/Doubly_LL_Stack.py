class node:
    def __init__(self,data):
        self.pre=None
        self.data=data      
        self.next=None

class Doubly_LL_Stack:
    def __init__(self):   
        self.head=None
        self.size=0
        
    def push(self,val):
        if self.size==5:
            print("overflow stack")
            return 
        new=node(val)
        temp=self.head
        if self.head is None:
            self.head=new
        else:
             while temp.next:
                 temp=temp.next
             temp.next=new
             new.pre=temp
        self.size+=1
        
            
    def pop(self):
         if self.size==0:
             print("stack underflow")
             return 
         if self.head is None:
             print("empty")
             return
         if self.head.next is None:
             self.head=None
             self.size-=1
             return
         temp=self.head
         while temp.next:
             p=temp
             temp=temp.next
         p.next=temp.next
         temp=None
         self.size-=1
             
           
      
    def show_reverse(self):
        if self.head is None:
            return
        print(None,end=" <-> ")
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end=" <-> ")
            temp=temp.pre
        print(None)
    
listt=Doubly_LL_Stack()   
l=[10,20,30,40,50,60]  
for i in l:
    listt.push(i)
listt.pop()
listt.show_reverse()