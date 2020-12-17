from random import randint 


items = [ "rock ","paper","scissors"]

computer = items [randint(0,2)]

player = False 

while player == False :
  player = input ("do you want to rock or paper or scissors ? : ")
  if computer == player :
    print ("the match has been tied .")

  elif player == "scissors":
    if computer == "rock":
      print ("you lose the match !.the rock smashes the scissors" )
    else :
      print ("you won the match !. the scissors cuts the  paper")

  elif player == "paper" :
    if computer == "scissors":
      print ("you loss the match !. scissors cuts the paper " )
  
    else : 
      print ("you won the match ! . paper catches the rock " )

  elif player == "rock":
    if computer == "paper":
      print ("you lose the match!. the rock has been catched by the paper ." ) 
    
    else :
      print ("you won the match !. the rock smashes the scissors")
  else :
     print ("you entered the invalid input ")
  
  player = False 

  computer = items [randint (0,2)]



items = [ "rock ","paper","scissors"]

computer = items [randint(0,2)]

player = False 

while player == False :
  player = input ("do you want to rock or paper or scissors ? : ")
  if computer == player :
    print ("the match has been tied .")

  elif player == "scissors":
    if computer == "rock":
      print ("you lose the match !.the rock smashes the scissors" )
    else :
      print ("you won the match !. the scissors cuts the  paper")

  elif player == "paper" :
    if computer == "scissors":
      print ("you loss the match !. scissors cuts the paper " )
  
    else : 
      print ("you won the match ! . paper catches the rock " )

  elif player == "rock":
    if computer == "paper":
      print ("you lose the match!. the rock has been catched by the paper ." ) 
    
    else :
      print ("you won the match !. the rock smashes the scissors")
  else :
     print ("you entered the invalid input ")
  
  player = False 

  computer = items [randint (0,2)]

