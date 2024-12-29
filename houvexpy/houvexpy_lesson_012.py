# Nested Loops Exercise
# Pake cara selain dari yg dicontohkan

numbersA = [8, 5, 4, 8, 6, 2, 0]
numbersB = [2, 3, 8, 4, 6, 1, 9]
foundNum = []
notFoundNum = []

# Iterate through each element in numbersA
for i in numbersA:
    if i in numbersB and i not in foundNum:  # Check if element is in numbersB and not already in foundNum
        foundNum.append(i)
    elif i not in numbersB:  # Only add to notFoundNum if it's not in numbersB
        notFoundNum.append(i)

# Print results
print("Found numbers:", foundNum)
print("Not found numbers:", notFoundNum)