
#CATETANZ

    #BOOLEAN

        # >
        # <
        # == equal to
        # != not equal to
        # >= greater than or equal to
        # <= less than or equal to

    #Test1
'''
x = 10
y = 12

print(x > y)
print(x < y)

print(x == y)
print(x == 10)

print(x != y)
print(x != 10)

print(x >= 10)
print(x >= 20)

print(x <= y)
print(x <= 10)
'''

    #Test2_and_OPERATOR
'''
print(True and True)
print(True and False)
print(False and False)
'''

    #Test3_or_OPERATOR
    #at least 1 value True, all will be True
'''
a, b, c = 1, 2, 3
print(b > a or c > a)
print(b > a or c < a)
print(b > a or b > c)
'''

    #Test4_not_OPERATOR
'''
print(not True)
print(not False)

x = 5
print(not (x ==5 ))

'''

    #IF_ELSE_Statement

        #IF_SYNTAX
        #if boolean_expression:
        #    statement(s)
        
        #jadi sebelum "statement" ada indentation 1 tab
        #if the boolean_expression evaluates to True, the body of the if statement is EXECUTED
        #if the boolean_expression evaluetes to False, the body of the if statement is SKIPPED

#Example1_IF
'''
numb = 100

if numb > 0:
    print("Number", numb, "is positive")

'''


    #IF_ELSE_SYNTAX
        #if boolean_expression:
        #   statement(s)
        #else:
        #   statement(s)

        #Jadi the program bakal evaluates the boolean_expression first
        #if the boolean_expression evaluates to True, the body of the if is executed
        #if False, the body of else is executed

#Example2_IF_ELSE
'''
numb = -3

#boolean expression results to True
if numb >= 0:
    print("The number", numb, "is Positive or Zero")
    print("The body of if is executed")

else:
    print("The number", numb, "is considered as negative")
    print("The body of else is executed")
'''

    #IF_ELIF_ELSE_SYNTAX
    
        #elif itu else if disingkat wkwk
        #there can be 0 or more elif parts

        #if boolean_expression1:
        #   statement(s)
        
        #elif boolean_expresion2:
        #   statement(s)
        
        #elif boolean_expression3:
        #   statement(s)

        #else boolean_expression4:
        #   statement(s)


#Example3_ELIF
'''
num = -123

if num > 0:
    print("positive number")
elif num == 0:
    print("is zero")
else:
    print("negative")
'''

    #NESTED_IF_ELSE
    #kita bisa punya if else di dalem if lese (namanya nesting kalo di computer science)

'''
num = float(input("Enter a number: "))

if num >= 0:

    if num == 0:
        print("Zero")
    
    else:
        print("positive")

else:
    print("negative")

'''

#Example4_SIMPLE_CALCULATOR

