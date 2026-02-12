'''
    Concatenate the below 2 strings
    List1 = ['W', 'a', 'w','c']
    List2 = ['e', 're','riting','ode']

    output= We are writing code

hint :-
list comprehension /dictionary comprehension
zip()
'''

def func(l1,l2):
    return [x+y for  x,y in zip(l1,l2)]

list1 = ['W', 'a', 'w', 'c']
list2 = ['e', 're', 'riting', 'ode']

print(func(list1,list2))

print("converting list to String  ")
list3=func(list1,list2)

str1=" ".join(list3)
print(str1)
