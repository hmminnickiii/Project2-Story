# Project 2 Story
# Your program must do the following:

# Set the scene by presenting the user with a story/scenario they are currently in.
# Ask the user to select one of three stories to participate in
# At least one of these stories must include a multiple choice problem (select 'a' through 'd')
# At least one of these stories must ask the user to enter a correct value to solve a riddle/puzzle
# The last story is up to you, but it must use Control Flow and at least one if statement.
# When the user navigates through a story, they should get a different ending based on whether they succeeded at that story's challenge or not
# Your code must be commented to be graded. Code without comments will NOT be graded.

# Give the story a title and introduction
print("~ LOST IN TIME AND SPACE ~")
print("* Choose Your Own Adventures of Epic Proportions *")
print()
# Provide the background of the scenario
print("You find yourself in a strange place at a strange time and you're unsure where you are, how you got there, or how to get home.")
print()
print("You see some beings in the distance and decide to go speak with them to try to figure out where and when you are. Let's hope they're friendly!")
print()
# Ask the user which story they want to explore
print("You see three beings. You could speak to:")
print("  A. A one-headed being")
print("  B. A two-headed being")
print("  C. A three-headed being")
userBranchChoice = input("Who do you want to ask for help? Please select option A, B, or C: ")
print()
# print(f"You chose to speak to {userBranchChoice}. Good luck!")
# First story has multiple choice options
if(userBranchChoice == "A"):
  print("You meet Una Cabeza. He is wearing many watches. What do you ask him?")
  print(" a. Where you are?")
  print(" b. What date/time you are in?")
  print(" c. How you got there?")
  oneHeadChoice = input("Please select option a, b, or c: ")
  print()
  if(oneHeadChoice == "b"):
    print("You are in the year 20202 and the time is 46:05. We have a different day length now.")
  else:
    print("I don't know where we are or how we got here. I'm sorry.")

# Second story requires a correct answer to a question/riddle
elif(userBranchChoice == "B"):
  print("You meet Dos Noggins. They have cartography tattoos. They say we can tell you where you are IF you can tell us the answer to life, the universe, everything...")
  print()
  twoHeadAnswer = input("What is the answer to life, the universe, everything? ")
  print()
  if(twoHeadAnswer == "42"):
    print("You are very wise! You are also on Multi-Caput and a very, very long way from home.")
  else:
    print("You chose incorrectly and we unfortunately are not permitted to tell you where you are. Our deepest apologies.")
# Third story requires an if statement and validation of logical condition
elif (userBranchChoice == "C"):
  print("You decided to speak with Drei Kopfe. Prepare yourself!")
  print()
  print("Drei Kopfe looks at you intently with all 6 eyes. He says... We know many things and you have many questions. If you can tell us who shot first, we can tell you how you got here.")
  print()
  threeHeadAnswer = input("Who shot first? ")
  print()
  if(threeHeadAnswer == "Han"):
    print(f"You are a geek and geeks are cool! {threeHeadAnswer} shot first. You got to Multi-Caput in the year 20202 only through a wild dream. You will awake at home, on Earth, in your time soon.")
  else:
    print(f"I'm sorry, {threeHeadAnswer} didn't shoot first. You are stuck here.")
else:
  print("Don't you want to speak to someone to try to find out where you are, when is now, and how you got here? Please try again.")
# All stories have right and wrong endings and users should only be able to see one of any options of any story at a time

