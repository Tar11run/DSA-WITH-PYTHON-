class node:
    def __init__(self,data):
        self.pre=None
        self.data=data      
        self.next=None

class DoublyCircular_LL_Stack:
    def __init__(self):   
        self.head=None
        self.size=0
        
    def push(self,val):
        if self.size==5:
            print("Stack Overflow")
            return 
        new=node(val)
        if self.head is None:
            self.head=new
            new.next=self.head
            new.pre=self.head
            self.size+=1
        else:
            temp=self.head.pre
            temp.next=new
            new.pre=temp
            new.next=self.head
            self.head.pre=new
            self.size+=1
            
    def pop(self):
         if self.size==0:
             print("Stack Underflow")
         if self.head is None:
             print("empty")
             return
         if self.head.next==self.head:
             self.head=None
             self.size-=1
             return
         temp=self.head
         while temp.next!=self.head:
             p=temp
             temp=temp.next
         p.next=temp.next
         temp.next.pre=p
         temp=None
         self.size-=1
          
      
    def show_reverse(self):
        if self.head is None:
            return
        print("Head",end=" <-> ")
        temp=self.head.pre
        while True:
            print(temp.data,end=" <-> ")
            temp=temp.pre
            if temp==self.head.pre:
                break
            
        print("Head")
    
listt=DoublyCircular_LL_Stack()   
l=[10,20,30,40,50]    
for i in l:
    listt.push(i)
listt.pop()

listt.show_reverse()