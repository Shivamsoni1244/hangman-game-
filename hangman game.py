import random

hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print("//////////////WELCOME TO HANGMAN GAME GENERATOR//////////////")
words = [
    "journey", "car", "phone", "hope", "cloud", "mask", "torch", "eagle", "hardware", "sword",
    "plant", "elephant", "castle", "fire", "justice", "circle", "absolute", "lion", "freedom", "glacier",
    "stone", "heart", "treasure", "backpack", "flame", "balance", "hunter", "bottle", "triangle", "gold",
    "brave", "blue", "mountain", "building", "crown", "wind", "silver", "templed", "star", "lightest",
    "weather", "rabbit", "picture", "spectrum", "game", "danger", "jungle", "mirror", "tree", "planet"
]
word=random.choice(words)
length=len(word)
string=""
for char in range(0,length):
    string+="_"
print(string)
lives=6

corrected_letter=[]
gameover=False
while not gameover:
    display=""
    user=input("guess the letter: ")
    for letter in word:
        if(letter==user):
            display+=letter
            if letter in corrected_letter:
               print("you already guessed it")
            else:
                print("----------------------------")
                print(f"you gussed right letter \"{user}\"")
                print("----------------------------")
                corrected_letter.append(letter)
        elif letter in corrected_letter:
            display+=letter
        else:
            display+="_"
    print(display)
    
    

    if user not in word:
        lives-=1
        print(hangman[lives])
        print("------------------------------")
        print(f"YOU HAVE ONLY {lives}/6 LIVES LEFT")
        print("------------------------------")
        if lives==0:
            gameover=True
            print("--------------------------------------------------")
            print("/////////////////////YOU LOSE/////////////////////")
            print("--------------------------------------------------")
            print(f"word is : {word}")

    if "_" not in display:
        gameover=True
        print("-------------------------------------------------")
        print("/////////////////////YOU WIN/////////////////////")
        print("-------------------------------------------------")
        print(f"word is : {word}")
        