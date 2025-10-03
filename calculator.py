# Simple Calculator with Repeat Option

# Start the while loop
continue_calculating = "yes"

while continue_calculating == "yes":
    
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    
    operator = input("Enter the operator (+, -, *, /): ")
    
    if operator == "+":
        result = num_1 + num_2
    
    elif operator == "-":
        decision = input("Subtract from bigger or smaller number? ")
        if decision == "smaller":
            if num_1 < num_2:
                result = num_1 - num_2
            else:
                result = num_2 - num_1
        
        elif decision == "bigger":
            if num_1 > num_2:
                result = num_1 - num_2
            else:
                result = num_2 - num_1
        
        else:
            print("Invalid command!")
            result = "Error"
    
    elif operator == "*":
        result = num_1 * num_2
    
    elif operator == "/":
        decision = input("Divide bigger by smaller or smaller by bigger? ")
        if decision == "smaller":
            if num_1 < num_2:
                result = num_2 / num_1
            else:
                result = num_1 / num_2
        
        elif decision == "bigger":  # ✅ Fixed: was 'if', now 'elif'
            if num_1 > num_2:
                result = num_2 / num_1
            else:
                result = num_1 / num_2
        
        else:
            print("Invalid command!")
            result = "Error"
    
    else:
        print("Invalid operator!")
        result = "Error"
    
    # Show result
    print("Result:", result)
    print("---")
    
    # Ask if user wants to continue
    continue_calculating = input("Do you want to calculate again? (yes/no): ")
    continue_calculating = continue_calculating.lower()  # Makes "Yes", "YES" work too

print("Thanks for using the calculator!")