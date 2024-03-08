#Emmanuel Velazquez
#3/7/24

#Problem 4:This program determines if a given year is a leap year

def leap_year(input_year):
    if input_year % 4 ==0:
        if input_year % 100 ==0:
            if input_year % 400 ==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year_to_Check = int(input("What year would you like to check?"))

if leap_year(year_to_Check):
    print(year_to_Check, "is a leap year")
else:
    print(year_to_Check, "is not a leap year")