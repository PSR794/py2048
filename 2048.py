import msvcrt
import os
import subprocess
import random
while True:
    try:
        n=int(input('enter the grid size ,give 0 for default'))#for the size of grid default:5
    except Exception:
        print('invalid input')
        break    
    if n==0:
        n=5

    try:
        w=int(input('enter the winning number ,give 0 for default'))#target number to be made on the grid to win
        if w!=0:
            while True:
                r=1
                while r<w:
                    r=2*r
                if r==w:
                   break
                else:
                    w=int(input('enter a valid number'))
    except Exception:
        print('invalid input')
        break    
    if w==0:
        w=2048

    grid=[]
    for Z in range(n):#making a empty grid
        rows=[]
        for A in range(n):
            rows.append(0)
        grid.append(rows)
        
    vertical=[]# horizontal and vertical conatins the positions of the boxes row wise and column wise resp.
    horizontal=[]
    for i in range(n):#for using in the algorithms positions are stored in the respective horizontal and vertical positions
        horizontal.append(list(range(1+(n*i),1+(n*i)+n)))
        vertical.append(list(range(i+1,(i+1+(n*n)),n)))

    active=[]#a list which tells the code which position is occupied 
    for i in range(n*n):#initially the grid is empty,so 0 is appended in the active list...1 denoted that the postions is occupied
        active.append(0)
        
    def grid_modify(position_played,number,grid,e,a,b,c,d):#for diplaying the modified grid evrytime player makes a move
        u=(position_played + position_played-1)/2
        u=int(u//n)
        grid[u][(position_played-1)%n]=number
        if e!=0:
            active[a-1+(b*(c*(d-1)))]=0
            active[a-1+(b*(c*d))]=e
        return 2
        
    def GRID_DISPLAY():
        L=0
        for i in grid:
                if max(i)>L:
                    no=max(i)
                    L=max(i)
        L=0
        while no!=0:
            no=no//10
            L+=1

        for i in grid:
            for j in i:
                print(j,end='  ')
                c=0
                if j==0:
                    c=1
                else:
                    while j!=0:
                        j=j//10
                        c+=1
                for k in range(L-c):
                    print(end=' ')
            print()
            
    def WIN_CHECK():#for checking if the winning number is attained in the grid
        for i in grid:
            if i.count(w)>0:
                return 1
        return 0
    
    def LOSE_CHECK(): #to check if the player has lost        
        for i in range(n):
            for j in range(n-1):
                if grid[i][j]==grid[i][j+1] or grid[j][i]==grid[j+1][i]:
                    return 0
        if active.count(0)==0:
            return 1

    def random_two(): #for generating a 2 randomly on any empty posiyon once the player makes a move
        position=random.randint(1,(n*n))
        while True:
            if active[position-1]==0:
                break
            else:
                position=random.randint(1,(n*n))  
        active[position-1]=1
        grid_modify(position,2,grid,0,1,1,1,1)
        GRID_DISPLAY()
        

    def SWIPE(): #a function for algorithm of swiping the numbers,has four parts for 'w','a','s','d' moves
        check=0
        #up swipe
        if move==b'w':
            for counta,i in enumerate(horizontal): #itterates in rows from top to bottom. 
                if counta==0:
                    continue
                for counti,j in enumerate(i): #iterates element in a row and swipes them to the expected positions, counta and counti lets us acces the element in the grid.
                    if active[j-1]==1 or active[j-1]==2: # j gives us the position of an element in the grid.
                        for k in range(1,counta+1):
                            if active[j-1-(n*k)]==0:
                                check=grid_modify(j-(n*k),grid[counta-(k-1)][counti],grid,1,j,(-1),n,k)
                                check=grid_modify(j-(n*(k-1)),0,grid,0,1,1,1,1)
                                
                            elif (active[j-1-(n*k)]==1 and active[j-1-(n*(k-1))]!=2 and grid[counta-(k-1)][counti]==grid[counta-1-(k-1)][counti]):
                                check=grid_modify(j-(n*k),2*grid[counta-(k-1)][counti],grid,2,j,(-1),n,k)
                                check=grid_modify(j-(n*(k-1)),0,grid,0,1,1,1,1)                                      
        # down swipe
        elif move==b's':
            for counta,i in enumerate(horizontal[::-1]): # iterates from bottom to top row wise.
                if counta==0:
                    continue
                for counti,j in enumerate(i): # iterates element by element. 
                    if active[j-1]==1 or active[j-1]==2 :
                        for k in range(1,counta+1):
                            if active[j-1+(n*k)]==0:
                                check=grid_modify(j+(n*k), grid[n-1-counta+(k-1)][counti], grid,1,j,1,n,k)
                                check=grid_modify(j+(n*(k-1)), 0, grid,0,1,1,1,1)
                                
                            elif (active[j-1+(n*k)]==1 and active[j-1+(n*(k-1))]!=2 and grid[n-1-counta+(k-1)][counti]==grid[n-1-counta+1+(k-1)][counti]):
                                check=grid_modify(j+(n*k),2*grid[n-1-counta+(k-1)][counti],grid,2,j,1,n,k)
                                check=grid_modify(j+(n*(k-1)),0,grid,0,1,1,1,1)                                
        #left swipe
        elif move==b'a':
            for counta,i in enumerate(vertical): # iteerates from left to right column wise
                if counta==0:
                    continue
                for counti,j in enumerate(i): # iterates element by element
                    if active[j-1]==1 or active[j-1]==2:
                        for k in range(1,counta+1):
                            if active[j-1-(1*k)]==0:
                                check=grid_modify(j-(1*k),grid[counti][counta-(k-1)],grid,1,j,(-1),1,k)
                                check=grid_modify(j-(k-1),0,grid,0,1,1,1,1)
                                
                            elif (active[j-1-(1*k)]==1 and active[j-1-(1*(k-1))]!=2 and grid[counti][counta-(k-1)]==grid[counti][counta-1-(k-1)]):
                                check=grid_modify(j-(1*k),2*grid[counti][counta-(k-1)],grid,2,j,(-1),1,k)
                                check=grid_modify(j-(1*(k-1)),0,grid,0,1,1,1,1)                                
        #right swipe
        elif move==b'd':
            for counta,i in enumerate(vertical[::-1]): # iterates from right to left column wise.
                if counta==0:
                    continue
                for counti,j in enumerate(i): # iterates element by element
                    if active[j-1]==1 or active[j-1]==2:
                        for k in range(1,counta+1):
                            if active[j-1+(1*k)]==0:
                                check=grid_modify(j+(1*k),grid[counti][n-1-counta+(k-1)],grid,1,j,1,1,k)
                                check=grid_modify(j+(k-1),0,grid,0,1,1,1,1)
                                
                            elif (active[j-1+(1*k)]==1 and active[j-1+(1*(k-1))]!=2 and grid[counti][n-1-counta+(k-1)]==grid[counti][n-1-counta+1+(k-1)]):
                                check=grid_modify(j+(1*k),2*grid[counti][n-1-counta+(k-1)],grid,2,j,1,1,k)
                                check=grid_modify(j+(1*(k-1)),0,grid,0,1,1,1,1)                        
        if check!=0:
            random_two()
        else: 
            print('try some other move')
            GRID_DISPLAY()
        for i in range(n*n):
            if active[i]==2:
                active[i]=1        
    #THE PLAY
    random_two()
    while True:# if player loses or wins the variable loss or win is assigned a value making the while loop end
        move=msvcrt.getch()
        while True:
            if move==b'w' or move==b'a' or move==b's' or move==b'd' or move==b'e':
                break
            else:
                print('invalid input')
                move=msvcrt.getch()
    
        os.system('cls')
        subprocess.call("cls",shell=True)

        if move==b'e':
            break        
        SWIPE() # for swiping the elmements as per the player's move
        if LOSE_CHECK() or WIN_CHECK():
            break
        
    if LOSE_CHECK():
        print("you lose")
    else:
        print("you win")
        
    print('do you want to play again?\n Give Answer In y/n:')
    PLAY=msvcrt.getch()
    while True:
        if PLAY==b'y' or PLAY==b'n' :
            break
        else:
            print('invalid input')
            PLAY=msvcrt.getch()
    if PLAY==b'n':
        break



















