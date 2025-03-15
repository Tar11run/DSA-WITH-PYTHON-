class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyCircular_LL:
    def __init__(self):
        self.head=None
        
    def add(self,val):
        new=node(val)
        if self.head is None:
            self.head=new
            new.next=self.head
        else:
            temp=self.head
            while temp.next!=self.head:
                temp=temp.next
            temp.next=new
            new.next=self.head
            
    def delete(self,val):
         if self.head is None    :
             return None
         temp=self.head
         if temp.data==val:
             self.head=temp.next
             temp=None
             return 
         while True and temp.data!=val:
             pre=temp
             temp=temp.next
             if temp==self.head:
                 break
         if temp==self.head:
              print("element to delete not found")
              return 
         pre.next=temp.next
         temp=None
         
    def add_after(self,after,val):
         new=node(val)
         temp=self.head
         while True and temp.data!=after:
             temp=temp.next
             if temp==self.head:
                 break
             
         if temp==self.head:
              print("element after which to insert not found")
              return 
         new.next=temp.next
         temp.next=new
      
    def show(self):
        print("Head",end=" -> ")
        temp=self.head
        if self.head is None:
            print("list is empty")
            return 
        while True:
            print(temp.data,end=" -> ")
            temp=temp.next
            if temp==self.head:
                break
        print("Head")
    
listt=SinglyCircular_LL()   
l=[10,20,30,40,50]    
for i in l:
    listt.add(i)
listt.delete(40)
listt.add_after(30,35)
listt.show()