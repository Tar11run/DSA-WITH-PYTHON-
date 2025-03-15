class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class singly_LL:
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
            
    def delete(self,val):
         if self.head is None:
             return None
         temp=self.head
         if temp.data==val:
             self.head=temp.next
             temp=None
             return 
         while temp and temp.data!=val:
             pre=temp
             temp=temp.next
         if temp==None:
              print("element to delete not found")
              return 
         pre.next=temp.next
         temp=None
         
    def add_after(self,after,val):
         new=node(val)
         temp=self.head
         while temp and temp.data!=after:
             temp=temp.next
         if temp==None:
              print("element after which to insert not found")
              return 
         new.next=temp.next
         temp.next=new
      
    def show(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print(None)
    
listt=singly_LL()   
l=[10,20,30,40,50]    
for i in l:
    listt.add(i)
listt.delete(40)
listt.add_after(30,35)
listt.show()
