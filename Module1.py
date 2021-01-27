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
   while weapon != "1" and weapon != "2" and weapon != "3" and weapon != "4" or weapon ==  "5":
      print("Do you choose to deal great damage(1)")
      print("Be able to defend against terrible foes(2)")
      print("Use magic for any circumstance(3)")
      print("Craft great items(4)")
      print("Or inspire and strengthen others(5)")
      weapon = input("Choose by selecting a number : ")
      if weapon == "1" or weapon == "2" or weapon == "3" or weapon ==  "4" or weapon ==  "5":
         pedastle = weapon
      else:
         print("Please choose 1, 2, 3, 4, or 5.")
   return pedastle


def findWeapon():
   print("One-handed Sword(1)")
   print("Bow(2)")
   print("Axe(3)")
   print("Spear(4)")
   print("Dagger(5)")
   print("Club(6)")
   print("Hammer(7)")
   print("Handwraps(8)(This is for unarmed combat styles)")
   item = input("Please choose by entering a number. (Ex: 1) :")
   return item

def findInstrument():
   print("Flute(1)")
   print("Violin(2)")
   print("Piano(3)")
   print("Drums(4)")
   print("Guitar(5)")
   print("Harp(6)")
   print("Vocalist(7)(This is for singing)")
   item = input("Please choose by entering a number. (Ex: 1) :")
   return item

def findTool():
   print("Blacksmith(Makes armor, weapons, and tools) Item: Hammer(1)")
   print("Alchemist(Makes potions, bombs, and poisons) Item: Chemist set(2)")
   print("Artificer(Makes complex machinery, constructs, and blueprints) Item: Designer's stand(3)")
   item = input("Please choose by entering a number. (Ex: 1) :")
   return item


def findItem(pedastle):#find and store their choice of item or magic
   if pedastle == "1":
      item = findWeapon()
      return item
   elif pedastle == "2":
      item = input("Choose any armor to wear: ")
      return item
   elif pedastle == "3":
      print("types of magic are: earth(1), fire(2), water(3), wind(4)")
      print("lightning(5), mind(6), poison(7), light(8), dark(9)")
      print("summoning(10), and celestial(11)")
      item = input("Please choose by entering a number. (Ex: 1) :")
      return item
   elif pedastle == "4":
      item = findTool()
      return item
   elif pedastle == "5":
      item = findInstrument()
      return item

def fillDict(newCharacter):
   dict = {'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 0,'Resistance': 0,'Strength': 0,'Toughness': 0,'Dexterity': 0,'Charisma': 0,'Accuracy': 0}
   if newCharacter.pedastle == 2:                                                         #Defense build : 51
      dict = {'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 5,'Resistance': 10,'Strength': 14,'Toughness': 15,'Dexterity': 1,'Charisma': 5,'Accuracy': 1}
   elif newCharacter.pedastle == 3:                                                       #Magic build : 51
      dict = {'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 20,'Resistance': 5,'Strength': 5,'Toughness': 5,'Dexterity': 10,'Charisma': 5,'Accuracy': 1}
   elif newCharacter.pedastle == 5:                                                       #Charisma build : 51
      dict = {'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 5,'Resistance': 5,'Strength': 5,'Toughness': 5,'Dexterity': 5,'Charisma': 21,'Accuracy': 5}
   elif newCharacter.pedastle == 1 and newCharacter.item != 2 and newCharacter.item != 5: #Strength combat build : 51
      dict = {'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 5,'Resistance': 5,'Strength': 22,'Toughness': 12,'Dexterity': 1,'Charisma': 5,'Accuracy': 1}
   elif newCharacter.pedastle == 1 and newCharacter.item == 2:                            #Accuracy combat build : 51
      dict = {'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 5,'Resistance': 5,'Strength': 5,'Toughness': 5,'Dexterity': 5,'Charisma': 5,'Accuracy': 21}
   elif newCharacter.pedastle == 1 and newCharacter.item == 5:                            #Dexterity combat build : 51
      dict = {'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 5,'Resistance': 5,'Strength': 5,'Toughness': 5,'Dexterity': 21,'Charisma': 5,'Accuracy': 5}
   elif newCharacter.pedastle == 4:                                                       #Crafter type build : 51
      dict = {'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 20,'Resistance': 5,'Strength': 8,'Toughness': 4,'Dexterity': 8,'Charisma': 5,'Accuracy': 1}
   return dict

def createCharacter(newCharacter):#create the character files and store their info
   
   f = open(newCharacter.name + ".txt", "x")
   f.write(newCharacter.name)
   f.write(newCharacter.door)
   f.write(newCharacter.pedastle)
   f.write(newCharacter.item)
   f.close()

   characterStats = fillDict(newCharacter) #{'Level': 0,'HP': 40,'MP': 20,'Stamina': 20,'Intelligence': 0,'Resistance': 0,'Strength': 0,'Toughness': 0,'Dexterity': 0,'Charisma': 0,'Accuracy': 0}
   jsonString = json.dumps(characterStats)

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

      



      selected = input("Make your selection: ")
      if selected == "1": 
         name = findName()
         door = findDoor()
         pedastle = findPedastle()
         item = findItem(pedastle)
         newCharacter = Character(name, door, pedastle, item) #gather our character choices

         createCharacter(newCharacter)#stores the relevant info in a file

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