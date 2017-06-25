import random
anwser = random.randint(1,10)
#anwser = 5
i = 0
while i < 3:
    if i == 0:
        num = int(input("please enter a number:"))
    else:
        num = int(input("please try again:"))
    if num > anwser:
        print("too big")
    elif num < anwser:
        print("too small")
    else:
        print("Correct")
        break
    i += 1
print("game over\n")
