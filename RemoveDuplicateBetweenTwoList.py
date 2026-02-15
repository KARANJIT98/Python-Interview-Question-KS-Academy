# Problem Statement:
# Write a Python function that takes two lists as input and returns a new list containing elements that are unique to each list (i.e., elements that appear in one list but not both).

# Input
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]

# Output:
# [1,2,5,6]


def func(l1,l2):
    print("using basics fundamentals")
    l3=[]
    for i in l1:
        if i not in l2:
            l3.append(i)

    for i in l2:
        if i not in l1:
            l3.append(i)

    print(l3)

def func(l1,l2):
    print("using list comprehension")
    l3=[i for i in l1 if i not in l2]+[j for j in l2 if j not in l1]
    print(l3)


func([1,2,3,4],[3,4,5,6])