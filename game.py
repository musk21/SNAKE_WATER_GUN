import random


def swg(comp, mine):
    if (comp == 'g' and mine == 'w'):
        return True
    elif(comp == 's' and mine == 'g'):
        return True
    elif(comp == 'w' and mine == 's'):
        return True
    else:
        return False
print("Lets play Snake Water gun")
print("s=Snake ,w=Water and g=gun")
wanna_play=int(input("Press 0 -> To exit \nPress 1->To continue:->"))
while(wanna_play==1):
    choice = ('s', 'w', 'g')
    comp = random.randint(0, 3)
    comp = choice[comp]
    mine = input("Choose either 's','w' or 'g': ")
    if (comp == mine):
         print("The match is draw")
    else:
        win = swg(comp, mine)
     
    if win:
     print("You choose",mine,"and Computer choose",comp)
     print("You Won")
    else:
      print("You choose",mine,"and Computer choose",comp)
      print("Computer win")
    wanna_play=int(input("Press 0 -> To exit 1->To continue Again:->"))
    
if(wanna_play==0):
    print("You Choose To Exit")
    
