# Q1. Write a Python program to check if a string has all unique characters.

# class Duplicate:
   
#     def __init__ (self,string):
#         a = []
#         self.string = string
#         for i in string:
#             if i in a:
#                 print("not unique")
#                 return
#             else:
#                 a.append(i)
#         print("All are unique")
# obj = Duplicate("RAIF")
#  ----------------------------XXXXXXXXXX------------------------------------------


#  ----------------------------XXXXXXXXXX------------------------------------------
# Q2. Create a program that removes all duplicate characters from a string.   

# class Removeduplicate:
#     def __init__(self,duplicate):
#         a = []
#         self.duplicate = duplicate
#         for i in duplicate:
#             if i in a:
#                 a.remove(i)
                
#             else:
#                 a.append(i)
                
#         print(a)
# obj = Removeduplicate("anoosha")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q3. Write a script to count the frequency of each character in a string.

# class Frequecy:
 
#  def __init__(self,string):
#   count = {

#   }
#   self.string = string
#   for i in string:
#     if i in count:
#             count[i] = count[i] + 1      
#     else:
#                 count [i]= 1
#   print(count) 
            
# obj = Frequecy("raif")
#  ----------------------------XXXXXXXXXX------------------------------------------


#  ----------------------------XXXXXXXXXX------------------------------------------
# Q4. Write a program that accepts a sentence and calculates the number of upper and lower case letters.
# class Check:
#     def __init__(self,sentence):
#         n = 0
#         b = 0
#         self.sentence = sentence
#         for i in sentence:
#             if i.upper() in sentence:
#                 n = n + 1
#             else:
#                 b = b + 1
#         print(f"upper case letter count {n}")
#         print(f"lower case letter  count{b}")
# obj = Check("HelloHowAreYou")
#  ----------------------------XXXXXXXXXX------------------------------------------


#  ----------------------------XXXXXXXXXX------------------------------------------
# Q5. Create a program to find the longest word in a sentence.
# class Longest:
#     def __init__(self,sentence):
#         largest = ""
#         self.sentence = sentence
#         word = sentence.split()
        
#         for i in word:
#             if len(i) > len(largest):
#                 largest = i
#         print(largest)
# obj = Longest(" I am learning python programing ")
#----------------------------XXXXXXXXXX------------------------------------------


#  ----------------------------XXXXXXXXXX------------------------------------------
# Q6. Write a program that takes a string and returns the string in reverse order without using [::-1].

# class Reverse:
#     def __init__(self,string):
#         rev = ""
#         self.string = string
#         for i in string:
#             rev = i + rev
#         print(rev)
# obj = Reverse("raif")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q7. Write a program that takes a number and returns the number in reverse order without using [::-1].

# class Reverse:
#     def __init__(self,Number):
#         rev = 0
#         self.Number = Number
#         while Number > 0:
#          digit = Number % 10
#          rev = rev * 10 + digit
#          Number = Number // 10
#         print(rev)
# obj = Reverse(int(54321))
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# # Q8. Create a Python function to check if a string is a pangram.
# class Pangram:
#     def __init__(self,sentence):
#         self.sentence = sentence
#         s = set()
#         for i in sentence.lower():
#             if i.isalpha():
#                 s.add(i)

#         if len(s) == 26:
#             print("Pangram")
#         else:
#             print("Not pangram")
# obj = Pangram("The quick brown fox jups over the lazy dog")
# obj2 = Pangram("Hey I am Learning Python form sheriyans coding school")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# # Q9. Write a Python script to sort words in a sentence alphabetically.
# class Sorting:
#    def __init__(self,sentence):
#       self.sentence = sentence
#       words = sentence.split()
#       words.sort()
#       print(" ".join(words))

# obj = Sorting("The quick brown fox jumps over the lazy dog")
# obj2 = Sorting("i am learning python")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q10 Write a program to check if two strings are anagrams.
# inp1 = input("Enter any string:-")
# inp2 = input("Enter any string:-")
# class Anagramchecker:
#   def __init__(self,s1,s2):
#     dict1={}
#     dict2={}
#     self.s1 = s1
#     self.s2 = s2
#     if len(s1) == len(s2):
#       print("Apllicable for checking wait for furthure processing")
#       for i in s1:
#         if i  in dict1:
#           dict1[i] = dict1[i]  +1
#         else :
#           dict1[i] = 1
#       for i  in s2:
#         if i  in dict2:
#           dict2[i] = dict2[i] +1
#         else:
#           dict2[i] = 1

#       if dict1 == dict2:
#         print("Anagram")
#       else:
#         print("Not an anagram")
#     else:
#         print("length are not similar")
              
# obj = Anagramchecker(inp1,inp2)
#  ----------------------------XXXXXXXXXX------------------------------------------


#  ----------------------------XXXXXXXXXX------------------------------------------
# Q11. Write a Python program to capitalize the first letter of each word in a sentence.
# class Capitalize:
#     def __init__(self,sentence):
#         result = []
#         self.sentence = sentence
#         s = sentence.split()
#         for i in s:
#             result.append(i.capitalize())
#         print(" ".join(result))
# obj = Capitalize("i am learning python")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q12. Create a program that extracts numbers from a string and returns their sum.

# class Extract:
#     def __init__(self,sentence):
#         sum = 0
#         self.sentence = sentence
#         s = sentence.split()
#         for i in s:
#            if i.isdigit():
#               convert = int(i)
#               sum =  convert + sum
#         print(sum)  
# obj = Extract("I have 10 apples and 20 oranges and 5 bananas")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q13. Write a program to replace all spaces in a string with underscores.
# class Replace:
#     def __init__(self,sentence):
#         self.sentence  = sentence
#         s = sentence
#         replace=""
#         for i in sentence:
    
#             if i.isspace():
#                replace += "_"
#             else:
#                 replace += i
                
#         print(replace)

# obj = Replace("This is my first Python program")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q14. Write a function to count how many times a substring appears in a string.
# class Substring:
#     def __init__(self,string,substring):
        
#         self.string = string
#         self.substring = substring

#         repeat = 0
#         n = len(substring)

#         for i in range(len(string) -n + 1):
#             if string[i:i+n] == substring:
#                 repeat +=1

#         print(repeat)

# obj = Substring("I love Python. Python is easy. Python is powerful.", 
#                 "Python")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q15. Write a script to convert a string into title case without using .title().

# class Titlecase:
#     def __init__(self,sentence):
#         self.sentence = sentence
#         s = sentence.split()
#         result = []
#         for i in s:
#             a = i[0].upper()
#             b = i[1:].lower()
#             result.append(a+b)

    
#         print(" ".join(result))
# obj = Titlecase("i am learning python")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q16. Write a Python program to merge two dictionaries into one.
#
#     a = {
#         "name" : "Ali",
#         "age" : 17,

#     }

#     b = {
#         "city" : "karachi",
#         "phone no" : 12345678,

#     }
#     for i in b:
#        a[i] = b[i]
#     print(a)
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q17. Create a program to filter out all non-alphabetic characters from a string.

# class Filter:
#     def __init__(self,string):
#         self.string = string
#         alphabet = ""
#         non_aplphabet= ""
#         for i in string:
#             if i.isalpha():
#                 alphabet += i 
#             else:
#                non_aplphabet += i
#         print(alphabet) 
#         print(non_aplphabet)
# obj = Filter("Pyth0n@123")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q18. Write a function that returns True if a string ends with a given suffix.

# class Sufix:
#     def __init__(self,string):
#         self.string= string

#     def check(self):
        
#         if self.string.endswith((".pdf",".txt",".py",".png",)):
#             print("True")
#             return True
#         else:
#             print("False")
#             return False


# obj = Sufix("document.py")
# obj.check()
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q19. Create a program that counts words, characters, and lines in a paragraph.   
# class Checker:
#     def __init__(self, string):
#         self.string = string

#         # Lines
#         lines = string.count("\n") + 1
#         print(f"Total lines: {lines}")

#         # Characters
#         characters = len(string)
#         print(f"Total characters: {characters}")

#         # Words
#         words = len(string.split())
#         print(f"Total words: {words}")

# obj = Checker("I love Python")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q20. Write a script to encode a string using Caesar cipher (shift = 3).

# class Encoded:
#     def __init__(self, string):
#         self.string = string
#         result = ""

#         for i in string:
#             if i.isalpha():

#                 if i.isupper():
#                     new_char = chr((ord(i) - 65 + 3) % 26 + 65)

#                 else:
#                     new_char = chr((ord(i) - 97 + 3) % 26 + 97)

#                 result += new_char

#             else:
#                 result += i

#         print(f"Caesar cipher of tasmia is {result}")
# obj = Encoded("raif")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q21. Write a program that accepts a string and counts vowels and consonants.
# class Count:
#     def __init__(self,string):
#         self.string = string
#         vowels = 0
#         consonats = 0
#         for i in string.lower():
#             if i in "aeioe":
#                 vowels += 1
#             else:
#                 consonats +=1
#         print(f"vowels = {vowels}")
#         print(f"consonats = {consonats}")


# obj = Count("raif")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q22. Create a script to convert binary string to decimal.
# class Convert:
#     def __init__(self,binary):
#         self.binary = binary
#         total = 0
#         power = 0
#         for i in binary[::-1]:
#          digit =int(i) 
#          value = digit * (2**power)
#          total = total + value
#          power = power + 1
#         print(total)
# obj = Convert("1101")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q23. Create a script to convert decimal to binary string .
# class Convert:
#     def __init__(self,decimal):
#         self.decimal= decimal 
#         reminder = 0
#         binary = ""
#         while decimal > 0:
#             a = decimal % 2
#             reminder = a
#             decimal = decimal // 2
#             convert = str(reminder)
#             binary = binary + convert
#         print(binary)
        
# obj = Convert(45)
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q24. Write a program to count the number of words starting with a vowel in a string.

# class Count:
#     def __init__(self,sentence):
#         self.sentence = sentence
#         count = 0

#         for i in sentence.split():
#             if  i[0].lower() in "aeiou":   
#                 count = count + 1
#         print(count)

# obj = Count("I am learning Python ")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q25. Create a script that takes a sentence and removes all stop words.
# class Script:
#   def __init__(self,sentence):

#     self.sentence = sentence
#     a = ["is", "am", "are", "the", "a", "an", "and", "of", "in", "to"]
#     result =[]
#     for i in  self.sentence.split():
#         if i not in a:
#            result.append(""+ i) 
        
           
#     print(" ".join(result))
           
# obj = Script("i am learning python and data science")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q26. Write a Python program to split a sentence into words and reverse each word.

# class Reverse:
#     def __init__(self,string):
#         self.string = string
#         result = []
#         for i in string.split():
#             print(i)
#             result.append(i[::-1]) 
#         print(" ".join(result))

# obj = Reverse("i love myself")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q27. Write a function that returns a new string made of every third character of the original string.
# class Newstring:
#     def __init__(self,string):
#         self.string = string
#         result = ""
#         index = 2
#         while index < len(string):
#             result = result + string[index]
#             index = index + 3
#         print(result)

# obj = Newstring("PythonProgramming")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q28. Write a program to find all palindromic substrings in a string.
# class Find:
#     def __init__(self, string):
#         self.string = string
#         result = []

#         for i in range(len(string)):
           
#             for j in range(i + 1, len(string) + 1):
        
#                 substring = string[i:j]

#                 if substring == substring[::-1]:
#                     result.append(substring)

#         print(result)
# obj = Find("madam")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q29. Write a function that compresses a string using run-length encoding.

# class Compresses:
#     def __init__(self,string):
#         self.string = string
       
#         result = ""
#         count = 0

#         for i in range(1, len(string)):
#           if string[i]==string[i - 1]:
#              count += 1
#           else:
#              result = result + string[i - 1] + str(count)
#              count = 1
#         result = result + string[-1] + str(count)
#         print(result)
            
# obj = Compresses("aaabbcccca")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q30. Write a Python program to count the frequency of each word in a file.
# with open("file.txt", "w") as fs:
#     fs.write("python is easy python is powerful")

# with open("file.txt", "r") as fs:
#     content =fs.read()
#     dict = {}
#     for i in content.split():
#         if i in dict:
#             dict[i] = dict[i] +1
#         else:
#             dict[i] =1
#     print(dict)
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
#  Q31. Write a script that extracts hashtags from a tweet.
# class Extract:
#     def __init__(self,sentence):
#         self.sentence = sentence
#         for i in sentence.split():
#             if i[0] == "#":
#                 print(i)
        
# obj = Extract("I am learning #Python and #FastAPI for #BackendDevelopment")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q32. Write a function to remove punctuation from a string.
# class Remove:
#     def __init__(self,string,a):
#         self.string = string
#         self.a = ""
#     def punctuate(self):
#         for i in self.string:
#             if i.isalpha() or i == " ":
#               self.a +=   i
#         print(self.a)


# obj = Remove( "Hello, world! How are you? ","punctuate")
# obj.punctuate()
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q33. Create a program that finds the first non-repeating character in a string.

# class Find:
#     def __init__(self,string):
#         self.string = string

#     def char(self):
#         count = {}
      
#         for i in self.string:
#             if i in count:
#                 count[i] = count[i] + 1
#             else:
#                 count[i] = 1
#         # print(count)
#         for key,value in count.items():
#            if value == 1:
#             print(key,value)
       
               
# obj = Find('aabbcde')
# obj.char()
#  ----------------------------XXXXXXXXXX------------------------------------------


#  ----------------------------XXXXXXXXXX------------------------------------------
#  Q34. Write a script that converts camelCase to snake_case.
# class Camelcase:
#     def __init__(self,string):
#         self.string = string
#         result= ""
  
#         for i in string:
#             if i.isupper():
#              result = result + "_" + i
#             else:
#                result = result + i
#         print(result)

# obj = Camelcase("myPython")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q35. Write a function to generate acronyms from a sentence.

# class Acronyms:
#     def __init__(self,string):
#         self.string = string
#     def generate(self):
#       b = ""
#       a = [i[0]for i in self.string.split()]
  
#       for i in a:
#          b = b + i.capitalize()
#       print(b)
       

# obj = Acronyms('international business machine')
# obj.generate()
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q36. Write a script to check if a file contains a specific word.
# class Script:
#     def __init__(self,string):
#         self.string = string
   
#             # print(i)
#         with open("file.txt",'r') as fs:
#                 content = fs.read()
#                 # print(content)
#         if string.lower() in content.lower():
#              print("Found")
#         else:
#             print("Not Found")

# obj = Script("Python")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q37. Write a Python program to find and replace text in a file.

# old_words = input("Enter finding word:-")
# new_words = input("Enter replacement word:-")
# class Program:
#     def __init__(self,string1,string2):
#         self.string1 = string1.lower()
#         self.string2 = string2

#         with open("file.txt","r") as fs:
#             content = fs.read()
            
#         if self.string1.lower()  in content.lower():
#             new_content = content.replace(self.string1.lower(),self.string2.lower())

#             with open("file.txt","w") as file:
#                 file.write(new_content)
#                 print(new_content)

            
                        
#         else:
#                 print("No such word found")
# obj = Program(old_words,new_words)
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q38. Write a script that checks if all characters in a string are digits.
# class Check:
#     def __init__(self, string):
#         self.string = string

#     def check(self):
#         for i in self.string:
#             if not i.isdigit():
#                 print("False")
#                 return False

#         print("True")
#         return True


# obj = Check("1234fds56")
# obj.check()
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q39. Write a program to calculate the average word length in a sentence.
# class Average:
#     def __init__(self,string):
#         self.string = string.split()
        
#         length =  len(self.string)
#         sum = 0
            
#         for i in self.string:
#             sum += len(i)
#         average = sum / length
#         print(average)

# obj = Average("I love python") 
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q40. Create a function that removes all HTML tags from a string.
# class Remove:
#     def __init__(self,sentence):
#         self.sentence = sentence
#         self.insidetag = False
#         self.result = ''
#         for i in self.sentence:
#             if i == "<":
#                 self.insidetag = True
#             elif i == ">":
#                 self.insidetag = False
#             elif  not self.insidetag:
#                 self.result = self.result + i
#         print(self.result) 
            
# obj = Remove("<p>I love <b>Python</b></p>")
# #  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q41. Write a program to parse a date string and display it in a different format.
# class Date:
#     def __init__(self,string):
#         self.string  = string.split("-")
       
#         self.day = ""
#         self.month =""
#         self.year =""
#         self.day = self.day  +   self.string[0] 
#         self.month = self.month + self.string[1]
#         self.year = self.year + self.string[-1]
#         total = self.year +"/"+ self.month +"/"+ self.day
#         print(total)
        
# obj = Date("9-10-2008")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q42. Write a script that finds all email addresses in a given text.

# class Email:
#     def __init__(self,string):
#         self.string = string
#     def Check(self):
#         result =[]
#         for i in self.string.split():
#             if "@" in i and "."in i:
#                 result.append(i)
#         print(result)


# obj = Email("My email is abc@gmail.com and office email is xyz@hotmail.com")
# obj.Check()
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q43. Write a program that counts the occurrence of each vowel in a paragraph.

# class Occurrence:
#     def __init__(self,paragraph):
#         self.paragraph = paragraph
#     def func(self):
#         count = {
#         }
       
#         for i in self.paragraph:
#             if i in "aeiou": 
#                 if i in count:
#                  count[i] = count[i] + 1
#                 else:
#                     count[i] = 1
        
#         print(count)

# obj = Occurrence("i love python programming")
# obj.func()
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
#Q 44. Write a script to check if a string is a valid URL.
# class Check:
#    def __init__(self,string):
#       self.string = string
      
#    def checker(self):
#         if self.string.startswith('http://' )or self.string.startswith('https://')  and "." in self.string:
#            print("Valid URL")
#         else:
#            print("Unvalid URL")
           

# obj = Check("raif//facebook.com")
# obj.checker()
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
#  Q45. Write a program that extracts all integers from a given text.
# class Extract:
#     def __init__(self,text):
#         self.text = text.split()
        
#     def extract(self):
#         a = []
    
#         for i in self.text:
#             if i.isdigit():
#                 a.append(i)
#                 print(i)
#         print(a)
        
                
# obj = Extract("I have 10 apples and 25 oranges and 5 bananas")
# obj.extract() 
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q46. Create a script to find duplicate words in a paragraph.

# class Duplicate:
#     def __init__(self,string):
#         self.string = string
#     def find(self):
#         count = []
#         for i in self.string.split():
#             if i not in count:
#                count.append(i)
#             else:
#               print(i)
            
# obj = Duplicate("Python is easy and Python is powerful")
# obj.find()
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q47. Write a program that converts a sentence to Pig Latin.
# class Convert:
#     def __init__(self,string):
#         self.string = string.split()
        
#         result = []
#         for i in self.string:
#             first_word = i[0]
#             remaining_word = i[1:]
#             new = remaining_word + first_word + "ay"
#             result.append(new)
#         print(result)
  

# obj = Convert("I love Python")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q48. Write a script that finds the longest sentence in a paragraph.
# class Find:
#     def __init__(self,paragraph):
#         self.longest_sentence =""
#         self.paragraph = paragraph.split(".")
#         for i in self.paragraph:
#             if len(i) > len(self.longest_sentence):
#                 self.longest_sentence = i
#         print(self.longest_sentence)


# obj = Find("I love Python. Python is easy to learn. It is used in web development and artificial intelligence.")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q48. Write a Python program to read a file and display all lines that contain a given keyword.
# class Keyword:
#     def __init__(self,string):
#         self.string = string
#         self.a =""
#         with open("file.txt","r") as fs:
#             content = fs.readlines()
#             for i in content:
                
#                 if string in i:
#                     self.a = self.a + i
#         print(self.a)
                  
# obj = Keyword("Python")
#  ----------------------------XXXXXXXXXX------------------------------------------

#  ----------------------------XXXXXXXXXX------------------------------------------
# Q49. Write a script to clean a text file by removing extra spaces and blank lines.
# with open('file.txt') as fs:
#     content = fs.readlines()
#     result = []
#     for i in content:
#         cleanline  = " ".join(i.split())
#         if cleanline != "":
#             result.append(cleanline)
        
# with open("file.txt", "w") as fs:
#     fs.write("\n".join(result))

# print("File cleaned successfully")
#  ----------------------------XXXXXXXXXX------------------------------------------


#  ----------------------------XXXXXXXXXX------------------------------------------
# Q50. Write a Python program to count how many sentences are in a paragraph.

# class Program:
#      def __init__(self,string):
#           self.string = string
#           count = 0
#           for i in self.string.split():
        
#                if i.endswith(('.' , '!' , '?')) :
#                     count+= 1
#           print(count)

# obj = Program("I love Python. It is easy. Do you like it?")
#  ----------------------------XXXXXXXXXX------------------------------------------
        

            




