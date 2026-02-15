'''
Question:
Write a Python function that takes a string as input and counts the number of vowels (a, e, i, o, u) present in it. Print the total count of vowels in the format:
Vowel Count <number>
Example:
Input: "Karnajit singh"
Output: Vowel Count 4


Hint:
- Use a loop to iterate through each character.
- Check if the character is in the list of vowels.
- Keep a counter to track the total.
'''

def func(str1):
    count=0
    vowel=['a','e','i','o','u']

    for i in str1:
        # print(i)#Ks Academy  -> k,s, ,a,c,a,d,e,m,y
        if i.lower() not in vowel:
            count+=1

    return count





print(func("Ks Academy"))