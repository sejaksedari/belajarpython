
# INGET GOALS BELAJAR PYTHON
# Buat understanding logical thinking buat dipake scripting or Automation tools di Blender, Unreal Engine, Houdini, dan Nuke . Jadi next abis paham basic2nya, lgsg cari tutorial Python for "Software Context"
# Long Term Goal --> LookDev or TD @WetaFX
# Course link: https://www.youtube.com/watch?v=LWIzgB8NOyk&list=PLZS-MHyEIRo59lUBwU-XHH7Ymmb04ffOY&index=60&ab_channel=KelasTerbuka

# ///////////////////////
# NOW: 4 Variable


# ///// 1 APA ITU PYTHON________________________________________________________________________ 
    # Hello Update Nih

# ///// 3 CARA KERJA PROGRAM DAN BYTECODE_______________________________________________________
    # python itu bahasa pemrograman yg interpreted, jd lgsg run tanpa kudu bikin compiled versionnya
    # Interpreted
        # Source code: "OpenClass_python.py" -> Interpreter: "Python 3.10.6" -> Terminal/Dijalankan
    # Compiled
        # Source code -> Compiler: C++ -> .exe
    # kita bisa ngompile python ke BYTECODE (compiled version of python, mirip cara kerja compiled code .exe, lebih efisien). kalo ditampilin di interpret biasanya makan waktu buat translasi. nah, kalo dicompile ke bytecode. runningnya lebih kentjeng. YANG DICOMPILE bakal lebih CEPET drpada yg di INTERPRET. Nanti jadi .pyc frmat filenya
        # ketik di terminal buat compile: python -m py_compile (namafile).py
        # masuk ke folder __pycache__: cd __pycache__
        # Cara run compiled pyc code: python (namafile).cpython-(nomorygtertera).pyc

    # Cara run py code: atau py "namafile.py"
    # Cara cek versi Python di terminal = "python --version"
    # single line comment: # (commented line)
    # multi line comment: ''' (commented multiline) '''
    # cara mindahin line code: alt + arrow
    # cara copy past line code: alt + + shift + arrow


# ///// 4 MENGENAL VARIABLE_______________________________________________________________
# Ternyata >>> itu Shell
    # caranya masuk shell tinggal ketik py terus enter, keluarnya CTRL + Z terus enter
# Variable Assignment
    # di Python, ga ada variable declaration kyk JS misal int a = 2, let b = "big", jadi langsung assignment 
# Varibale Naming
    # 10juta =  10000000 # angka ga boleh di depan
    # juta 10 = 10000000 # ga boleh ada spasi

# Example

'''
# Variable Assignment
a = 10 # a adalah variable dengan value 10
x = 5
panjang = 1000
sepuluhjuta = 10000000

# Pemanggilan Pertama
print ("nilai a =", a)
print ("nilai x =", x)
print ("nilai panjang =", panjang)
print ("sepuluhjuta =", sepuluhjuta)

# Pemanggilan Kedua var a
print ("nilai a =", a)

# Direct Assignment  Variable a di tengah2
a = 7

# Pemanggilan Ketiga var a, berubah jadi 7
print ("nilai a =", a)

# Indirect Assignment var a to var b
b = a
print ("nilai b =", b)

'''


# ///// 5 TIPE DATA___________________________________________________________________


# """
data_integer = 1
a = 1
b = 1.2
c = "1"
d = "satu 1"
e = True
f = complex(5,6) # complex numb, complex(realnumb, imaginer), 5+6j

# manggil or import tipe data dari C language
from ctypes import c_double, c_char, c_long

g = c_double(10.581249182317391)

print("data: ", data_integer, "bertipe: ", type(data_integer))
print(type(a)) #int
print(type(b)) #float
print(type(c)) #string
print(type(d)) #string
print(type(e)) #bool
print("data: ", f, "bertipe: ", type(f)) #complex 5 + 6j
print("data: ", g, "bertipe: ", type(g)) #ctypes.c_double
# """

# ///// 6 ________________________________________________________________________
# Casting Tipe Data
# Merubah suatu tipe data ke tipe data lain
# https://github.com/kelasterbuka/Python3.x_Dasar_Programming/blob/master/Episode%2006%20-%20Casting%20Tipe%20Data/Main.py 

'''
data_int = 9
print("data = ", data_int, ",type = ", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # false kalo nilai integer 0

print("___CASTED___")
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))

# buat string, kalo mau dicast jadi int float atau bool harus berupa angka, bukan text
'''

# ///// 7 ________________________________________________________________________
# Get Input from User

# data yg dimasukin pasti string
# kalo mau ambil int or float , convert string tadi ke int or float
# kalo mau ambil true false or boolean, pake 1 0 biner aja

'''
biner = bool(int(input("masukan nilai boolean (1 = True / 0 = False): ")))
print("data = ", biner,", type=", type(biner))
'''

# ///// 8 ________________________________________________________________________
# Arithmetic Operation

'''
# operasi aritmatika
# variable declaration
a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,"+",b,'=',hasil)

# operasi pengurangan -
hasil = a - b
print(a,'-',b,'=',hasil)

# operasi perkalian *
hasil = a * b
print(a,'*',b,'=',hasil)

# operasi pembagian /
hasil = a / b
print(a,'/',b,'=',hasil)

# operasi eksponen (pangkat) **
hasil = a ** b
print(a,'**',b,'=',hasil)

# operasi modulus %
hasil = a % b
print(a,'%',b,'=',hasil)

# operasi floor division //
hasil = a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, operational precedence

#    1. ()
#    2. exponen **
#    3. perkalian dan teman-teman * / ** % //
#    4. pertambahan dan pengurangan + -

x = 3
y = 2
z = 4

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z 
print('(',x,'+',y,') *',z,'=',hasil)
'''

# ///// 9 ________________________________________________________________________
# Latihan Program Perhitungan Sederhana

# TEMPERATURE CONVERSION

'''
print("Welcome to Temperature Conversion Program!")

celcius_temp = float(input("Insert temperature in Celcius: "))
print("\n")

kelvin_temp = celcius_temp + 273.15
print(celcius_temp, "C, is equal to", kelvin_temp, "Kelvin\n")

farenheit_temp = (celcius_temp * (9/5)) + 32
print(celcius_temp, "C, is equal to", farenheit_temp, "Farenheit\n")

reamur_temp = (celcius_temp * (4/5))
print(celcius_temp, "C, is equal to", reamur_temp, "Reamur\n")

print("Thank You! Hope It Helps!")
'''

# ///// 10 ________________________________________________________________________
# Comparation Operation

# setiap HASIL dari operasi komparasi itu BOOLEAN
# >,<,>=,<=,==,!=
    # semua ini bisa bekerja pada syntax LITERAL
    # misal a == 4, a -> ada nilainya, sebuah variable, makan memory, 4 -> LITERAL, lgsg tertulis, ga ada variabelnya, ga makan memory

# is,is not
    # mereka membandingkan objek (Coba cek materi OOP)
    # a = 4, b = 4
    # a is b = True
    # jadi is itu makan memory banget, tapi lebih customizable 

'''
a = 4
b = 2

# lebih besar dari >
print('========== lebih besar dari (>)')
hasil = a > 3
print(a,'>',3,'=',hasil)
hasil = b > 3
print(b,'>',3,'=',hasil)
hasil = b > 2
print(b,'>',2,'=',hasil)

# tidak sama dengan (!=)
print('======== tidak sama dengan(!=)')
hasil = a != 4
print(a,'!=',4,'=',hasil)
hasil = b != 4
print(b,'!=',4,'=',hasil)

# 'is' sebagai komparasi object identity
print('======== object identity(is)')
x = 5 # ini adalah assignment membuat object
y = 5
print('nilai x =',x,',id = ',hex(id(x)))

# IMPORTANT NOTE
# hex(id(x) nampilin address hex number, ini jadi alat perbandingan karena si hex ini itu identitas dari si integer. Jadi kalo ada data sama misal sama2 5 yg di x dan y. 5 nya itu masuk ke id memory yang sama.

print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)

x = 5 # ini adalah assignment membuat object
y = 6
print('nilai x =',x,',id = ',hex(id(x)))
print('nilai y =',y,',id = ',hex(id(y)))
hasil = x is y
print('x is y =',hasil)
'''


# ///// 11 ________________________________________________________________________
# Operasi Logika Boolean

'''
# NOT
a = False
c = not a
print('data a =', a)
print('data c =', c)

# OR - At least salah satu true
a = False
b = False
c = a or b
print(a, 'or', b, '=', c)
a = True
b = False
c = a or b
print(a, 'or', b, '=', c)

# AND - 22nya must be True for return True

# XOR - True kalo SALAH SATU SAJA TRUE,
print("\n") 
print('====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)
'''

# ///// 12 ________________________________________________________________________
# Latihan Komparasi dan Logika

# SOAL 1
# ++++++3--------10+++++++

# Jawaban 1A
'''
UserInput = float(input("Masukkan angka kurang dari 3 or lebih dari 10: "))
if( 3 < UserInput and UserInput < 10):
    print(False)
elif(UserInput == 3):
    print(False)
elif(UserInput == 10):
    print(False)
else:
    print(True)
'''

# JAWABAN 1B
'''
UserInput = float(input("Masukkan angka kurang dari 3 or lebih dari 10: "))

IsLower = (UserInput < 3)
IsUpper = (UserInput > 10)
if(IsLower or IsUpper):
    print("Anda Benar! Angka ", UserInput, "lebih kecil dari 3 atau lebih besar dari 10")
else:
    print("Anda Salah")
'''

# SOAL 2
# -------0++++++5--------8++++++11----------
# 0 False, 0.2 True, 9 True, 11 False

# JAWABAN 2A
'''
UserInput = float(input("Masukkan angka antara (0 dan 5) atau (8 dan 11): "))
if( 0 < UserInput < 11):
    if( 5 < UserInput < 8):
        print (False)
    elif(UserInput == 5):
        print(False)
    elif(UserInput == 8):
        print(False)
    else:
        print(True)
else:
    print(False)
'''

# +++++++0-------5+++++++8-------11+++++++
# JAWABAN 2A

'''
UserInput = float(input("Masukkan angka antara (0 dan 5) atau (8 dan 11): "))
if( 0 < UserInput < 11):
    if( 5 < UserInput < 8):
        print (True)
    elif(UserInput == 5):
        print(False)
    elif(UserInput == 8):
        print(False)
    else:
        print(False)
elif(UserInput == 0):
        print(False)
elif(UserInput == 11):
        print(False)
else:
    print(True)
'''

# ///// 13 ________________________________________________________________________
# Operator Bitwise
# BARU SAMPE SINI





# ///// 58 ________________________________________________________________________
# Standard Library 
'''
import datetime

data_waktu = datetime.datetime.now()
print(data_waktu)
print(f"Datetime now: {data_waktu}")
print(f"Tahun: {data_waktu.year}")
print(f"Hari : {data_waktu.strftime('%A')}")

# QNA | kenapa kok ada f di sebelumnya printf string?

data = ["a", "b", "c", "d", "e", "a", "g", "a", "e", "d"]

count = 0
for i in data:
    if i == "a":
        count += 1

print("Jumlah a: " + str(count) + "\n")

# coba pake module data count buat do something similar. Ngapain kita bikin dari scratch kalo emg udah disediain di Python wkwkwk

from collections import Counter

data_count = Counter(data)

print(f"data count = {data_count}\n")
print(f"jumlah a = {data_count['a']}\n")
print(f"jumlah d = {data_count['d']}\n")

'''