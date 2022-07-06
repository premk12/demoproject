# #fibonacci series:-
#
# num = int(input("Enter any number: "))
# n1 = 0
# n2 = 1
# count=0
#
# print("Fibonacci series of given number:-")
# while count < num:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count+=1

# #factorial:-
#
# num = int(input("Enter any Number : "))
# fact = 1
#
# for i in range(1,num+1):
#     fact = fact * i
#
# print(f"Fcatorial of {num} is {fact}")

# #sum of digits from string:-
#
# str = input("Enter any String which contain digits: ")
# sum = 0
#
# for char in str:
#     if char.isdigit():
#         sum = sum + int(char)
#
# print(f"Sum of digits from string:{sum}")

#count of characters from string:-

# from collections import Counter
#
# str = "         ... Harshit is a good boy ...                  "
#
# print(str.split("r"))
#
# print(Counter(str))