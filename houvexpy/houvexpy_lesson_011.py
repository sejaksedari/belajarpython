
# list nilai tiap subjects
numbers = [80, 45, 44, 78, 64, 56, 99]

totalScore = 0
average = 0

for x in numbers:
    totalScore = totalScore + x

average = totalScore/len(numbers)
print("the total score is", totalScore)
print("average score", average)
