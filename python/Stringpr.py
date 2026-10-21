import string

# #create a string
# str0 = "prince"
# str = "    Ra uniYar the   Great"

# # #method
# # print(len(str))
# # print(str.upper())
# # print(str.lower())
# # print(str.find("i"))
# # print(str.find("io")) #return true if find otherwise gives -1
# # print(str.find("i"))
# # print(str.index(""))


# # print(str.lstrip())
# # print(str.rstrip())
# # print(str.strip())

# print(str.capitalize())
# print(str.upper().title())
# print(str.swapcase())

#replace and join
# str="prince rauniyar, i am froam "
# str.replace("rauni","baniya")
# print((" ".join(str)))

# print(str.split(" "))
# print(str.partition(","))


# #check the string
# str = "prince"
# str2 ="r34i@1"
# print(str.isalpha())
# print(str.isdigit())
# print(str2.isalnum())
# print(str.isspace())
# print(str2.islower())
# print(str2.isupper())

#string clean

# str5 = "prince@124*&%"
# clean =" "
# for ch in str5:
#   if ch in string.ascii_letters:
#     clean += ch
# print(clean)
    
#password check

# password = input("enter the password: ")
# if len(password) <12:
#   print("password should be 12 digit")
# elif "prince" in password.lower():
#   print("dont use of name")
# elif password in string.punctuation:
#   print("password must use the punctuation")
# else:
#   print("accepted")

# #vowels exist
# str6 = input("enter the string: ")
# vowels = 0
# consonant = 0
# for ch in str6:
#   if ch.lower() in "aeiou":
#     vowels +=1
#   else:
#     consonant +=1
# print("vowels: ",vowels,"consonant: ",consonant)

# #word,count,search

# str = input("enter the string: ")
# print(str)
# list = str.split()
# print("count word: ", len(list))
# print("upper case:", str.upper())





