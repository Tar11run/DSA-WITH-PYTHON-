class stack:
    def __init__(self,size):
        self.items=[]
        self.size=size
        
    def add(self,val):
        if len(self.items)==self.size:
            print("Stack Overflow")
        else:
            self.items+=[val]
           
    def pop(self):
        if len(self.items)==0:
            print("Stack Underflow")
        else:
            self.items=self.items[:-1]
            
    def show(self):
            for j in range(0,len(self.items)):
                print(self.items[j],end=" ")
            
            
s=stack(5)
l=[10,20,30,40,50]
for i in l:
        s.add(i)
s.pop()
s.show()
        
        
        
