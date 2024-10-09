# recursion function
# # write a recursive function to calculate the sum of first n natural numbers.
# def cal_sum(n):
#     if(n==0):
#         return 0
#     # print(n)
#     return cal_sum(n-1) + n
    
# sum = cal_sum(10)
# print(sum)

# write a recursive function to print all element in a list
# hint : use list & index as parameter.

def print_list(list,index=0):
    if(index == len(list)):
        return
    print(list[index])
    print_list(list,index+1)
    
fruits = ['mango','apple','banana','cherry','blackberry']
print_list(fruits)