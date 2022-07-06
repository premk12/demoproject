import array
element=array.array('i',[200,300,800])

print(element[2])

print(type(element))

print(element[0])


# element=array.array('i',[5,10,6,8])
#
# sum=sum(element)
#
# print(sum)


element=array.array('i',[5,True,6,8])

sum=sum(element)###True=1

print(sum)  ###output=20