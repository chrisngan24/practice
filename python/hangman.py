import random, math
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
wrong_guess = []
correct_guess = []
output_word=''



def getRandomWord():
  index = int(math.floor(random.random() * len(words) +1))  
  return words[index]

def readInput():
  print "Errors: " + "".join(wrong_guess) + "\n"
  return raw_input("Please guess a letter:\t")

def checkGuess(word, output_word):
  guess = readInput()
  guess= guess[0]
  index = word.find(guess)
  if index == -1:
    already_guessed = False
    for i in range(0, len(wrong_guess)):
      if wrong_guess[i] == guess: 
        already_guessed = True
        break
    if already_guessed:
      print "Letter has already been guessed.  Please try again."
    else:
      wrong_guess.append(guess)
      print ("Incorrect guess! Please try again")

  else:
    correct_guess.append(guess)
    output_list = list(output_word)
    for i in range(0, len(word)):
      if guess == word[i]:
        output_list[i] = guess
    output_word  =  "".join(output_list)

  return output_word


def checkGame():
  if len(wrong_guess) == len(HANGMAN)-1:
    print "You lose :(\n The secret word was " + word

    return False
  elif output_word.find("_") == -1:
    print "Winner!"
    return False
  return True


if __name__ == "__main__":  
  isPlaying = True  
  word = getRandomWord()  
  output_list = []
  for i in range(0,len(word)):
    output_list.append('_')
  output_word = "".join(output_list)
  
  print output_word
  while isPlaying:     
    output_word = checkGuess(word, output_word)     
    print HANGMAN[len(wrong_guess)]
    print output_word + "\n"
    isPlaying = checkGame()

     




