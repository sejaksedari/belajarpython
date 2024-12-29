# CEK ELEMEN A yang NGGAK ADA di B

# __________________________________
# Overall Idea:  bikin array foundNum, bikin array notFoundNum pake status exists.
# Removes duplicate from an array

numbersA = [8, 5, 4, 8, 6, 2, 0]
numbersB = [2, 3, 8, 4, 6, 1, 9]
foundNum = []
notFoundNum = []

# Cari nomor yang nggak ada di numbersB tapi ada di numbersA
for x in numbersA:
    # Set semua status nomor A jadi False
    exists = False
    # kalo ada di B sama kyk A, masukin dia ke foundNum, exist jadi True
    for y in numbersB:
        if(x == y):
            foundNum.append(x)
            exists = True
    # kalo status exist tetep false, masukin ke notFoundNum
    if (exists == False):
        notFoundNum.append(x)

print("numbersA:")
print(numbersA)
print("notFoundNum:")
print(notFoundNum)

# Go use this https://pythontutor.com/



# __________________________________
# Overall Idea: Bikin imaginary array notFoundNum2 = numbersA2 - foundNum2
# alternative way
numbersA2 = [8, 5, 4, 8, 6, 2, 0]
numbersB2 = [2, 3, 8, 4, 6, 1, 9]
foundNum2 = []
notFoundNum2 = []

# Bikin array foundNum2
for x in numbersA2:
    exists2 = False
    for y in numbersB2:
        if(x == y):
            foundNum2.append(x)
            exists2 = True
print("numbersA2:")
print(numbersA2)

# Bikin array notFoundNum2 = numbersA2 - foundNum2
for x in foundNum2:
    for y in numbersA2:
        if(x == y):
            numbersA2.remove(y)
print("notFoundNum2:")
print(numbersA2)



# CEK ELEMEN B yg NGGAK ADA di A
numbersA3 = [8, 5, 4, 8, 6, 2, 0]
numbersB3 = [2, 3, 8, 4, 6, 1, 9]
foundNum3 = []
notFoundNum3 = []



# Print numbersB
for x in numbersA3:
    exists3 = False
    for y in numbersB3:
        if(x == y):
            foundNum3.append(x)
            exists3 = True
        if(exists3 == False):
            notFoundNum3.append(x)
print("numbersB3:")
print(numbersB3)

# Cek, elemen A yg sama dengan B, kalo ada, remove dia dari elemen B
for x in numbersA3:
    for y in numbersB3:
        if(x == y):
            numbersB3.remove(y)
print("notFoundNum3:")
print(numbersB3)

# Lesson Learned
    # Don't remove elements from the parent if array
    # Because it will delete its index for modifying (delete) the child 