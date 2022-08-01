user_response=int(input("Enter n: "))
a=2
b=9
#Declare one variable equal to 0 in loop in order to save the sum of values 
count=0
for i in range (1,user_response+1):
    if i%2 ==0:
        n=-1
    else:
        n=1
    count=count+n*a/b
    a+=3
    b+=4
print("The answer is",count)
    