#You are required to print the Greatest Common Divisor (GCD) of two numbers.
# You are also required to print the Lowest Common Multiple (LCM) of the same numbers.
# Take input "num1" and "num2" as the two numbers.
# Print their GCD and LCM.

def compute_gcd(x,y):
   
    if x==0 or y==0:
        return None
    else:
        while(y):
            x,y=y,x%y
        print("GCD of the numbers is: ",x)
        return x
    


def compute_lcm(x,y):
    try:
        get_gcd=compute_gcd(x,y)
        lcm=(x*y)//get_gcd
        if get_gcd!=None:
            return lcm
    
    except Exception as e:
        response="For value GCD and LCM can't be determined"
        return response
    

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
get_lcm=compute_lcm(num1,num2)

print("LCM is: ",get_lcm)


