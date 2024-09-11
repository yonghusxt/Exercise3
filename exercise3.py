import random


grid_size=5
player_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
treasure_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
check = (treasure_position == player_position)
attempt=5
distance = abs(player_position[0]-treasure_position[0])+abs(player_position[1]-treasure_position[1])
check1=False
check2=False
check3=False
check4=False

while check:
    treasure_position = [random.randint(0, grid_size - 1), random.randint(0, grid_size - 1)]
    check = (treasure_position == player_position)

while attempt > 0:
    print()
    print(f"Moves left: {attempt}")
    print(f"Position: {player_position}")
    
    for i in range(5):
        for j in range(5):
            if i==player_position[0] and j==player_position[1]:
               print("P",end=' ')
            else:
               print(".",end=' ')
        print() 

    print() 
    if player_position[1]<(grid_size-1):
        print("1. Walk east")
        check1=True
    if player_position[1]>0:
        print("2. Walk west")
        check2=True
    if player_position[0]<(grid_size-1):
        print("3. Walk south")
        check3=True
    if player_position[0]>0:
        print("4. Walk north")
        check4=True
    
    choose=input("Enter the serial number of the direction you want to go:")

    if choose.isdigit():
        choose = int(choose)
        if choose == 1 and check1==True:
          player_position[1]=player_position[1]+1
          check1=False
        elif choose == 2 and check2==True:
          player_position[1]=player_position[1]-1
          check2=False
        elif choose == 3 and check3==True:
          player_position[0]=player_position[0]+1
          check3=False
        elif choose == 4 and check4==True:
          player_position[0]=player_position[0]-1
          check4=False
        else:
          print("Please enter the correct number.")
          continue
    else:
        print("Please enter number.")
        continue
    distance1 = abs(player_position[0]-treasure_position[0])+abs(player_position[1]-treasure_position[1])
    if distance1 == 0:
       print()
       print("You have found the treasure.")
       print("Congratulations on winning.")
       break
    else:
        if distance1 == distance:
           print("at the same location")
           distance = distance1
           attempt=attempt-1
        elif distance1 > distance:
           print("moving farther")
           distance = distance1
           attempt=attempt-1
        else:
           print("moving closer")
           distance = distance1
           attempt=attempt-1

if attempt == 0:
   print()
   print(f"treasure position: {treasure_position}")
   for i in range(5):
        for j in range(5):
            if i==player_position[0] and j==player_position[1]:
               print("P",end=' ')
            elif i==treasure_position[0] and j==treasure_position[1]:
               print("T",end=' ')
            else:
               print(".",end=' ')
        print() 
   print("You can't move anymore, you lost.")
