
# Make addition and substraction function (def)
def Process(var1, var2):
    if(var1 > var2):
        finalValue = var1 - var2
    else:
        finalValue = var1 + var2
    return finalValue

num1 = 60
num2 = 50
print("num1 = ", num1, ",", "num2 = ", num2, "Processing Result :", Process(num1, num2))


# Print out the even numbers with Loop, then the odd
EvenNum = []
OddNum = []

# While Loop
x = 0
while x < 10:
    if(x % 2 == 0): #modulus
        EvenNum.append(x)
        # print(str(x) + " is an even num")
    else:
        OddNum.append(x)
        # print(str(x) + " is an odd num")
    x = x+1

print("These are even Num", EvenNum)
print("These are odd  Num", OddNum)
