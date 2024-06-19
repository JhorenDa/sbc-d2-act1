#index
'''
text = "Bertox"
imput = int(input("Enter a number >"))
print(text[imput])

print(len(text)-2)'''
#-------------------------------------------------------------------------------------------------------------------------
#slicing
'''
text = "Hello World"
#       012345678910
#       12345
print(text[-5: ])

print("{0} {1}".format(text[-5:], text[0:5]))
'''
#-------------------------------------------------------------------------------------------------------------------------
#sting
'''
text = "hello world"
print(text.upper())
print(text.lower())
print(text.capitalize())
print(text.title())
print(text.replace("h","s"))
print(text.find("h"))
print(text.isalpha())
print(text.isnumeric())
print(text.isalnum())
'''
#-------------------------------------------------------------------------------------------------------------------------
#activity
text = "summer bootcamp"
print(text.title())
s = text.capitalize()
print(s.replace('p','P'))
s = text.replace("b","l")
print(s[7:11].capitalize())
s = text[-4:]
print(s.replace("p","E"))
s = text.upper()
print(f"{s[-3]}{s[5]}")
print(text.replace(" ", "").isalpha())

