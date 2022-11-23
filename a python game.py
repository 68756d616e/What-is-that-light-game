# Welcome to What is that light? game
# A simple python game

print('''
*********************************************
             _,--=--._
               ,'    _    `.
              -    _(_)_o   -
         ____'    /_  _/]    `____
  -=====::(+):::::::::::::::::(+)::=====-
           (+).""""""""""""",(+)
               .           ,
                 `  -=-  '
*********************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

question1 = str.lower(input("You stand infront of two roads, with no other direction. Where do you choose to go, left or right? "))

if question1 == 'left':
  question2 = str.lower(input("As you walk, you see a light flash and something appears to have fallen from the sky, do you 'run back' or 'go to the light' ? "))
  
  if question2 == 'go to the light':
    question3 = str.lower(input("You see a UFO in the light, the door is open. Do you 'enter' the UFO, 'wait' to see or 'head back'? "))
    
    if question3 == 'enter':
      print("Aliens abduct you, game over")
      
    elif question3 == 'head back':
      print("A meteroid fell on you, game over")
      
    elif question3 == 'wait':
      print("Humans appear and take the ship, you win!")
      
    else:
      print("Game over, simply because")
      
  else:
    print("A meteroid fell on you, game over")
  
else:
  print("You chose the wrong path, game over!")