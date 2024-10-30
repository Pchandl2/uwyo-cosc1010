# Peyton Chandler
# UWYO COSC 1010
# 10/29/24
# HW 02
# Lab Section: 11
# Sources, people worked with, help given to: used chatGpt to debug what my code, wasnt working occasionally needed to add the .upper function to char in line 45
# Chat-GPT (2024, October 29) can you help me figure out why my code doesn't work only sometimes but works great other times? " copy and pasted code" https://chat.openai.com/
# your
# comments
# here

morse_code_dict = {
'A': '.-' ,
'B': '-...' ,
'C': '-.-.' ,
'D': '-..' ,
'E': '.' ,
'F': '..-.' ,
'G': '--.' ,
'H': '....' ,
'I': '..' ,
'J': '.---' ,
'K': '-.-' ,
'L': '.-..' ,
'M': '--' ,
'N': '-.' ,
'O': '---' ,
'P': '.--.' ,
'Q': '--.-' ,
'R': '.-.' ,
'S': '...' ,
'T': '-' ,
'U': '..-' ,
'V': '...-' ,
'W': '.--' ,
'X': '-..-' ,
'Y': '-.--' ,
'Z': '--..' ,
}

morse_code = ""
textinput = input("Input the string you want to convert to morse code: ")

for char in textinput:
    if char.isalpha():
        morse_code += morse_code_dict[char.upper()] + " "

    elif char == " " :
        morse_code += " "

print(morse_code)




