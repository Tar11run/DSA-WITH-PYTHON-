def insertion_sort(l):
    for i in range(1,len(l)):
        pivot=l[i]
        j=i-1
        while j>=0 and l[j]>pivot:
            l[j+1]=l[j]
            j-=1
        l[j+1]=pivot 
        
l=[4,1,2,5,7]
insertion_sort(l)
print(l)