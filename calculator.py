# Requirements:
# - Ask user for two numbers
# - Ask which operation (+, -, *, /)
# - Show the result
# - Use if/elif/else to handle different operations
# - Use a while loop to keep asking "Do you want to calculate again?"

num_1 = int(input("Enter the first number : "))
num_2 = int(input("Enter the second number : "))

operator = input("Enter the operator : ")

if operator == "+" :
    result = num_1 + num_2

elif operator == "-":
    desicion = input("Enter from which number you want to subtarct bigger or smaller :")
    if desicion == "smaller":
        if num_1<num_2:
            result = num_1 - num_2
        else:
            result = num_2 - num_1
    
    elif desicion == "bigger":
        if num_1>num_2:
            result = num_1 - num_2
        else:
            result = num_2 - num_1
    
    else:
        print("Invalid Command ! , Please Press Q to request for help !")

elif operator == "*":
    result = num_1 * num_2

elif operator == "/":
    desicion = input("You want to divide from smaller number or the bigger number ?") 
    if desicion == "smaller":
        if num_1<num_2:
            result = num_2 / num_1
        
        else:
            result = num_1 / num_2
        
    
    if desicion == "bigger":
        if num_1>num_2:
            result = num_2 / num_1
        
        else:
            result = num_1 / num_2
    else:
        print("Invalid Command ! , Please Press Q to request for help !")

print("Here is the result : ", result)
