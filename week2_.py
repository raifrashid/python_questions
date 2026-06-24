
#                               Week 2: Functions, Lists, Tuples, Dictionaries, Sets


# 1. Write a function to check if a number is even.
# def func(a):
#     if a%2 == 0:
#         print("even")
#     else:
#         print("odd")
# func(2)
# func(3)
#  ----------------------------XXXXXXXXXX------------------------------------------

# 2. Create a list and find the sum of all its elements.
# l =[23,34,56,78]
# sum = 0
# for i in l:
#     sum = sum +i
# print(sum)
#  ----------------------------XXXXXXXXXX------------------------------------------

# 3. Write a program to find the maximum and minimum in a list.
# l = [10,4,3,12]
# max=l[0]
# min = l[0]

# for i in l:
#     print(i)
#     if i > max:
#         max = i
#     elif i < min:
#         min = i
# print(f"maximum value is {max} and minimum value is {min}")
#  ----------------------------XXXXXXXXXX------------------------------------------

# 4. Create a program that removes duplicates from a list.
# numbers = [1, 2, 2, 3, 4, 4, 5]

# unique_list = []

# for i in numbers:
#     print(i)
#     if i not in unique_list:
#         unique_list.append(i)

# print(unique_list)
#  ----------------------------XXXXXXXXXX------------------------------------------

#5. Write a function to reverse a list.
# def reverse(nums):
#    reverse_list =[]
#    for i in range(len(nums)-1,-1,-1):
#       print(nums[i])
#       reverse_list.append(nums[i])
#    return reverse_list   

# nums =[12,13,14,15,16]
# result = reverse(nums)
# print(result)
#  ----------------------------XXXXXXXXXX------------------------------------------      


#6. Create a tuple and access its elements.

# t = (12,34,5,6,5)
# print(t)
# print(t.index(6))
# print(t.count(5))
# h = t[3]
# print(h)
#  ----------------------------XXXXXXXXXX------------------------------------------      

#7. Convert a list into a tuple and vice versa.
# l = [12,65,78,90]
# convert = tuple(l)
# print(type(convert))

# vise_versa = list(convert)
# print(type(vise_versa))
#  ----------------------------XXXXXXXXXX------------------------------------------      


# 8. Write a program to merge two dictionaries.
# d1 ={
#     1 : "10",
#     2 : "20",
#     3 : "30",
#     40 : "40",
# }

# d2 ={
#     4 : "40",
#     5 : "50",
#     6 : "60",
#     7 : "70",
# }

# for  i in d2:
#     d1[i] = d2[i]
   
# print(d1)
#  ----------------------------XXXXXXXXXX------------------------------------------      

# 9. Write a function to count the frequency of elements in a list.

# def frequency(nums):
#    d={
      
#    }
#    for i in nums:

#       if i in d.keys():
    
#          d[i] +=1
     

         
#       else:
#         d[i] = 1
#    return d

# nums=[1,4,6,4,7,5,1,2,3,4]
# # print(frequency(nums))

#  ----------------------------XXXXXXXXXX------------------------------------------

#10. Create a dictionary of squares of numbers from 1 to 10.

# l = [1,2,3,4,5,6,7,8,9,10]
# sq =0
# d ={}
# for i in l:
#    sq = i*i
#    d[i] = sq
# print(d)
#  ----------------------------XXXXXXXXXX------------------------------------------

#11. Create a dictionary from a list where the key is the number and the value is the number multiplied by 5.
# l = [2,4,6,8,10]

# d={

# }
# for i in l:
#     d[i]=i*5
# print(d)
#  ----------------------------XXXXXXXXXX------------------------------------------

#12. Create a dictionary from a list where only even numbers are included and the value is the square of the number.
# l = [1,2,3,4,5,6,7,8,9,10]
# d ={

# }
# for i in l:
#     if i%2 ==0:
#         d[i ]= i*i
# print(d)
#  ----------------------------XXXXXXXXXX------------------------------------------

#13. Create a dictionary that counts how many times each word appears in the given string.
# s = ",apple ,mango ,apple ,banana ,mango ,apple "
# word =s.split()
# count ={

# }
# for i in word:
#     print(i)
#     if i  in count.keys():
#         count[i]+=1
#     else:
#         count[i]= 1
# print(count)
#  ----------------------------XXXXXXXXXX------------------------------------------

# 14. Write a program to sort a list in ascending order.
# nums = [5, 2, 9, 1, 7]
# result = []

# while nums:
#     m = min(nums)
#     result.append(m)
#     nums.remove(m)

# print(result)
#  ----------------------------XXXXXXXXXX------------------------------------------

# 15. Create a program to check if a key exists in a dictionary.

# d ={
#     "name":"raif",
#     "age":18,
#     "city":"karachi",
     
# }

# key = str(input("Enter your key"))
# if key in d:
#     print(f"key is exist and value is {d[key]}")
# else:
#     print("key does not exist")
#  ----------------------------XXXXXXXXXX------------------------------------------

# 16. Create a set and perform union, intersection, and dif{ference.
# s1 = {1,2,3,4,5,6}
# s2 ={6,7,8,9,10 }
# print(s1.union(s2))
# print(s2.intersection(s1))
# print(s1.difference(s2))
#  ----------------------------XXXXXXXXXX------------------------------------------

# 17. Write a function to find common elements in two lists.
# s1 =[1,8,3,4,5,6 ]
# s2 =[6,1,8,4,10 ]

# common=[]
# for i in s1:
#     if i in s2:
#         common.append(i)
# print("common num is",common)
#  ----------------------------XXXXXXXXXX------------------------------------------

# 18. Write a function that returns the factorial of a number.
# def fact(num):
#     fact = 1
#     for i in range(num,0,-1):
#         fact= fact *i
#     return fact
# print(fact(10))
#  ----------------------------XXXXXXXXXX------------------------------------------

# 19. Create a function that checks whether a string is a palindrome.

# def pallindrome(st):
#     rev="" 
#     for i in range(len(st)-1,-1,-1):
#        rev = rev + st[i]
       
#     if rev ==st:
#      print("pallindrome")
#     else:
#         print("not a pallindrome")

# pallindrome("raif")
# pallindrome("naman")
# pallindrome("maham")
#  ----------------------------XXXXXXXXXX------------------------------------------

# 20. Write a function to count vowels in a string.

# def vowel(st):
#     a = 0
#     for i in st:
#         if i in "aeiou":
#             a = a+1
#     return a
# print(vowel("bilal"))

#  ----------------------------XXXXXXXXXX------------------------------------------

# 21. Create a dictionary and iterate over its keys and values.
# d ={
#     "name":"raif",
#     "age":18,
#     "city":"karachi",
#     "Attendece":True
# }
# for i in d:
#      print(f"{i},{d[i] }")
#  ----------------------------XXXXXXXXXX------------------------------------------

# 22. Write a function to find punctuation from a string.
# import string

# def func(st):
#   a =" "
#   for i in st:
#     if i in string.punctuation:
#       a = a + i
#   return a
# print(func("Hello, world! How are you?"))
#  ----------------------------XXXXXXXXXX------------------------------------------

# 23. Write a function to remove all the punctuation from a string.
# def func(st):
#   a =""
#   for i in st:
#     if i.isalpha():
#       a = a + i
#   return a
# print(func("Hello, world! How are you?"))
#  ----------------------------XXXXXXXXXX------------------------------------------

# 24. Write a function to capitalize the first letter of each word in a string.

# def func(st):
#     a =st.split()
#     print(a)
#     n =[]
#     for i in a:
#         n.append(i.capitalize())
#     r = " ".join(n)
#     print(r)
# func("hello world python")

# 25. Create a list comprehension to get squares of all even numbers in a range.

# n = int(input("Enter num"))
# l =[i*i for i in range(1,n+1) if i%2 == 0]
# print(l)



#  26. Create a list comprehension to get squares of all even numbers in a range.
# n = int(input("Enter num"))
# l =[i*i for i in range(1,n+1) if i%2!= 0]
# print(l)

#  27. Create a list comprehension to get cube of anumbers in  n term.

# n = int(input("Enter num"))
# l = [i*i*i for i in range(1,n+1)]
# print(l)

# 28. Write a function to check if a string is an anagram
# def func(a,b):
#    if len(a)!=len(b):
#     print("not anagram")
#    else:
#     s = sorted(a)
#     d =sorted(b)
#     if s == d:
#         print("anagram")
#     else:
#        print("not anagram")

# func("listen","listen")

# 29. Create a nested dictionary to represent student records.

# students = {
#     "Ali": {
#         "age":15,
#         "marks":60,
#         "attendence": True,
#    },
#    "sara": {
#         "age":16,
#         "marks":90,
#         "attendence": True,
#    },
#     "Ahmed": {
#             "age":17,
#             "marks":80,
#             "attendence":True,
#     }
# }
# # print(students["Ali"]["marks"]
# for i,info in students.items():
#     print(f"Name:- {i}")
#     print(f"Attendance:- {info["attendence"]}")
#     print(f"Age:- {info["age"]}")
#     print(f"Marks:- {info["marks"]}")

# 30. Write a function to flatten a nested list.

# def flatten_list(nested):
#     flat = []
#     for item in nested:
#         if isinstance(item, list):   # agar item list hai
#             flat.extend(flatten_list(item))  # andar wali list ko bhi flatten karo
#         else:
#             flat.append(item)
#     return flat 
# numbers = [1, 2, [3, 4], [5, [6, 7]]]

# print(flatten_list(numbers))

# 31. Write a program to find the second highest number in a list.

# num = [40,10,50,5,11 ]

# first = num[0]
# second = num[0]

# for i in num:
#     if i > first:
#         second = first
#         first = i
# print(f"second highest num is {second}")


