# SO this is all about the loops 

count = 1

while count <= 5 :
    print("Count is :" , count)
    count = count + 1
    
print("Loop is finishesd ! did you got is ?")

# Break and continue statement in loop 

new_value = 1 

while new_value <=10:
    print(new_value)
    if new_value == 3:
        print("Breaking at 3 !") # When the condition is satisfied loop will this if statement will let loop end.
        break
    else:
        print("Loop continues !", new_value ,"times")
    new_value = new_value +1

second_value =1

while second_value <5:
    second_value = second_value +1 
    
    if second_value == 3:
        print("The number three will be skipped ")
        continue
    print(second_value)