#Emmanuel velazquez
#03/7/24

#problem 2: This program takes 2 inputs and lets the user if the sum of the two are greater, less than, or equal to 10
def checkIf10(x,y):
    if x + y <10:
        print("Sum of values is less than 10")
    elif x + y >10:
        print("Sum of values is greater than 10")
    else:
        print("These values equal 10")
#User can input any interger for x and y
checkIf10(5,1)
