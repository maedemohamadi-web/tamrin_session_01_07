number_list=[]
count=0
sum=0

for i in range (112,999,14):
    number_list.append(i)
    count+=1
    sum+=i

average=sum/count

print("________________________________________________________________________")
print("Numbers:",number_list)
print("________________________________________________________________________")
print("Average=",average)
