s='aabbba'
a_last_index=s.rfind('a')
b_last_index=s.rfind('b')

if s=='a' or s=='b':
    print(True)
else:
    if a_last_index==-1 or b_last_index==-1:
        print(True)
    else:
        if b_last_index>a_last_index:
            print(True)
        else:
            print(False)

# num=int(input('Enter a number: '))
a = lambda x,y : x*y
print(a(7,19))


# current_time=str(datetime.today())
# print(current_time)

def palindrome(s):
    s=s.lower()
    s=s.replace(" ","")
    if s==s[::-1]:
        value=print(True)
    else:
        value=print(False)
    return value
s='abcba'
palindrome(s)
