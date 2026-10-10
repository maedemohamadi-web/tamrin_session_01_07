odd_sum=0
even_sum=0

num=None
while num!=0:
    num=int(input("Enter a number:"))
    if num!=0:
        if num%2==0:
            even_sum+=num
        else:
            odd_sum+=num

print("Even Sum=",even_sum)
print("Odd Sum=",odd_sum)
