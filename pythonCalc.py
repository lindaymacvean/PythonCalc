#Python Calculator

#Calculator

print("-- [Calculator] --")

#Breaker
print(' ')
#Breaker

#Notify
print("© Calulator - 2013 - Noah Coleman")

#Breaker
print(' ')
#Breaker

#The First Number
numberOne = int(input("Enter a Number : "))

#Breaker
print(' ')
#Breaker

#The Second Number
numberTwo = int(input("Enter another Number : "))

#Breaker
print(' ')
#Breaker

#Selecting a Statement
statementInput = input("Select a Statement (/ , *, +, -): ")

#Breaker
print(' ')
#Breaker

#Variables for the Sums
variableDivison = numberOne/numberTwo
variableMultiply = numberOne*numberTwo
variableAddition = numberOne+numberTwo
variableSubtraction = numberOne-numberTwo

#Getting the Statement input
if statementInput == '/':
    print(variableDivison)

    #Breaker
    print(' ')
    #Breaker

if statementInput == '*':
    print(variableMultiply)

    #Breaker
    print(' ')
    #Breaker

if statementInput == '+':
    print(variableAddition)

    #Breaker
    print(' ')
    #Breaker

if statementInput == '-':
    print(variableSubtraction)

    #Breaker
    print(' ')
    #Breaker
