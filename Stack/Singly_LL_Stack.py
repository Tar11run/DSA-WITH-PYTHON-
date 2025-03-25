class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

class singly_LL:
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
            self.size+=1
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new
            self.size+=1
            
    def pop(self):
         if self.size==0:
             print("list underflow")
             return
         if self.head is None:
             return None
         temp=self.head
         if self.head.next is None:
             self.head=None
             self.size-=1
             return
         while temp.next:
             pre=temp
             temp=temp.next
         pre.next=None
         temp=None
         self.size-=1
         
      
    def show(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print(None)
    
listt=singly_LL()   
l=[10,20,30,40,50,60,70]    
for i in l:
    listt.push(i)
listt.pop()
listt.show()