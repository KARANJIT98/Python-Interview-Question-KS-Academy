# Problem Statement:
# Write a Python function that takes a string as input and returns the first non-repeating character.
# - If all characters repeat, return an empty string or a suitable message.
# - Treat uppercase and lowercase letters as distinct (e.g., A ≠ a).

# Input:
# s = "aabbccde"
#output:
#   d


def func(str1):

    for i in str1: #a,a,b,b,c,c,d,e
        count=0
        for j in str1:
            if  i==j:
               count+=1
        if count ==1:
            return i
        # print(f"{i}:{count}")





s = "aabbccde"
print(func(s))