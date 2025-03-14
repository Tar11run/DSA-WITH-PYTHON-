def rec_bin_search(l,start,end,val):
    if start<=end:
        mid=(start+end)//2
        if l[mid]==val:
            return mid
            
        elif l[mid]>val:
            return rec_bin_search(l,start,mid-1,val)
            
        else:
            return rec_bin_search(l,mid+1,end,val)
            
    return -1
 
l=[1,2,3,4,5]                      
index=rec_bin_search(l,0,len(l)-1,4)    
print(index)        