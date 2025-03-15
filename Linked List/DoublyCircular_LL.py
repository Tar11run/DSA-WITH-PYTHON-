class node:
    def __init__(self,data):
        self.pre=None
        self.data=data      
        self.next=None

class DoublyCircular_LL:
    def __init__(self):   
        self.head=None
        
    def add(self,val):
        new=node(val)
        if self.head is None:
            self.head=new
            new.next=self.head
            new.pre=self.head
        else:
            temp=self.head.pre
            temp.next=new
            new.pre=temp
            new.next=self.head
            self.head.pre=new
            
    def delete(self,val):
         if self.head is None:
             print("empty")
             return
        
         temp=self.head
         if temp.next==self.head:
             self.head=None
             return
         if temp.data==val:
             self.head=temp.next
             self.head.pre=temp.pre
             temp.pre.next=self.head
             temp=None
             return 
         while True and temp.data!=val:
             p=temp
             temp=temp.next
             if temp==self.head:
                 break
         if temp==self.head:
              print("element to delete not found")
              return 
         p.next=temp.next
         temp.next.pre=p
         temp=None
         
    def add_after(self,after,val):
         if self.head is None:
             return
         new=node(val)
         temp=self.head
         while True and temp.data!=after:
             temp=temp.next
             if temp==self.head:
                 break
         if temp == self.head:
              print("element after which to insert not found")
              return 
         if temp.next==self.head:
             self.add(val)
             return
         
         new.next=temp.next
         temp.next.pre=new
         new.pre=temp
         temp.next=new
      
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
    
listt=DoublyCircular_LL()   
l=[10,20,30,40,50]    
for i in l:
    listt.add(i)
listt.delete(10)

listt.add_after(50,35)
listt.show_reverse()