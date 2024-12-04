name = input("hello whats your name?:")                       #asks for name via input feature 
print("your name is " + name )                                #prints text "" + variable which in this case is the name
age = input("whats your age?")                                #asks for age via input feature 
print("your age is " + age)                                   #prints the name + variable same as with the name
startyn = input("do you want to start (y/n)?")                #asks user if it wants to start, y continues the script and n ends the script
if startyn == "y":                                            #if statement that means yes that then starts the code
    print("hello")                                            #prints welcome messages
    print("welcome")
    startyes = "y"
    print("welcome to my calculator")
    num1 = float(input("select your number"))                 #this starts the calculator and uses float input feature that lets us calculate the number without a string
    print(num1)                                               #prints out the input
    num2 = float(input("select your 2nd number"))             #same thing but for number 2 
    print(num2)
    operation = input("select your operation ( +, -, :)")     #asks for calculation operation that then has if and elif statements 
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == ":":
        result = num1 / num2
    print(result)                                             #all variables here are called result and are as it says, they are the result of the calculation

    made_by = "kamil"                                         #simple credit list
    python_version = " python version 3.10"                    
    credits = input("do you want to see the credits? (y/n)")
    if credits == "y":
        print(made_by + python_version)

    again = input("do you want to start again? (y/n)?")
    if again == "n":
        print("thanks for trying it out")
        
        
        

if startyn == "n":
    print("bye")
