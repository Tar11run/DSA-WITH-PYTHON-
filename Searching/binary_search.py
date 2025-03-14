def binary_search(l,low,high,val):
    global found
    found=False
    while low<=high:
        mid=(low+high)//2
        if l[mid]==val:
            print(mid,"is the position ")
            
            found=True
            break
        elif l[mid]>val:
            high=mid-1
        elif l[mid]<val:
            low=mid+1
    
    if found:
            pass
    else:
            print("not found")
            
l=[1,2,3,4,5]
binary_search(l,0,len(l)-1,5)
            
        