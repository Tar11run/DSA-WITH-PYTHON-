def bubble_sort(l):
    for i in range(len(l)):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
l=[5,3,1,2,4]
bubble_sort(l)
print(l)