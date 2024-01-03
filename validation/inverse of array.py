# 1. You are given a number n, representing the size of array a.
# 2. You are given n numbers, representing elements of array a.
# 3. You are required to calculate the inverse of array a.


number_of_elements=int(input("Size of list: "))
list=[]
for i in range(number_of_elements):
    element=int(input(f"Enter value of {i} index position element: "))
    list.append(element)
print(list)

inverse_list=[]
for j in range(number_of_elements):
    if j in list:
        index_position=list.index(j)
        inverse_list.append(index_position)

print(inverse_list)

