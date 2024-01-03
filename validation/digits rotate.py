# #Given two numbers n and k, we have to rotate the number n by k digits. If k is positive, right rotate the number i.e. remove k rightmost digits and make them leftmost. 
# #Else for negative values of k, left rotate the number, i.e. remove k digits from left and make them rightmost digits.
# #Eg) Rotating 562984 by +2 will give 846529, whereas rotating it by -2 will give 298456.

def convert(final_list):
    res = int("".join(map(str, final_list)))
    return res

def rotating(n,k):
    if k>=0:
        print("k is positive")
        print("length of list",len(list_digits))
        left_out_digits=len(list_digits)-k
        print("left out digits",left_out_digits)
        i=0
        #current_index_list=[]
        elements_to_remove=[]

        for i in range(left_out_digits,len(list_digits)):
            elements_to_remove.append(list_digits[i])
        for i in elements_to_remove:
            list_digits.remove(i)
        final_list=elements_to_remove+list_digits
        print(final_list)
        print(convert(final_list))

    elif k<0:
        print("k is negative")
        k=-k
        print("altering value of k",k)
        elements_to_remove=[]
        for i in range(0,k):
            elements_to_remove.append(list_digits[i])
        for i in elements_to_remove:
            list_digits.remove(i)
        print(list_digits)
        final_list=list_digits+elements_to_remove
        print(final_list)
        
        print(convert(final_list))


n=int(input("Provide value of n: "))
k=int(input("Provide value of k: "))

if n<0:
    n=-n
    list_digits=[int(x) for x in str(n)]
    print(rotating(n,k))
    

elif n>0:
    list_digits=[int(x) for x in str(n)]
    rotating(n,k)
    








 



        
    
    