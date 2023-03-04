
#What is a Loop?
#In programming, a loop is used to repeat a block of code
#as long as the boolean expression is True


#WHILE LOOP = the body of the while loop is executed as long as the boolean expression is True
#SYNTAX
#while boolean_expression:
#   statement(s)

#Example
'''
n = 3
i = 1

while i <= n:
    print("Loop is easy.")
    i = i + 1 #i is increased by 1 in the end of each loop
'''

#Example_Infinite_While_Loop

''' contoh infinite while loop 1
n = 3
i = 1

while i <= n:
    print("Loop is easy.")
    print("Infinite loop is also easy")
'''

''' contoh infinite while loop 2
while True:
    print("Loop is easy.")
    print("Infinite loop is also easy")
'''

''' contoh infinite while loop 3
i = 1

while i <= 5:
    print("Loop is easy.")
    i = i - 1
'''

#Example_Sum_Loop

''' contoh pake sum gabungan while loop
n = 3

# sum will sum 1 + 2 + 3 + ... + n, where n is a positive integer
# di case ini kalo n = 3, berarti sum = 1 + 2 + 3 = 6 (Output)
sum = 0
i = 1

while i <= n:
    sum = sum + i #sum function bakal looping dan ngejumlah i baru dan sum sebelumnya
    i = i + 1 #update counter

print("The sum is", sum)
'''

#WhileLoop_With_Else

#a while loop can have an optional else block
#the else part is executed after the condition in the while loop evaluates to False
'''
counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1

else:
    print("Inside else")
'''

#Example_MultiplicationTable

n = 12
i = 1

while i <= 10:
    print(n,'x', i, '=', n*i)
    i =  i + 1