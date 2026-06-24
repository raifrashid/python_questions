# Phase 1: Python (Week 1–4)
#               : Basics – Variables, Data Types, Input/Output, Loops, Conditionals


#Q1. Write a Python program to swap two variables.
# a = 5
# b= 10
# a,b= b,a
# print(a,b)
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q2. Take user input and display it back to the user.
# user = input("input here")
# print(user)
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q3. Write a program to check if a number is even or odd.
# user_num = int(input("tell the number"))
# if user_num % 2 == 0:
#     print("even")
# else :
#     print("odd")
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q4. Create a program that prints the multiplication table of a given number.
# user = int(input("tell the table num"))
# for i in range(11):
#     print(f"{user}x{i}={user * i} ")
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q5. Write a program to find the largest of three numbers.
# user_inp = int(input("ENter 1st num"))
# user_inp2 = int(input("ENter your 2nd num"))
# user_inp3 = int(input("Enter your 3rd num"))

# if user_inp > user_inp2 and user_inp > user_inp3:
#     print(F"{user_inp} is greater")
# elif user_inp2 > user_inp and user_inp2 > user_inp3:
#     print(f"{user_inp2} is greater")
# elif user_inp3 > user_inp and user_inp3 > user_inp2:
#     print(f"{user_inp3} is greater")

# elif user_inp == user_inp2 :
#     print(f"{user_inp,user_inp2} both are same")
# elif user_inp == user_inp3 :
#     print(f"{user_inp,user_inp3} both are same")
# elif user_inp2 == user_inp3:
#      print(f"{user_inp2,user_inp3} both are same")
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q6. Convert temperature from Celsius to Fahrenheit.
# celsius = int(input("convet temp celsius to farhenheit"))
# farhenheit = celsius*9/5 + 32
# print(farhenheit)
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q7. Write a program to calculate the factorial of a number using a loop.
# n = int(input("Enter your num"))
# num = 1
# for i in range(n,0,-1):
#     num = i * num
# print(num)
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q8. Create a program to count the number of vowels in a string.
# name = input("Enter any letter or sentence: ")
# counter = 0

# for ch in name:
#     if ch.lower() in "aeiou":
#         counter = counter + 1

# print(counter)
#  ----------------------------XXXXXXXXXX------------------------------------------


#Q9. Write a Python script to reverse a given string.
# text = input("Enter a string: ")

# reversed_text = text[::-1]

# print("Reversed string:", reversed_text)
#  ----------------------------XXXXXXXXXX------------------------------------------


#Q10. Check if a number is a palindrome.
# num = int(input("Enter number :"))
# if num == num[::-1]:
#     print("Number is palindrome")
# else:
#     print("not a palindrome")
#  ----------------------------XXXXXXXXXX------------------------------------------


#Q11. Check if a string is a palindrome.
# inp = input("Enter your string")
# if inp == inp[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q11. Write a program to find the sum of first N natural numbers.
# n = int(input("Calculate the sum where you want to "))
# sum = 0
# for i in range(1,n+1):
#      print(i)
# #     sum = i + sum
# # print(sum)
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q12. Create a number guessing game.
# import random
# computer = random.randint(1,10)
# print(computer)
# sum = 0
# while True:
#     user = int(input("Guess the Number"))
#     sum +=1
#     if user == computer:
#         print("Congrats you win")
#         print("You took",sum,"Guesses to find the correct number")

#         break
#     elif user > computer:
#         print("Your num is high")
#     elif user< computer:
#         print("Your num is low")
#  ----------------------------XXXXXXXXXX------------------------------------------


#Q13. Write a program to print all prime numbers between 1 and 100.

# for num in range(2,101):
#    prime = True
#    for i in range(2,num):
#       if num %i == 0:
#          prime == False
#          break
# if prime:
#    print(num)
#  ----------------------------XXXXXXXXXX------------------------------------------


#Q14. Check if a given year is a leap year or not.
# year = int(input(("Enter year")))
# if year % 4 == 0:
#     print("leap year")
# elif year % 100 != 0:
#     print("not a leap year")
# elif year % 400 == 0:
#     print("Leap year")
# else:
#     print("not a leap year")
#  ----------------------------XXXXXXXXXX------------------------------------------



#Q15. Create a program to print the Fibonacci series up to N terms.
# n = int(input("Enter number"))
# a = 0
# b = 1
# if n>= 1:
#     print(a,end=(""))
# if n>=2:
#     print(b,end=(""))
# for i in range(3,n+1):
#     print(i)
#     next = a + b
#     print(next)
#     a = b
#     b= next
#  ----------------------------XXXXXXXXXX------------------------------------------


#Q16. Write a program to find the GCD of two numbers.

# a = int(input("Enter 1st num"))
# b = int(input("Enter 2nd num"))

# gcd = 1

# for i in range(1, min(a, b) + 1):
#     # print(i)
#     if a % i == 0 and b % i == 0:
#         gcd = i
#         print(gcd)
# print(gcd)

# print("GCD is:", gcd)


#  ----------------------------XXXXXXXXXX------------------------------------------


#Q17. Write a program to find the LCM of two numbers.
# a = int(input("Enter 1st num"))
# b = int(input("Enter 2nd num"))
# for i in range(max(a,b), a*b +1):
#     print(i)
#     if a % i == 0 and b % i == 0:
#        lcm = i
#        print(lcm)
#        break
# print(lcm)
#  ----------------------------XXXXXXXXXX------------------------------------------

#Q18 Check whether a character is a vowel or consonant.
# a = input("Enter any letter: ")

# for i in a:
#     if i.lower() in "aeiou":
#         print("Vowel")
#     else:
#         print("Consonent")
#  ----------------------------XXXXXXXXXX------------------------------------------

#Q19. Write a program to calculate the sum of digits of a number.
# n = int(input("Enter a number: "))

# sum = 0
# while n > 0: 
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10

# print("Sum of digits:", sum)
#  ----------------------------XXXXXXXXXX------------------------------------------

#Q20. Create a program to find the second largest number in a list.
# nums = [10, 45, 32, 60, 25]

# largest = nums[0]
# second = nums[0]
# for n in nums:
#     if n > largest:
#         second = largest
#         largest = n

#     elif n < largest and n > second:
#         second = second

# print("Second largest is:", second)
#  ----------------------------XXXXXXXXXX------------------------------------------
