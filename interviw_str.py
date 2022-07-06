# ##Python Program to Print Hello world!
#
# print("Print Hello world!")
#
# ##Python Program to Add Two Numbers
#
# a=5
# b=9
# print("addition of a and b:",a+b)
#
# # ##Python Program to Find the Square Root
# #
# num=10
#
# num_sqr=num**0.5
#
# print("Square root of 10:",num_sqr)
#
# # ##Python Program to Calculate the Area of a Triangle
# #
# a=10
# b=5
# c=6
#
# # calculate the semi-perimeter
# s = (a + b + c) / 2
#
# # calculate the area
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#
# print("Area of triangle",area)
#
# # ##Python Program to Swap Two Variables
# #1st way
# x=10
# y=8
#
# temp=x
#
# x=y
#
# y=temp
#
# print("value of x",x)
# print("value of y",y)
# #2nd way
# a=10
# b=5
# a,b=b,a
#
# print(f"a:{a}")
# print(f"b:{b}")
#
#
#
# # ##Python Program to Generate a Random Number
# #
# import random
# print(random.randint(0,9))
#
# # ##Python Program to Convert Kilometers to Miles
# #
# kilometers = 10
#
# ##conversion factor km to miles
# conv_fac = 0.621371
#
# # calculate miles
# miles = kilometers * conv_fac
#
# print("miles is of 10km:",miles)
#
# ##Python Program to Convert Celsius To Fahrenheit
#
# celsius = 37.5
#
# # calculate fahrenheit
# fahrenheit = (celsius * 1.8) + 32
#
# print("celsius",fahrenheit)
#
#
# # ##Python Program to Check if a Number is Positive, Negative or 0
# #
# num = -1
# if num > 0:
#    print("Positive number")
# elif num == 0:
#    print("Zero")
# else:
#    print("Negative number")
#
# # ##Python Program to Check if a Number is Odd or Even
#
# num = 10
# if (num % 2) == 0:
#    print("{0} is Even".format(num))
# else:
#    print("{0} is Odd".format(num))
#
#
# ##Python Program to Check Leap Year
#year=2012
# divided by 100 means century year (ending with 00)
# century year divided by 400 is leap year
# if (year % 400 == 0):
#     print("{0} is a leap year".format(year))
#
# # not divided by 100 means not a century year
# # year divided by 4 is a leap year
# elif (year % 4 ==0) :
#     print("{0} is a leap year".format(year))
# # #
# # # if not divided by both 400 (century year) and 4 (not century year)
# # # year is not leap year
# else:
#     print("{0} is not a leap year".format(year))
# #
# # ##Python Program to Check Prime Number
# #
# num = 5
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#
#             break
#     else:
#         print(num, "is a prime number")
#
# else:
#     print(num, "is not a prime number")
#
# ##Python Program to Print all Prime Numbers in an Interval
# num1=100
# num2=200
#
# for number in range(num1, num2 ):
#    # all prime numbers are greater than 1
#    if number > 1:
#        for i in range(2, number):
#            if (number % i) == 0:
#                break
#        else:
#            print(number)
#
#
# # ##How to find factorial of number
# #FOR loop
# num=5
#
# fact=1
#
# for i in range(1,num+1):
#     fact=fact*i
# print((f"factorial of {num} is {fact}"))

##while loop

# num=5
# i=1
# fact=1
#
# while i<=num:
#     fact=fact*i
#     i=i+1
# print(f"factorial of {num} is :{fact}")



# # ##Python Program to Print the Fibonacci sequence
#
# num=8
# n1=0
# n2=1
# count=0
#
# print(f"fibbonacci series:{num}")
# while count<num:
#     print(n1)
#     nth=n1+n2
#     n1=n2
#     n2=nth
#     count+=1
# #
# # ##How to find the sum of element in an array
# #
# import array
#
# element=array.array('i',[5,10,6,8])
#
# sum=sum(element)
#
# print(sum)
#
# ## How to find length of list
#
# list=[2,3,"prem",8,1.1,True,False]
#
# print(len(list))
#
# ##How to swap first and last element in the list
#
# list=[1,2,5,8,9]
#
# a=len(list)-1
#
# list[0],list[a]=list[a],list[0]
#
# print(f"After swipiing :,{list}")
#
# # ##How to swap any two number from list
# # ##1st way
# list=[1,2,5,8,9]
#
# a=(int(input("insert 1st value="))-1)
# b=(int(input("insert 2nd value="))-1)
#
# list[a],list[b]=list[b],list[a]
#
# print(f"After swipiing :,{list}")
#
# # # ##2nd way
# #
# a=int(input("insert 1st value="))
# b=int(input("insert 2nd value="))
#
# list[a-1],list[b-1]=list[b-1],list[a-1]
#
# print(f"After swipiing :,{list}")
#
# ##How to remove nth occurance of a given word list
#
# list=["he","she","my","love","how","where","prem"]
#
# a=(int(input("Enter remove value= "))-1)
#
# remove=list.pop(a)
#
# print(f"removed value=,{remove}")
#
# print(f"After removing{a} value=,{list}")
#
# ##How to search an element in the list
#
# list=["prem","my","pratima","shital"]
#
# print(list)
#
# element=input("Enter element which you want to find=")
#
# index=list.index(element)
#
# print(f"Index position of {index} element is:",index)
#
# ##Python Program to Find the Largest Among Three Numbers
#
# num1=int(input("enter 1st value="))
# num2=int(input("enter 2st value="))
# num3=int(input("enter 3st value="))
# num4=int(input("enter 4st value="))
#
# if (num1>=num2) and (num1>=num3) and (num1>=num4):
#     largest=num1
# elif (num2>=num1) and (num2>=num3) and (num2>=num4):
#     largest=num2
# elif(num3>=num1) and (num3>=num2) and (num3>=num4):
#     largest=num3
# else:
#     largest=num4
#
# print("Largest number is=",largest)
#
#
# ##How clear the list
#
# list=[1,2,3,4,5,6]
#
# list.clear()   ##By clear
#
# print(list)
#
# ##How to reverse list
# list=[1,2,3,4,5,6]
#
# list.reverse()
#
# print(list)
#
# ##How to copy or clone list
#
# list=["my","name","is","nita"]
#
# list2=[]
#
# list2=list.copy()
#
# print("old list =",list)
# print("new list created=",list2)
# #
# # ##How to count occurences of an element in a list
# #
# list=[1,1,1,5,5,4,4,2,5,6,9,8,7,5,2]
#
# print(list)
#
# element=int(input("Enter the element that you want to count:"))
#
# print(list.count(element))
# #
# # ##How the sum of the elementsin list
# #
# list=[1,1,4,4,5,6,4,6,4,6]
#
# sum=sum(list)
#
# print("Sum of list=",sum)
#
# ##How to find maximum and minimum element in an array
# import array
# array=array.array('i',[1,2,3,4,5,2,1,7,8])
#
# print(type(array))
#
# max=max(array)
# min=min(array)
#
#
# print(f"max of aaray={max}")
# print(f"min of array={min}")
#
# # ##How to multiply all numbers of list
# #
# list=[1,2,8,9]
#
# len=1
# for i in list:
#     len=len*i
# print(f"Multiplication of all the list element:",len)
#
# ##How to find smallest and largest numbers on the list
#
# list=[1,2,5,4,6,9]
#
# max=max(list)
# min=min(list)
#
# print(f"largest number:{max}")
# print(f"smallest number:{min}")
#
# ##How to find second largest number in alist
#
# list1=[1,4,5,6,6,3,2]
#
# setcon=set(list1) ## convert list into set bcs unique
#
# listcon=list(setcon)  #convert into list
#
# print(listcon)
#
# listcon.sort() ## asending and decending
# #
# print("second largest:",listcon[-2])
#
# ##How to check string is palinderome or not
#
# element=input("Enter string :")
#
# if element ==(element[::-1]):
#     print("The given string palinderome")
#
# else:
#     print("The given string is not palindrome")
#
#
# ##How to reverse words in a string
#
# name=input("Enter string ")
#
# revers=name[::-1]
#
# print(f"After reverse:",revers)
#
# #How to find substring in a string
#
# str= "prem_ramesh_katre"
#
# result=(str.find("katre",0))
#
# print(result)

# ##How to find length of string
# str="prem katre"
#
# length=len(str)
#
# print("length of string",length)
#
# ##how to find special characters
#
# import re
#
# str=input("Enter string:")
#
# var=re.compile('[~!@#$%^&*()]')
#
# if var.search(str)==None:
#     print(("No special character in string"))
#
# else:
#     print("string has special characters")
#
# ##Python Program to Display the multiplication Table
#
# num = 2
#
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)
#
# ##Python Program to Display Calendar
#
# import calendar
#
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))
#
# # display the calendar
# print(calendar.month(yy, mm))
#
# ##Python Program to Remove Duplicate Element From a List
#
# list1=[1,5,6,6,8,8,9]
#
# setcon=(set(list1))
#
# listcon=(list(setcon))
#
# print("After convertion:",listcon)
#
# ##Python Program to Capitalize the First Character of a String
#
# my_string = "programiz is Lit"
#
# print(my_string.capitalize())

##Frequency of each character in String/count of occurance

# from collections import Counter
#
# string = "premkatre"
#
# res = Counter(string)
#
# print("Count of all characters in string is :\n ",(res))

##How to count digit from string

# value=input("Enter string which contain digit:")
#
# sum=0
#
# for x in value:
#     if x.isdigit():
#         sum=sum+int(x)
# print("Addition of string digit",sum)

##Remove Duplicates from a list without change sequence

# list1=[40,20,60,10,5,40,80]
#
# print("the list is:",list1)
#
# result=[]
# for i in list1:
#     if i not in result:
#         result.append(i)
# print(result)

#2nd way
# from collections import OrderedDict
#
# result=list(OrderedDict.fromkeys(list1))
#
# print(result)





















































