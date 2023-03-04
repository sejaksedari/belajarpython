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


