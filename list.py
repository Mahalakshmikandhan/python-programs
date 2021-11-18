#positive numbers from list
list1=[]
list2=[]
n=int(input("Enter the number of elements in a list: "))
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
print("The list is",list1)
for i in list1:
    if i>0:
        list2.append(i)
print("The positve elements are:")
print(list2)
      
