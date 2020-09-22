var = int(input("Enter a number: "))
count=0
while(var>0):
    count=count+1
    var=var//10

print("Number of digits = ",count)