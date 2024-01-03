# #You are required to display the prime factorization of a number.
# Take as input a number n.
# Print all its prime factors from smallest to largest.


# num=100
# factors=[]
# for i in range(1,num+1):
#     if num%i==0:
#         factors.append(i)
    

# factors.remove(factors[0])
# print(factors)

# prime_factors=[]

# for j in factors:
#     for k in range(1,max(factors)+1):
#         if k%j==0 and k<=j:
#             if j==2:
#                 prime_factors.append(k)
#             elif (j>2 and j%2!=0):
#                 prime_factors.append(k)


# print(prime_factors)



# Function definition to get all prime factors
def get_prime_numbers(num):
    i=2
    while i*i<=num:
        if num%i==0:
            prime_factors.append(i)
            num//=i
        else:
            i+=1
    if num>1:
        prime_factors.append(num)

    return prime_factors

num=10003
prime_factors=[]
prime_numbers=get_prime_numbers(num)

final_list=list(set(prime_factors))
final_list.sort()
print(final_list)



