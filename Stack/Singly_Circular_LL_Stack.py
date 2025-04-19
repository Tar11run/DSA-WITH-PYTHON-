class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

class SinglyCircular_LL_Stack:
    def __init__(self):
        self.head=None
        self.size=0
        
    def push(self,val):
        
        new=node(val)
        if self.size==5:
            print("list overflow")
            return
        if self.head is None:
            self.head=new
            new.next=self.head
            self.size+=1
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new
            new.next=self.head
            self.size+=1
            
    def pop(self):
         if self.size==0:
             print("list underflow")
             return
         if self.head is None:
             return None
         if self.head.next is self.head:
         	self.head=None
         	self.size-=1
         	return
        
         temp=self.head
         while temp.next!=self.head:
         	pre=temp
         	temp=temp.next
         pre.next=temp.next
         temp=None
         	
         self.size-=1
         
      
    def show(self):
        temp=self.head
        while True:
            print(temp.data,end=" -> ")
            temp=temp.next
            if temp==self.head:
            	break
            
        print(None)
    
listt=SinglyCircular_LL_Stack()   
l=[10,20,30,40,50,60]    
for i in l:
    listt.push(i)
listt.pop()

listt.show()