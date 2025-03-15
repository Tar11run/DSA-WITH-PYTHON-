class node:
    def __init__(self,data):
        self.pre=None
        self.data=data      
        self.next=None

class doubly_LL:
    def __init__(self):   
        self.head=None
        
    def add(self,val):
        new=node(val)
        if self.head is None:
            self.head=new
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new
            new.pre=temp
            
    def delete(self,val):
         if self.head is None:
             print("empty")
             return
         if self.head.next is None:
             self.head=None
             return 
         temp=self.head
         if temp.data==val:
             self.head=temp.next
             self.head.pre=None
             temp=None
         while temp and temp.data!=val:
             p=temp
             temp=temp.next
         if temp is None:
              print("element to delete not found")
              return 
         if temp.next is None:
             p.next=temp.next
             temp=None
             return
         p.next=temp.next
         temp.next.pre=p
         temp=None
         
    def add_after(self,after,val):
         new=node(val)
         temp=self.head
         while temp and temp.data!=after:
             temp=temp.next
         if temp is None:
              print("element after which to insert not found")
              return 
         if temp.next is None:
             self.add(val)
             return
         
         new.next=temp.next
         temp.next.pre=new
         new.pre=temp
         temp.next=new
      
    def show_reverse(self):
        if self.head is None:
            return
        print(None,end=" -> ")
        temp=self.head
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.pre
    
listt=doubly_LL()   
l=[10,20,30,40,50]    
for i in l:
    listt.add(i)
listt.delete(50)

listt.add_after(30,35)
listt.show_reverse()