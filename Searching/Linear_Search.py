def linear_search(l,val):
    for i in range(len(l)):
        if l[i]==val:
            print(i,"is the position")
            break
    if l[i]!=val:
        print("not found")

l=[1,2,3,4,5]
linear_search(l,5)
