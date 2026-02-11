#list comprehension


li=[1,2,3,4,5,6,7,8]

# li2=[] # even value ko hi add krna chhta hu
#
#
# for i in li:
#     if i%2==0:
#         li2.append(i)
#
# print(li2)

#################################################################################

print("this is done by list comprehension")
li3=[i for i in li if i%2==0]
print(li3)

##################################################################################3
print("this is done by dictionary comprehension ")
dic1={i:i*2 for i in li if i%2==0}
print(dic1)