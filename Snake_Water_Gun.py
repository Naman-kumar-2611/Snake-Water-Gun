# Snake Water Gun
import os
import random
import time

computer = {'G': 'S', 'W': 'G', 'S':'W'}


f = open('SNG_Data.txt','r+')   
    
if f.read() == "":
        f.write('0')
        f.seek(0)     
    
def computerChoice():
    CompOptions = ['S','W','G']
    return random.choice(CompOptions)

HighScore = 0

while True:
    f.seek(0)
    EverScore = int(f.read())
    os.system('clear')
    print(f"High Score : {HighScore} | Highest Score Ever : {EverScore}")
    
    UserChoice = input("Enter a choice (S/W/G) : ").upper()
    compChoice = computerChoice()
    if UserChoice.upper() not in ['S','W','G']:
        print("Invalid Input!")
        time.sleep(5)
        continue
    
    os.system('clear')
    print(f"High Score : {HighScore} | Highest Score Ever : {EverScore}")
    print(f"Computer Chose: {compChoice} | You chose : {UserChoice}")
    if UserChoice is compChoice:
        print("Draw!")
    
    elif computer[compChoice] == UserChoice:
        print("Computer Wins! Game Over!")
        time.sleep(5)
        break
            
    else:
        print("You Won! Congratulations!")
        HighScore += 1
        if HighScore > EverScore:
            f.seek(0)
            f.write(str(HighScore))
    time.sleep(5)
        
f.close()