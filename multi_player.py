from random import randint
from os import system, name
from ascii import welcome



# gameRunning = True
# p1turn = True
# p2turn = False

# while gameRunning:
#     #player1
#     while p1turn:
#         input("Player 1 Turn\n")
#         p1turn = False
#         p2turn = True

    # #player2
    # while p2turn:
    #     input("Player 2 turn\n")
    #     p2turn = False
    #     p1turn = True




def getWord():
    word_bank = ["flatiron", "codekids", "consolelog" , "raccoon",""]
    return word_bank[randint(0, len(word_bank)-1)]

def drawMan(incorrect):
    if incorrect == 0:
        print("\n+---+") 
        print("     ⛓️")
        print("     ⛓️")
        print("     ⛓️")
        print("    🔥🔥🔥🔥")
    if incorrect == 1:
        print("\n+---+") 
        print("🪝   ⛓️")
        print("      ⛓️")
        print("     ⛓️")
        print("    🔥🔥🔥🔥")
    if incorrect == 2:
        print("\n+---+") 
        print("🪝  ⛓️")
        print("🥴  ⛓️")
        print("     ⛓️")
        print("     ⛓️")
        print("    🔥🔥🔥🔥")  
    if incorrect == 3:
        print("\n+---+") 
        print("🪝  ⛓️") 
        print("🥴  ⛓️")
        print("👕  ⛓️")
        print("     ⛓️")
        print("    🔥🔥🔥🔥") 
    if incorrect == 4:
        print("\n+---+") 
        print("🪝  ⛓️")
        print("🥴  ⛓️")
        print("👕  ⛓️")
        print("👖  ⛓️")
        print("   🔥🔥🔥🔥")
    if incorrect == 5:
        print("\n+---+") 
        print("🪝  ⛓️")
        print("🥴  ⛓️")
        print("👕  ⛓️")
        print("👖  ⛓️")
        print("👞 🔥🔥🔥🔥")
           
    if incorrect == 6:
        print("\n+---+") 
        print("🪝  ⛓️") 
        print("🥴  ⛓️")
        print("👕  ⛓️")
        print("👖  ⛓️")
        print("👞👞 🔥🔥🔥🔥")
           
    if incorrect == 7:
        print("\n+---+") 
        print("🪝    ⛓️")
        print("💀    ⛓️")
        print("👕    ⛓️")
        print("🦴🦴  ⛓️")
        print("🔥🔥🔥🔥")
        print(" 🔥🔥🔥🔥")
        print("🔥🔥🔥🔥🔥")
         
def play():
    word = getWord()
    progress = ""   # moves to the following letter if guessed corretly
    for i in range(len(word)):
        progress += "_" # Gives word a blank base/ i need to space this out some how
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
            print(f"You Won!!! you guess {word} correctly")
            break
        if incorrect >= 7:
            print("You lose.")
            print(f"the word was {word}.")
            break
        print(progress)
        print("guess a letter")
        guess = input()
        if guess not in guesses:
            guesses.append(guess)
        if guess in word:
            for i in range(len(word)):
                if guess == word[i]:
                    progressStart = progress[0:i]  #split
                    progressEnd = progress[i+1:]
                    progress = progressStart + guess + progressEnd 
        else:
            incorrect += 1 # this is if the guess is not in the word increase the number of incorrect            
if __name__ == '__main__':
    while True:
        print(welcome)
        print("Do you want to play 🪝 Hangman?🪝 (yes/no)")
        print("LOADING.....⌛")
        answer = input()
        if answer == "yes":
            play()
            print("Player 2 turn")  
        if answer == "no":
            print("Boooooo!!!!!🪝 GoodBye🪝")  
            break
            # need to see if i can create a multiplayer hangman and also see if i can gett the score to appare on the chart
            #also get a nice load up screen

        
