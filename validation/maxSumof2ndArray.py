# N=int(input("No. of elements in Array: "))
N=6
A=[3,7,8,2,6,9]
# for i in range(0,N):
#     x=int(input("Element value: "))
#     A.append(x)
# print(A)
A.sort()
num_remove=N//3
for i in range(num_remove):
    A.remove(A[i])
    
print(A)
min(A)
print(min(A))

A.remove(A[1])
B=A
length_of_B=len(B)
