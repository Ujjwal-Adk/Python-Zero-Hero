# WElcome to day 3 here we will learn to compare the values 

a = 10 
b = 5

print("Is a equal to b?", a==b)

print("Is a not equal to b?", a!=b)

print("Is a greater than b", a>b)

print("Is a smaller than b", a<b)

print("Is a greater or equal to b ?", a>=b)

print("Is a smaller or equal to b ?" , a<=b)

# SO = is for assigning values and then == is for comparing values 

# Now we will learn about changing the data types 

text_number = "404"
# So the above mumber is in text form right now I mwan string 
print(type(text_number))

# To change it to the Int or float we have to do this 
real_number = int(text_number)
# This is now integers
print(type(real_number))

real_number = float(text_number)
# This is now float = decimal values 
print(type(real_number))

# Changing to String again 
evo_text_number = str(real_number)
print(type(evo_text_number))

pie = 3.14
changed_value_pie = int(pie)
print(changed_value_pie)
print(type(changed_value_pie))

#SO things to remember is that you cant change the any names type of string to float and int and if there is decimal value in any string then we cant chnage that to string 