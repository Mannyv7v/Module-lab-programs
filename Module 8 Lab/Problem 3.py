#Emmanuel Velazquez
#3/7/24

#Problem 3: This function will tell you if the value 5 is in a list
def has_5_in_list(input_list):
    return 5 in input_list

#user can create list to be anything
my_list = (1,4,6,3,6,7,20)
result = has_5_in_list(my_list)

if result:
    print("5 appears in this list!")
else:
    print("5 is not in this list")

