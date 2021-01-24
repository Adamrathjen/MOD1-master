import os
import json

class Character:
   
#make a class to hold info on our characters

   def __init__(self, name, door, pedastle, item):
      self.name = name
      self.door = door
      self.pedastle = pedastle
      self.item = item
   
   
def findName():#get a character name, repeat till it is acceptable
   flag = 0
   name = " "
   while flag != 1:
      name = input("Enter character name: ")
      if name == "Character" or name == "Name":
         print("That is not an acceptable name.")
      else:
         flag = 1
   return name
   


def findDoor():#find and store their choice for future information
   choice = "4"
   door = "0"
   while choice != "1" and  choice != "2" and choice != "3":

      print("Do you choose to have allies(1)")
      print("Become skilled in anything(2)")
      print("Or to be separate from all others(3)")
      choice = input("Choose by selecting a number 1, 2, or 3: ")
      if choice == "1"  or choice == "2" or choice == "3":
         door = choice
      
   return door
         


def findPedastle():#find and store their choice for future information
   weapon = 5
   pedastle = "0"
   while weapon != "1" and weapon != "2" and weapon != "3" and weapon != "4":
      print("Do you choose to deal great damage(1)")
      print("Be able to defend against terrible foes(2)")
      print("Use magic for any circumstance(3)")
      print("Or inspire and strengthen others")
      weapon = input("Choose by selecting a number 1, 2, 3, or 4: ")
      if weapon == "1" or weapon == "2" or weapon == "3" or weapon ==  "4":
         pedastle = weapon
      else:
         print("Please choose 1, 2, 3, or 4.")
   return pedastle



def findItem(pedastle):#find and store their choice of item or magic
   if pedastle == "1":
      item = input("Choose any weapon to weild: ")
      return item
   elif pedastle == "2":
      item = input("Choose any armor to wear: ")
      return item
   elif pedastle == "3":
      print("types of magic are: earth, fire, water, wind")
      print("lightning, mind, poison, light, dark")
      print("summoning, and celestial")
      item = input("Choose any magic to weild: ")
      return item
   elif pedastle == "4":
      item = input("Choose any instrument to play: ")
      return item



def createCharacter(characterStats, newCharacter):#create the character files and store their info
   jsonString = json.dumps(characterStats)
   f = open(newCharacter.name + ".txt", "x")
   f.write(newCharacter.name)
   f.write(newCharacter.door)
   f.write(newCharacter.pedastle)
   f.write(newCharacter.item)
   f.close()
   s = open(newCharacter.name + "stats.txt", "x" )
   s.write(jsonString)#stores our dictionary of stats as a string
   s.close()

   


def readCharacter():#read the character info to the user
   filename = input("Enter character name: ")
   
   if os.path.exists(filename + ".txt"):
      f = open(filename +".txt")
      print(f.read())
      f.close()
      s = open(filename + "stats.txt")
      characterStats = json.loads(s.read())#turns our stats back into a dictionary
      s.close()
      print(characterStats)
   else:
      print("The character does not exist")
      



def main(): #a character creator program of my own design
   print("Character Creator!")

   selected = 1
   while "4" != selected:
      print("Make new Character: 1")
      print("Delete character: 2")
      print("See a current character: 3")
      print("Quit: 4")

      characterStats = {'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 0,'Resistance': 0,'Strength': 0,'Toughness': 0,'Dexterity': 0,'Charisma': 0,'Accuracy': 0}
#all characters start with something like these stats


      selected = input("Make your selection: ")
      if selected == "1": 
         name = findName()
         door = findDoor()
         pedastle = findPedastle()
         item = findItem(pedastle)
         newCharacter = Character(name, door, pedastle, item) #gather our character choices

         
         createCharacter(characterStats, newCharacter)#stores the relevant info in a file

      elif selected == "2": 
         filename = input("Enter the name of the character to delete or enter n to stop: ")
         if filename != "n":
               if os.path.exists(filename + ".txt"):#get rid of a character if it exists
                  os.remove(filename + ".txt")
                  os.remove(filename + "stats.txt")
               else:
                  print("The file does not exist")
         else: continue
      elif selected == "3": 
         readCharacter()#read the info stored of the character

      elif selected == "4": 
         print("you quit")#done messing with characters for the day
      else: 
         print("that isn't an option")#there are only so many options



if __name__== '__main__':
   main()