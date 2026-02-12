#common element in List
#
# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
#
#output=[3,4]
#Hints: Intersection / list Comprehension


#basic method
def func(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3

#using list comprehension
def funcUsingListComprehension(l1,l2):
    return [ i for i in l1 if i in l2]


def funcUsingIntersection(l1,l2):
    return list(set(l1) & set(l2))  #l1=[1,2,3,3,4,5] -> [1,2,3,4,5] l2=[3,4,5,6,2,3] -> [3,4,5,6,2]

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

print(func(list1,list2))

print("Using List Comprehension")
print(funcUsingListComprehension(list1,list2))
print("using Intersection")
print(funcUsingIntersection(list1,list2))