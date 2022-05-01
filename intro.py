# Name + Variable = Syntax. Dont use "let,const"
print("Hello world")

name = "Albert" #string
last_name = "Lara" #string
age = 100 # integer
total = 23.784 #decimal
found = False #boolean

print(name, last_name, age, total, found)

#if statement, testing age. There is a seperation between the if and the parameters being passed through. The print is right below the age. Instead of else, its elif. *****When you use the colon that is indicating a start of the code, so whats underneath it has to have a space******

#code blocks

if (age < 100):
    print("You are old")
elif (age ==100): #else if combined
    print("Congrats on the century")
else: 
    print("troiher")

#functions, we use def to define a function of code. Need to execute a function, same as in javascript

def say_hello():
    print("Hello")
    print("Im inside a function")

say_hello()
say_hello()