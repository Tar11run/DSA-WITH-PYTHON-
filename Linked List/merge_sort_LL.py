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
      
    def show(self):
        temp=self.head
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print(None)
        
    def sort(self,head):
        if head is None or head.next is None:
            return head
        mid=self.middle(head)
        next_middle=mid.next
        mid.next=None
        left=self.sort(head)
        right=self.sort(next_middle)
        sorted=self.merge(left,right)
        return sorted
        
    def middle(self,head):
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
        
    def merge(self,left,right):
        if left is None:
            return right
        if right is None:
            return left
        if left.data<right.data:
            result=left
            result.next=self.merge(left.next,right)
        else:
            result=right
            result.next=self.merge(left,right.next)
        return result
        
    
listt=singly_LL()   
l=[50,40,30,20,10]    
for i in l:
    listt.add(i)
listt.head=listt.sort(listt.head)
listt.show()

