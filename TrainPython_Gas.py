# Terminal Command + Git f(x)
    # CLS -> clear terminal
    # git status -> checking file status within a specified folder
    # git init -> initiate git remote on on a selected folder 
    # git add filename.py buat nambahin file tsb ke repo
    # git commit -m "first commit" - "nama commit"
    # git remote add origin (linkrepo) buat ngelink ke repo
    # git push -u origin main buat ngepush 
    # kalo abis make change, cara push commit
        # git add . 
        # git status
        # git commit -m "second commit" - "nama commit"
        # git push
    # Link cara commit, push, dll -> https://www.youtube.com/watch?v=eGaImwD8fPQ&ab_channel=VedTheMaster
    # Link tambahan -> https://stackoverflow.com/questions/827351/push-origin-master-error-on-new-repository/6518774#6518774

#Darurat
    #Stop the running code by pressing  CTRL + C in the terminal

# Python_Variables_____________________________________________________________________
    # Used to store data (values)
        # Eg. a = 10, b = 1.1, a & b itu variables. Bacanya, variable a storing value 10
    # Ibaratnya variable itu bag to store books in it, booksnya bisa diganti at any time
        # Eg. a = 10, a =1, awalnya value a 10 trs ganti jadi 1
    # Aturan penamaan
        # a to z, A to Z, 0 to 9 atau _ 
        # ga bisa start a variable name with a digit
        # pake underscore buat gantiin spasi
        # ada beberapa word yg ga bisa dipake krn dia functions misal: if, for, except, try, or, etc. (kalo maksa masukin ini bakal ada feedback syntax error)
        # Eg. number, salary, first_name, number1
    #Python_Literals
        # number = 5.5 | number itu variabelnya, 5.5 itu literal
        # jenis literalnya ada numeric, string, boolean
        # Numeric_Literals
            # Integers = 5, 0, -45
            # Floats = 3.4, 1.3, 1.52e2 = 1.525*10^2, e = 10^
            # Numeric_literals can also be represented in binary, hexadecial, or octal systems
            # Eg. a = 0b1011 -> binary, b = 0o310 -> Octal, c = 0x12c -> hexadecimal
        # String_Literals
            # a sequence of characters surrounded by quotes, bisa pake single, double, or triple quotes for a string
            # triple quotes """___""" buat multiline string, jadi output printnya bisa >1 baris
        # Boolean_Literals
            # True, False
            # a = true -> error
                # dia case sensitive, kalo kita tulis a = true -> error
            # a = True -> assigned True to the variable 'a'
            # a = 'True' -> ga error sih, tapi 'True' is stored as string
        #  Opearator
            # '%' modulus -> a%b -> Gives remainder after dividing a from b
            # '**' Exponential -> 3**2 = 9
            # '//' floor division -> 15//2 = 7 -> hasilnya kan 7.5 dibuletin ke bawah 7
            # & and
            # | or
            # ^ XOR
            # ~ NOT
            

# Opeartor List

# Python_Input_and_Output
            


# Operator&Operrands___________________________________________________________

# Declare
# a = input("Insert Integer a: ")
# A = int(a)

# b = input("Insert Integer b: ")
# B = int(b)

# c = input("Insert Integer c: ")
# C = int(c)

# Operator
# Multi = A*B*C
# Add = A+B+C

# Printing
# print(A, "times", B, "times", C, "equals: ", Multi)
# print(A, "add", B, "add", C, "equals: ", Add)


# Coba2___________________________________________________________

# tes leap year
# tahun yg habis dibagi 4
# kalo century year (yg endingnya 00) dia habis dibagi 100
# century year yag masuk ke himpunan leap year itu habis dibagi 400

# tahun = 1999 (isi tahunnya)

'''

print ("Silakan input tahun yang ingin dicek apakah dia leap atau bukan")
tahun = input ()
tahun = int (tahun)

if (tahun % 4) == 0:
    if (tahun % 100) == 0:
        if (tahun % 400) == 0:
            print (tahun, 'is a leap year')
        else:
            print (tahun, 'is not a leap year')
    else:
        print (tahun, 'is not a leap year')
else:
    print (tahun, 'is not a leap year')

'''

# LearnPython FreeCodeCampOrg  _________________________________________________________
# Link (https://youtu.be/rfscVS0vtbw)

# 1
# DATA TYPES AND VARIABLES
'''

character_name = "Tom"
character_age = "50"
is_male = True 

print ("There once was a man named " + character_name + ", ")
print ("He was " + character_age + " years old. ")

# Store and replace variable with new value
character_name = "Tomi-Chan"

print ("He really liked the name " + character_name + ", ")
print ("but didn't like being " + character_age + ".")

# Data Type
    # Strings = Plain text
    # Numbers -> bisa integer (whole number) bisa float (decimal) - no need using quotation mark
    # Boolean -> True or False -> "istrue"
'''

# 2
# WORKING WITH STRINGS______________________________________

'''

# \n  -> buat add enter
# \" -> print quotation mark
# concatenation -> combining multiple strings

phrase = "Giraffe Academy"

print("\n\"Giraffe\"\nAcademy\n")
print (phrase + " is cool")

# Bisa juga nambain functions to Modifiy or Get Information about our strings

print (phrase.lower())
print (phrase.upper())

# Apakah phrase variable SEMUA STRINGNYA uppercase,
# kalo gak harusnya return 0 or False

print (phrase.isupper())
print (phrase.islower()) 

# bisa juga kita kasih functions yg berurutan,
# misal mau ngasih upper case ke phrase,
# terus dicek pake True False statement,
# harusnya return True

print (phrase.upper().isupper())

# we can also figure out the length,
# (number of character) of the string,

print (len(phrase))

# Get individual character inside of a string
# Misal mau ngambil value r nya doang, start index di 0

print (phrase[0])
print (phrase[3])

# Index Functions -> kita bisa cari tahu where a specific,
# function itu sebenernya ya cuma a little collection of code that does sth, kyk Mf kalo di UE
# character is located within our string
# ini namanya proses passing parameter - kyk proses inverse
# kalo kita get location dari "Acad" bakal return 8 karena
# kata Acad distart di character ke-8 yakni a
# kalo cari lokasi "z" dari string ga bakal ketemu, return error 

print (phrase.index("G"))
print (phrase.index("a"))
print (phrase.index("Acad"))

# ada function .replace (par1, par2), tapi kita kudu masukin 2 parameter
# old value sama new value

print (phrase.replace("Giraffe", "Elephant"))

# yg barusan itu functions2 yg common, kalo mau ngulik lebih googling aja

'''

# 3
# WORKING WITH NUMBERS______________________________________

'''

print(2)
print(2.0987)
print(-2.0987)
print(3+4.5)
print(((1+1)*6)/2)

# 10 modulo 3 -> 10 / 3 itu jawabannya 3 sisa 1... yg diprint oleh
# modulus operator itu sisanya

print(10 % 3)

my_num = -5.2
print(my_num)

# convert my_num value into a string. why perlu convert
# supaya number ini bisa diprint bareng string

print(str(my_num) + " is my favorite number")

# Number functions
# abs - take absolute value
# pow - pass 2 pieces of information to pow (number, the power of it)
# max
# min
# round - value desimal 0.5 ke atas bakal dibuletin ke atas

print (abs(my_num))
print ("Absolute number of my_num is " + str(abs(my_num)))
print ((pow(3, 2)))
print (max(4,100))
print (round(3.2))
print (round(3.5))


# kalo kita mau import specific python operation or function yg
# udah kita buat bisa juga broo atau udah ada librarynya -> type: from math import *
# kalo bahasa teknisnya "math" ini adalah MODULE, bukan library
# floor - grab lowest number, ceil sebaliknya
# sqrt - square root


from math import *

print (floor(2.7))
print (ceil(2.3))
print (sqrt(36))

'''

# 4
# GETTING INPUT FROM USERS_________________________________

'''
name = input("Enter yout name: ")
age = input("Enter yout age: ")
gender = input("Enter yout gender (Male/Female): ")
print ("\nHello, I am " + name + "!" + "\nA " + age + " years old " + gender)
'''

# 5
# BUILDING BASIC CALCULATOR________________________________

# By default, Python convert angka ke string, makanya kudu didefine kalo ini float or int
# Function int() or float()

'''
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
add = float(num1) + float(num2) 

print (add)
'''

# 6
# Mad Libs Game____________________________________________

'''
color = input("Type a color: ")
plural_noun = input("Type a plurar_noun: ")
celebrity = input("Type a celebrity: ") 

print ("Roses are " + color)
print (plural_noun + " are blue")
print ("I love " + celebrity)
'''

# 7
# Lists____________________________________________________

# Penting karena kita deal with large amount of data, biar managable
# [2:] -> 2 sampe habis listnya
# [1:3] -> 1 sampe 2, value 3 cuma sebagai batas atas, ga include 

'''

friends = ["Fuad", "Kanza", "Edo", "Angel", "Isyfi"]

# Revisi value inside of a python list (ganti)
# kita juga bisa add element within a list, copy, dll.

friends[1] = "JAYANTO"

print (friends)
print (friends[2])
print (friends[-1])
print (friends[2:])
print (friends[1:3])

'''
'''
lucky_numbers = [4, 8, 15, 16, 23, 70, 42]
teman = ["Fuad", "Kanza", "Edo", "Angel", "Isyfi"]
teman.extend (lucky_numbers)
teman.append ("Jokowi")
teman.insert (1,"USTAD_NYEMPIL")
teman.remove ("Edo")

# pop itu ngekick last emlement within a list, di sini Jokowi yg udah diappend dipop
teman.pop ()

print (teman)

#cari tau Isyfi itu di urutan ke-berapa
print (teman.index("Isyfi"))

#ngitung berapa kali suatu element muncul di list
print (teman.count(15))

# https://www.youtube.com/watch?v=rfscVS0vtbw&ab_channel=freeCodeCamp.org
# Now 1:16:48

#SortingNomer_

print (lucky_numbers)

lucky_numbers.sort ()
print (lucky_numbers)

lucky_numbers.reverse ()
print (lucky_numbers)

teman2 = teman.copy()
print (teman2)
'''

# 8
# Tuples__________________________________________________

# tes V11

# 8
# TUPLES
'''
# tes V11
# Tuple = type of data structure -> A Container where we can store different value. Mirip sama list. Tapi ada bedanya ->

# Tuple is IMMUTABLE (Can't be changed or modified)
# Tuple pake (), sedangkan list pake []

coordinates = (4, 5)

# 4 itu index position 0 dan 5 itu index position 1
# kalo kita ganti value dalem tuples -> misal:
# coordinates[1] =  10
# bakal return Error, jadi 4 ga bisa diganti 10

print (coordinates[0])
print (coordinates[1])

tupleinsidelist = [(4, 5), (6, 7), (80, 34)]
print (tupleinsidelist)
'''

# 9
# FUNCTIONS_______________________________________________

# F(x) = collection of code which performs a specific task
# kalo mau do that task, tinggal call aja functionsnya
# biar ada chunking! dan lebih modular
# Commit V12

'''
# make function
def say_hi():
    print("Hello User")

# call the function
print ("top")
say_hi ()
print ("bottom")

# coba digabung sama input
name = input("Tulis Namamu: ")
age = input("Tulis Umurmu: ")

def say_hiv2 (name, age):
    print ("Hello " + name + ", you are " + str(age))

say_hiv2 (name, age)
'''

'''
# add additional info to the f(x) -> parameters
say_hiv2 ("Joe, ", "35")
say_hiv2 ("Mike, ", "10")
say_hiv2 ("Steve, ", "5")
'''

#Lanjutan if statements

# 10
# RETURN STATEMENTS in python f(x)__________________________
'''
def cube(num):
    return float(num)*float(num)*float(num)

# !!!! setelah return statement ga bisa ditambahin statement lain kyk print dll. return will breaks out the functions, ibaratnya diterminate.

num = input("Type a number: ")
print(str(num) + " cubed equals: " + str(cube(num)))
'''
# Now at 1:40:10 - IF Statements

# 11
# IF Statements_____________________________________________

# Statemetn Examples

# I wake up
# If I'm hungry (Conditions: True/False)
    # I eat breakfast (Action if true)

# I leave my house
# If it's cloudy
    # I bring an umbrella (Action if true)
# otherwise
    # I bring sunglasses (Action if false)

# I'm at a restaurant
# If I want meat
    # I order a steak (Action if true)
# otherwise if I want pasta
    # I order spaghetti & meatballs (Action if previous false)
# otherwise
    # I order a salad (Action if previous false)

'''
# Create boolean_var
is_male = False
is_tall = False

#if statements: or
if is_male or is_tall:
    print ("he is male or tall or both\n")
else:
    print ("he neither male nor tall")

is_male2 = True
is_tall2 = True

#ifstatements: and
if is_male2 and is_tall2:
    print ("he2 is tall male\n")
else:
    print ("he2 is either nor male or not tall or both")
'''
'''
def max_num (num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print (str(num1) + " is the largest")
    elif num2 >= num1 and num2 >= num3:
        print (str(num2) + " is the largest")
    else:
        print (str(num3) + " is the largest")

max_num (7, 212, 3)
'''

# 12
# Building a better Calculator_____________________________

'''
num1 = float (input ("Enter first number:"))
# Usually kalo kita get input dari user bakal dibaca sbg string, makanya kudu diconvert inputnya ke float or int

op = input ("Enter the operator: ")
num2 = float (input ("Enter second number:"))

if op == '+':
    print (num1 + num2)
elif op == '-':
    print (num1 - num2)
elif op == '*':
    print (num1 * num2)
elif op == '/':
    print (num1/num2)
else:
    print ("Invalid. you should use + - * or /")
'''

# 13
# Dictionary_______________________________________________________

# Semacam structure di python buat ngebantu kita untuk stor info (KEY VALUE PAIR)
# di kamus ada 2 item -> 1. word dan 2. definition associated to that word
# di case ini, 1. key = word, 2. value = definition
# pake CURLY BRACKET!

# Task
# Jan -> January
# Mar -> March
# 4 -> April (kita bisa pake number buat key, as long as it uniques)

'''
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    4 : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
}

print (monthConversions["Jul"])
print (monthConversions.get("Jul"))

# bisa pake box bracket bisa pake .get function
# kalo pake .get function, kita bisa specify a default value kalo key not found

print (monthConversions.get("Lov", "Key ini gak ada di library"))
print (monthConversions.get(4))
'''

# 14
# While Loop_______________________________________________________

'''
i = 1
while i <= 10:
    print (i)
    # i = i + 1
    i += 1

print ("\nDone with loop\n")
'''

# 15
# Build A Guessing Game____________________________________________

secret_word = "fuad"
guess = ""

while guess != secret_word:
    guess = input("Type the secret word: ")

print ("Bener!")

# Now at 2:23:56
