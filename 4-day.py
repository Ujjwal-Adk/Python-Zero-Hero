# Today we will learn about the if else statement 

age = int(input("Hi User , Please input your age here : "))

if age>=18 and age<=40 :
    print("You are adult !")
elif age>40 and age<=60 :
    print("You are uncle and aunts")
elif age>60 and age<=100 :
    print("You are old hags")
elif age>100:
    print("You don't even exist. Are you an alien ?")
else:
    print("you are minor")

# Holy cow ! Came to know that "and" and "&" are different and is logical operator and & is bitwise operator 