# Longest Word in a String

# Problem Statement:
# Write a Python function that takes a string as input and returns the longest word in the string.
# - If multiple words share the maximum length, return all of them.
# - Ignore leading/trailing spaces.
# - Assume words are separated by spaces only (no punctuation for simplicity).

# Input:-
#    s = "apple banana cherry"
# Output:-
#    banana cherry

def func(str1):

    list1=str1.split(" ")
    # print(list1)

    dic={}  # appple- len(apple),bnanan-len(banana),cherry and so on
    for i in list1:
        dic.update({i:len(i)})

    # print(dic)
    newl=[]
    for key,val in dic.items():
        if val == max(dic.values()):
            # print(key)
            newl.append(key)

    newstr=" ".join(newl)
    print(newstr)


s = "apple banana cherry"
func(s)