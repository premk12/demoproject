##fibbonaci

num=int(input("enter number"))
n1=0
n2=1
count=1

while count<num:
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1


##factorial
num=int(input("enter number"))
factor=1

for i in range(1,num+1):
    factor=factor*i
print(factor)

##count occurence from string


