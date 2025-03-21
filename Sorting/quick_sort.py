def quick_sort(l,low,high):
    if low<high:
        pi=partition(l,low,high)
        quick_sort(l,low,pi-1)
        quick_sort(l,pi+1,high)
def partition(l,low,high):
    pivot=l[high]
    i=low-1
    for j in range(low,high):
        if l[j]<pivot:
            i+=1
            l[i],l[j]=l[j],l[i]
    l[i+1],l[high]=l[high],l[i+1]
    return i+1
    
l=[5,1,3,2,6]
quick_sort(l,0,len(l)-1)
print(l)