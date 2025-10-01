import random
secret_number = random.randint(1,10)
attempt = 0
max_attempt = 4

while attempt < max_attempt :
    attempt = attempt + 1
    user_num = int(input("Enter the secret number bwtween 1 to 10: "))

    if user_num == secret_number :
        print("Damnnnn !! , You got it", user_num ,"was the secret number.")
        break
    
    print("You got it wrong !. You have", max_attempt-attempt, "attempt left.")

print("Secret number was :",secret_number)
if max_attempt == attempt and secret_number != user_num:
    print("Game Over !")