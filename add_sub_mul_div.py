def cal_sum(a,b):
    add = a + b
    return add

def cal_sub(a,b):
    sub = a - b
    return sub
    
def cal_mul(a,b):
    mul = a * b
    return mul
    
def cal_div(a,b):
    div = a / b
    return div

choice = int(input("Enter Your Choice : 1. Add 2. Substraction 3. Multipy  4. Divide : "))
first  = int(input("Enter First Number : "))
second  = int(input("Enter Second Number : "))

if(choice == 1):
    print("The sum of two number is ",cal_sum(first,second))
elif(choice == 2):
    print("The substraction of two number is ",cal_sub(first,second))
elif(choice == 3):
    print("The multiply of two number is ",cal_mul(first,second))
elif(choice == 4):
    print("The divide of two number is ",cal_div(first,second))
else:
    print("Invalid Choice")
