import random
import pandas as pd
import csv
choice = 'y'
while choice=='y' or choice=='Y':
 print(" WELCOME TO YOU !")
 print ("RULE")
 print("There's one randomly selected word of FIVE ,SEVEN OR EIGHT letters")
 print("you will get FEW attempts to guess the word according to the level")
 print("if any letter is in the correct position the letter would be replaced by '*'" )
 print("Have FUN!")
 print("LEVEL")
 print("1. EASY")
 print("2. MEDIUM")
 print("3. HARD")
 print("4. ATTEMPTS")
 hidden_word = ['Study', 'Taken' ,'Times' ,'Known' ,'Court','Young'
 ,'Words', 'White','Light ','Least','Level','Child '
 ,'Death','Press', 'Cases', 'Going','Party','Using'
 ,'Sense','Based','Whose','South','Total','Class','Local'
 ,'Along','Terms','Money','Black','Force','North','Night'
 ,'Short', 'Field','Asked','Quite','Thing' ,'Woman','Major'
 ,'Third','Shown' ,'Began', 'Cause', 'Heart','Seems'
 ,'Trade' ,'Clear']
 medium_level = [ 'Cabinet' , 'Ability', 'Backing' , 'Enhance',
 'Divided' , 'Compete' , 'Evening','Essence' ,
 'Dynamic' , 'courage' , 'Success' , 'Habited',
 'jacamar' , 'Failure' , 'Fashion' , 'Exhibit' ,
 'Illegal' , 'Initial' , 'Removed' , 'Warning' ,
 'Violent' , 'Wedding' , 'Virtual' , 'Weekend' ,
 'Typical' , 'Revenue' , 'Smoking', 'Silicon' ,
 'Supreme' , 'Nervous']
 hard_level = ['Absolute' ,'Bachelor' , 'Computer' , 'Addition', 'Business'
 ,'Contrary' , 'Adequate', 'Calendar', 'Contrast' ,
 'Adjacent' , 'Campaign' , 'Convince' , 'Adjusted' ,'Capacity'
 ,'Corridor' , 'Goodwill' , 'Highland' , 'Frequent' ,
 'Maturity' , 'Mobility' , 'Leverag' , 'Maximize' , 'Modeling'
 ,'Lifetime' , 'Meantime' , 'Moderate' , 'Lighting' ,
 'Slightly' , 'Strategy' , 'Sympathy' , 'Software' ,'Strength'
 , 'Syndrome' , 'Solution' ,'Striking' , 'Tactical'
 , 'Terrible' , 'Training' , 'Tailored' ,
 'Thinking' , 'Transfer' , 'Takeove']
 y=open('project.csv','w+')
 W=csv.writer(y)
 L=["Name","Level","Attempt"]
 W.writerow(L)
 R=csv.reader(y)
 def Start(level):
  level = input("Choose level: ")
  return()
 word = random.choice(hidden_word).lower()
 medium = random.choice(medium_level).lower()
 hard = random.choice (hard_level).lower()
 level = input("Choose level: ")
 if level=='Easy' or level=='easy' or level=='1' or level=='EASY':
   attempt =4
   print("Hint of the word: ")
   print(word[0] + "_ _ _ _")
   while attempt>0:
#print(word)
    guess = input("Enter word: ")
   if guess == word:
    print("Great! You won the game")
    name=input("your name")
    l=[name,level,attempt]
    W.writerow(l)
    break
   else:
     for i in range(0,4):
      if word[i] == guess[i]:
        guess=guess.replace(guess[i],'*')
 #print(guess)
      print(guess)
      attempt = attempt-1
      if attempt!=0:
       print("you have", attempt,"attempts left")
      if attempt==0:
       print("oh no! Attempts exhausted")
       print ("you have lost the game ")
       print("The actual word was: ", word)
       break
 elif level=='Medium' or level=='medium' or level=='2' or level=='MEDIUM':
     attempt = 6
     print("Hint of the word: ")
     print(medium[0] + "_ _ _ _ _" +medium[6])
     while attempt>0:
 #print(word)
      guess = input("Enter word: ")
      if guess == medium:
        print("Great! You won the game")
        name=input("your name")
        l=[name,level,attempt]
        W.writerow(l)
        break
      else:
       for i in range(0,6):
         if medium[i] == guess[i]:
          guess=guess.replace(guess[i],'*')
 #print(guess)
          print(guess)
          attempt = attempt-1
         if attempt!=0:
          print("you have", attempt,"attempts left")
         if attempt==0:
          print("oh no! Attempts exhausted")
         print ("you have lost the game ")
         print("The actual word was: ", medium)

 elif level=='Hard' or level=='hard' or level=='3' or level=='HARD':
   attempt = 5
   print("Hint of the word: ")
   print(hard[0] + "_ _ _ _ _ _" + hard[7])
   while attempt>0:
 #print(word)
    guess = input("Enter word: ")
    if guess == hard:
      print("Great! You won the game")
      name=input("your name")
      l=[name,level,attempt]
      W.writerow(l)
      break
    else:
     for i in range(0,5):
       if hard[i] == guess[i]:
        guess=guess.replace(guess[i],'*')
#print(guess)
       print(guess)
       attempt = attempt-1
       if attempt!=0:
         print("you have", attempt,"attempts left")
       if attempt==0:
         print("oh no! Attempts exhausted")
         print ("you have lost the game ")
         print("The actual word was: ", hard)

 elif level=='Attempts' or level=='attempts' or level=='ATTEMPSTS' or level=='4':
   df = pd.read_csv('project.csv')
   print(df.to_string())
 #print ("Go to dekstop to project.csv to check scores")
choice = input("Do you wish to continue further (y/n): ")
