
### find the frequencies of all the characters in that string and
# return a dictionary with key as the character and
# its value as its frequency in the given string.
from collections import Counter
details="Prem katre from tirora he is good boy very hard working boy"

char=Counter(details)

print("count of  accurance of all characters,"+str(char))

#---------------------------------------------------------------------------------------------------------------
# count the occurence of element in the string

# l=input("enter the string")
# d={}
# print(l)
# for i in l:
#  if i not in d:
#   d[i]=l.count(i)
#  else:
#   pass
# print("Frequency of each element-")
#
# for k in d:
#   print(k,"-",d[k])

# --------------------------------------------------------------------------------------------------------------------


