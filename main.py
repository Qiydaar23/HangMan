from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from random import randint
from os import system, name
from pyfiglet import figlet_format
from ascii import welcome
from ascii import man

Base = declarative_base()

def getWord():
    word_bank = ["flatiron", "codekids", "consolelog" , "raccoon","terminal","vscode","github"]
    return word_bank[randint(0, len(word_bank)-1)]

def drawMan(incorrect):
    if incorrect == 0:
        print("\n+---+") 
        print("     ⛓️")
        print("     ⛓️")
        print("     ⛓️")
        print("    ===")
    if incorrect == 1:
        print("\n+---+") 
        print("🪝   ⛓️")
        print("      ⛓️")
        print("     ⛓️")
        print("    ===")
    if incorrect == 2:
        print("\n+---+") 
        print("🪝  ⛓️")
        print("🥴  ⛓️")
        print("     ⛓️")
        print("     ⛓️")
        print("    ===")  
    if incorrect == 3:
        print("\n+---+") 
        print("🪝  ⛓️") 
        print("🥴  ⛓️")
        print("👕  ⛓️")
        print("     ⛓️")
        print("    ===") 
    if incorrect == 4:
        print("\n+---+") 
        print("🪝  ⛓️")
        print("🥴  ⛓️")
        print("👕  ⛓️")
        print("👖  ⛓️")
        print("   ===")
    if incorrect == 5:
        print("\n+---+") 
        print("🪝  ⛓️")
        print("🥴  ⛓️")
        print("👕  ⛓️")
        print("👖  ⛓️")
        print("👞 ===")
           
    if incorrect == 6:
        print("\n+---+") 
        print("🪝  ⛓️") 
        print("🥴  ⛓️")
        print("👕  ⛓️")
        print("👖  ⛓️")
        print("👞👞 ===")
           
    if incorrect == 7:
        print("\n+---+") 
        print("🪝   ⛓️")
        print("💀  ⛓️")
        print("👕  ⛓️")
        print("👖  ⛓️")
        print("👞 ===")
        print("      ")
        print("     👞")
         
def play():
    word = getWord()
    progress = ""   
    for i in range(len(word)):
        progress += "_" #make word bank blink
    print(progress)
    incorrect = 0
    guesses = []
    while True:
        _ = system("clear")
        guessesString = ""
        for i in range(len(guesses)):
            guessesString += guesses[i] # guesses string that was guessed
        print(f"Past guesses: {guessesString}")
        drawMan(incorrect) 
        if progress == word: # if they guess all letter correct
            print(progress)
            print("🏃💨💨💨")
            print(f"{word} is correct")
            print("🏆🏆You Won!!! , You Have Escaped🏆🏆")
            break
        if incorrect >= 7:
            print("You lose")
            print(f"the word was {word}.")
            print(man)
            break
        print(progress)
        print("Guess a letter")
        guess = input()
        if guess not in guesses:
            guesses.append(guess)
        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    progressStart = progress[0:i]  #split
                    progressEnd = progress[i+1:]
                    progress = progressStart + guess + progressEnd # getting the split letter 
        else:
            incorrect += 1 # this is if the guess is not in the word increase the number of incorrect            
if __name__ == '__main__':
    while True:
        print(welcome)
        print("🪝   DO YOU WANT TO PLAY HANGMAN? ENTER (YES/NO)   🪝")
        print("LOADING.....⌛")
        answer = input()
        if answer == "yes":
            play()
        if answer == "no":
            print("Boooooo!!!!! 🪝  GoodBye") 
            print(man) 
            break
            
        