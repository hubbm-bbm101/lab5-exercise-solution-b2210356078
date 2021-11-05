N = input("please enter a integer x:")
list1=[]
list2=[]
for x in range(1,int(N)+1):
    if x %2!=0:
        list1.append(x)
    else :
        list2.append(x)
print(sum(list1))
print(sum(list2)/len(list2))