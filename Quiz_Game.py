print("Welcome to my computer Quiz!")
# input makes the content inside the brackets interactive
playing = input("Do you want to play?")
# != not equal to - this symbol allows us not to use else or elif because it makes anything other than yes quit the game
if playing.lower() != "yes":
    quit()                                                                 #can't use break cause u use break in a loop
print("Okay! Let's play  :)")
score = 0

answer = input("What does CPU stand for? \n a) central processing unit b)central  \n c) process d) unit \n Answer: ")
if answer.lower() == "a":  #“\n” is used to create a new line. When inserted in a string all the characters after the character are added to a new line.
    print("Correct!")
    score += 1
else: print("Incorrect!")

answer = input("What does GPU stand for? \n a)graphics b)graphics processing unit \n c)processing d)unit \n Answer: ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GUI stand for? \n a)graphics b)user \n c)graphics user interface d)interface \n Answer: ")
if answer.lower() == "c":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? \n a)random b)acess \n c)memory d)random acess memory \n Answer: ")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ROM stand for? \n a)random b)random acess memory \n c)acess d)memory \n Answer: ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does RIT-K stand for? \n a)AUK b)Rochester \n c)College d)rochester institute of technology - kosovo \n Answer: ")
if answer.lower() == "d":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CIT stand for? \n a)IT b)computer information technologies \n c)information d)technology \n Answer: ")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
#print("You got" + str((score/7)*100)+%)
print("Your Score = ",round((score/7)*100),"%")






