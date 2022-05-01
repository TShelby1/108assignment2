#imports

#global variables

#functions
def print_menu():
    print("**py calc")
    print("----------")
    print("[1] Sum")
    print("[2] Difference")
    print("[3] Multiplication")
    print("[4] Division")

def sum(num1, num2):
    result = num1 + num2
    print("Result is: "+ str(result))

def difference(num1, num2):
    result = num1 - num2
    print("Result is: "+ str(result))

def multiplication(num1, num2):
    result = num1 * num2
    print("Result is: "+ str(result))

def division(num1, num2):
    if num2 ==0:
        print("Result is: "+ str(result))
    else:
        result = num1 / num2
        print("Result is: "+ str(result))


#plain instructions, instruction that goes outside function

print_menu()

opt = input("Please select and option: ") #this is a string

num1 = float(input("Please provide num1: "))
num2 = float(input("Please provide num2: "))

#need to parse string to float
if opt =="1":  #make it a string so the input can read a string
    sum(num1, num2)
elif opt =="2":
    difference(num1, num2)
elif opt =="3":
    multiplication(num1, num2)
elif opt =="4":
    division(num1, num2)
