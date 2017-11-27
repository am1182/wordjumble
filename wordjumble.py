import random
import shelve
import time
import sys
import bubblesort

def menu():
     print("""
                    Welcome to the Word Jumble Game

                    """)
     print("   1 - Play the game")
     print("   2 - Browse a word set")
     print("   3 - Add a new word set")
     print("   4 - Delete a word set")
     print("   5 - View high scores")
     print("   6 - Exit")
     choose = int(input("\nChoose an option: "))

     if choose == 1:
          print("""
                    Unscramble letters to make a word
          """) 
          #open the file that the sets of words are loaded into and print keys:
          word_file = shelve.open("allwords.txt") 
          for key in word_file.keys():
               print(key)
          #player inputs name of key to choose the word set they want to play:
          keyinput = input("""
                    Choose a set of words: """)  
          #words are the chosen using key from the word file:
          words = word_file[keyinput]
          #score initially set to 0:
          score = 0
          #the player gets 10 guesses, since the loop runs 10 times:
          for i in range(0, 10):
               #a random word from list is chosen:
               word = random.choice(words)
               correct = word
               jumble = ""
               #while loop scrambles the word:
               while word:
                    position=random.randrange(len(word))
                    jumble += word[position]
                    word = word[:position] + word[position+1:]
               #print the jumbled word:
               print("""       
     The jumble word is: {}""".format(jumble))
               guess = input("\nEnter your guess: ")
               #if player's input is the same as correct answer add 1 to score:
               if(guess == correct):
                    print("You guessed it. \n")
                    score += 1
               #if input is not the same as the correct answer show correct answer:
               else:
                    print("Incorrect, the word is: {}. \n".format(correct))
          print("""
                         The End
                                        """)
          word_file.close()
          print("Your score is: {}/10. \n".format(score))
          #time format from: http://strftime.org/
          currenttime = time.strftime("%H:%M:%S %d/%m/%Y")
          #open file with scores:
          score_file = shelve.open("scores.txt")
          #if list with key 'scores' is not in file, create new list:
          if "scores" not in score_file:
               score_file["scores"] = []
          #put scores into list s:
          s = score_file["scores"]
          #append score and current time to list s:
          #from https://www.ibisc.univ-evry.fr/~fpommereau/blog/2015-06-01-automating-writeback-to-python-shelve.html
          s.append((score, currenttime))
          #list s is assigned to key:
          #have to explicitly assign s to key to save scores
          score_file["scores"] = s
          #sync to save the shelf and then close it:
          score_file.sync() 
          score_file.close()
          press = int(input("\nPress 0 to go back to Main Menu: "))
          if press == 0:
               menu()

     elif choose == 2:
          word_file = shelve.open("allwords.txt")
          print("""
                    Loaded wordsets:
                    """)
          #print all available keys on new line:
          for key in word_file.keys():
               print("""           {}""".format(key))
          keyinput = input("\nChoose a set of words to browse: ")
          print("""         
                     {}
                         """.format(keyinput))
          #print list of words without commas or brackets:
          #adapted from: http://stackoverflow.com/questions/13550423/python-printing-without-commas
          print(" ".join(str(word) for word in word_file[keyinput]))
          word_file.close()
          press = int(input("\nPress 0 to go back to Main Menu: "))
          if press == 0:
               menu() 
                  
     elif choose == 3:
          #user inputs name of file to extract words from:
          fileinput = input("\nChoose file of words: ")
          afile = open(fileinput)
          whole_thing = afile.read()
          #split string of words by comma:
          z = whole_thing.split(",")
          #strip list z of whitespace:
          s = [x.strip() for x in z]
          afile.close()
          keyinput = input("Choose a name for your word set: ")
          word_file = shelve.open("allwords.txt")
          #list with chosen keyinput is assigned to list s:
          word_file[keyinput] = s
          word_file.sync()
          word_file.close()
          print("\nYour word set '{}' has been added".format(keyinput))
          press = int(input("\nPress 0 to go back to Main Menu: "))
          if press == 0:
               menu()

     elif choose == 4:
          word_file = shelve.open("allwords.txt")
          print("""
                    Loaded wordsets:
                    """)
          #print every key in 'allwords.txt' on new line:
          for key in word_file.keys():
               print("""           {}""".format(key))
          keyinput = input("\nChoose a set of words to delete: ")
          #delete list with the same key as the input:
          del word_file[keyinput]
          word_file.sync()
          word_file.close()
          print("""
                    Your word set '{}' has been deleted""".format(keyinput))
          press = int(input("\nPress 0 to go back to Main Menu: "))
          if press == 0:
               menu()

     elif choose == 5:
          print("""
                    Highscores
                    """)
          score_file = shelve.open("scores.txt")
          #load list of scores into new list for sorting:
          score_list = score_file["scores"]
          #sorting function to sort from highest to lowest:
          #bubble sort code adapted from: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
          bubblesort.bubble_sort(score_list)
          #print each tuple on new line:
          for score in score_list:
               print(score)
          score_file.close()           
          press = int(input("\nPress 0 to go back to Main Menu: "))
          if press == 0:
               menu()
  
     elif choose == 6:
          #ends program:
          #exit function from: https://docs.python.org/2/library/sys.html
          sys.exit()
menu()

