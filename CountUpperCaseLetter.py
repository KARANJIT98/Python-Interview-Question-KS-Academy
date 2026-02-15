# Problem Statement:
# Write a Python function that takes a string as input and returns the number of uppercase letters in it.
# - Treat uppercase letters as those recognized by Python’s str.isupper() method.
# - Non-alphabetic characters should be ignored.
#
# Input :
# s = "helloWorld"
# Output:
# 1


def fun(str1):
    count=0
    for i in str1:
        if i.isupper():
            count+=1

    return count


def func(str2):
    for i in str2:
        if i.isupper():
            print(i)
            break

s = "h22641eLloWorld"
print(fun(s))

func(s)