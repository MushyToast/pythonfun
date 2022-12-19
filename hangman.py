#imports
import pyfiglet
import random
import sys
import time



#pyfiglet -------------------------
feegl = pyfiglet.figlet_format("Hangman", font="big")
print(feegl )
#variables and functions
comparison = []
def dotdot(wording, times):
  for x in range(0, times):
    print(" " + wording + ".", end="\r")
    time.sleep(0.5)
    print(" " + wording + "..", end="\r")
    time.sleep(0.5)
    print(" " + wording + "...", end="\r")
    time.sleep(0.5)
    sys.stdout.write("\033[K")

easy = [
  "chair", "table", "output", "input", "python", "good", "food", "sink", "easy", "hang", "kill", "death", "hello", "seat", "dance", "vow", "cream", "goofy", "me", "like", "doing", "men", "not", "woman", "each", "enjoy", "servo", "time", "clock"
]
med = [
  "vowel", "brushy", "institute", "bottle", "toaster", "breadroll", "shelving", "beeswax", "grater", "stovetop", "cutlass", "melody", "calculator", "yellow", "computer", "hangman", "cheetos", "glasses", "chocolate", "flavoring", "balloon", "children", "trash", "lunchbox", "mission", "mirror", "microwave"
]

hard = [
  "institution", "toaster", "chickfila", "refrigerator", "dishwasher", "demonstrator", "mathematics", "psychology", "redundancy", "plagiarize", "technology", "corruption", "decorative", "integrated", "memorandum", "engagement", "disappointment", "inappropriate", "environmental", "anniversary", "jurisdiction", "consolidate", "comprehensive", "conglomerate", "rehabilitation", "supercalifragilisticexpialidocious" #sorry for anyone that gets that last one lol
]

mistake_dialogue = {
  1:"Well, one mistake. The post where the man will be hanged from has been drawn. The man stil ceases to exist..",
  2:"Bet you were hoping not to make it here. 2 mistakes, the man's head has been drawn. He looks kinda scared..",
  3:"Here you are again. 3 mistakes. The man's torso has been drawn. The lava still bubbles underneath him with a hungry cry..",
  4:"Oh well. 4 mistakes? Can't be too bad. The man's left arm has been drawn. The post is starting to strain due to the mans weight..",
  5:"5 mistakes?!? Come on bro, is it that hard (that's what she said), the man's right arm has been drawn. The post continues to bend..",
  6:"Look at you. 6 mistakes. Sucks for you, the man's left leg has been drawn, and the post is under alot of stress..",
  7:"Oh no, 7 mistakes. One more and you're OUT! The man's right leg has been drawn, and the post is under extreme stress..",
  8:"OHHH NOOOOO!!! THE POST BROKE AND THE MAN FELL INTO THE LAVA! Better luck next time!"
}

#code!

print("Welcome to Hangman, my first major project that's not completely dumb and stupid! \nRules are pretty simple, and I am NOT giving you an explanation on how to play hangman, look it up yourself!")

difficulty = 0

while True:
  ndiff = input("Let's start off with game setup. What difficulty do you want, [1] Easy, [2] Medium, [3] Hard?\n")
  if ndiff == "1":
    print("Great, easy mode it is!")
    difficulty = "easy"
    break
  elif ndiff == "2":
    print("Great, medium mode it is!")
    difficulty = "med"
    break
  elif ndiff == "3":
    print("Great, hard mode it is! Good luck, hehe :>")
    difficulty = "hard"
    break
  else:
    print("Not a valid response. Use 1, 2, or 3 for difficulty selection.")

word = 0

if difficulty == "easy":
  word = random.choice(list(easy))
elif difficulty == "med":
  word = random.choice(list(med))
elif difficulty == "hard":
  word = random.choice(list(hard))
#8 mistakes and your out. 7 safely 8 out
letterscount = 0
underline = []
for i, v in enumerate(word):
  letterscount = letterscount + 1
  underline.append("_")
  comparison.append(v)
#actual game
dotdot("Loading game", random.randint(0, 10))
usedwords = [] #table of ALREADY used words
guesses = 0 #incorrect guesses total. this doesn't reset
inguesses = 0
print("You have been presented with a", letterscount, "letter word.")
while True:
  correctletters1 = {}
  correctletters2 = [] #one shows the letters and their order in the word and 2 shows just the correct letters for easier reference
  incletter = True
  letterscorrect = 0
  v1 = ""
  for i in underline:
    v1 = v1 + i
  print("\n")
  print(v1)
  print("\n")
  print("Used Words:")
  if "_" not in underline:
    print("\n" + v1 + "\n")
    print("You got it! The word was", word + "! Good game!")
    exit()
  v2 = ""
  for x in usedwords:
    v2 = (v2 + " " + x)
  print(v2)
  print("------------------------------------------------------")
  lguess = input("Enter in your letter guess. Note you cannot guess words. Please enter your input in lowercase and one letter.\n")
  if (len(lguess)==1 and lguess.isdigit()==False and lguess.islower()==True): #guess criteria checker for valid input
    alreadyguessed = False
    for x in usedwords:
      if x == lguess:
        alreadyguessed = True
    if alreadyguessed == True:
      print("You have already guessed this letter. Please try again.")
    elif alreadyguessed == False: #if the word has NOT been guessed
      for i, v in enumerate(word):
        if lguess == v:
          letterscorrect = letterscorrect + 1
          index = i-1
          underline[i] = v
          incletter = False

      if incletter == False:
        print(f"You got", letterscorrect, "letters correct!")
        usedwords.append(lguess)
        for i in underline:
          v1 = v1 + i


      elif incletter == True:
        print("\n \n \n")
        print("You didn't get any letters correct!")
        usedwords.append(lguess)
        inguesses = inguesses + 1
        print(mistake_dialogue.get(inguesses))
        if inguesses == 8:
          print("Whoops! You lost!! The word was", word + "!! Better Luck next time.")
          exit()



  else:
    print("This input does not meet the guess criteria. Try again")


