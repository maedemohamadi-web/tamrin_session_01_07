number=None 
odd_nums=[]
even_nums=[]
odd_sum=0
even_sum=0

while number!=0:
    number=int(input("Enter a number:"))
    if number%2==0:
        even_nums.append(number)
        even_sum+=number
    else:
        odd_nums.append(number)
        odd_sum+=number

print("__________________________________")
print("Even Numbers=",even_nums)
print("Odd Numbers=",odd_nums)
print("__________________________________")
print("Even Sum=",even_sum)
print("Odd Sum=",odd_sum)
