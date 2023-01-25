from random import random,randint 
choice=['rock','paper','scissor']
p_score=0 
c_score=0
limit=6
while p_score !=limit and c_score != limit: 
    print(f"choose the following:",choice) 
    my_ch=input("player choice").lower()
    if my_ch not in choice: 
      print("invalid")
      continue 
    sys_ch=choice[int(randint(0,2))] 
    print(f"System choice: {sys_ch}") 
    if my_ch==sys_ch: 
      print("---DRAW---") 
      continue
    if my_ch=="rock" and sys_ch=="scissor": 
      p_score +=1 
    elif my_ch=="paper" and sys_ch=="rock": 
        p_score+=1  
    elif my_ch== "scissor" and sys_ch=="paper": 
        p_score+=1  
    else: 
        c_score+=1 
    print(f"your score: {p_score},system score: {c_score}") 

if p_score > c_score: 
  print("you win the match")
else: 
    print("computer win the match")  
















# computer=randint(1,3) 
# while True:
#      player=input() 
#      if computer==1:
#        if player=='paper': 
#         score_player=score_player+1 
#        else: 
#         score_computer=score_computer+1  
#      elif computer==2: 
#          if player=='scissor': 
#             score_player=score_player+1 
#          else: 
#             score_computer=score_computer+1  
#      elif computer==3: 
#         if player=='rock': 
#            score_player=score_player+1 
#         else: 
#            score_computer=score_computer+1 
#      else:
#          score_computer=score_computer 
#          score_player=score_player 
#          print("break")    
