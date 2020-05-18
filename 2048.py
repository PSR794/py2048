print('WELCOME!')
def controls():
    print('controls while playing:- \n w-up swipe \n a-left swipe \n s-down swipe \n d-right swipe \n e-exit the game \n r-restart the game \n c-to display controls')
    print('input "0" in grid and winning number for the default settings (5X5 grid and 2048-winning number)')
controls()
import msvcrt
import os  #for clear screen
import subprocess  #for clear screen
import random
def main():
    while True:
        try:
            n=int(input('enter the grid size ,give 0 for default'))  #for the size of grid default:5
            if n<0:
                print('negattive numbers not allowed')
                n=int(input('enter the grid size ,give 0 for default'))  #for the size of grid default:5                
        except Exception:
            print('invalid input')
            main()
            break    
        if n==0:
            n=5

        try:
            w=int(input('enter the winning number ,give 0 for default'))    #target number to be made on the grid to win
            if w!=0 :
                while True:
                    r=1
                    while r<w:
                        r=2*r
                    if r==w:
                       break
                    else:
                        w=int(input('enter a valid number'))
            if w==1:
                raise Exception
        except Exception:
            print('invalid input')
            main()
            break    
        if w==0:
            w=2048

        grid=[]
        for Z in range(n):   #making a empty grid
            rows=[]
            for A in range(n):
                rows.append(0)
            grid.append(rows)
            
        vertical=[]  # horizontal and vertical conatins the positions of the boxes row wise and column wise resp.
        horizontal=[]
        for i in range(n):   #for using in the algorithms positions are stored in the respective horizontal and vertical positions
            horizontal.append(list(range(1+(n*i),1+(n*i)+n)))
            vertical.append(list(range(i+1,(i+1+(n*n)),n)))

        active=[]   #a list which tells the code which position is occupied
        #initially the grid is empty,so 0 is appended in the active list...1 denoted that the postions is occupied and 2 denotes that the number was merged before so it doesnt merges again in the same move(algorithm is set acc. to that)
        
        for i in range(n*n):    
            active.append(0)
            
        def grid_modify(position_played,number,grid,e,a,b,c,d):   #for diplaying the modified grid and the active list everytime player makes a move
            u=(position_played + position_played-1)/2
            u=int(u//n)
            grid[u][(position_played-1)%n]=number
            if e!=0:
                active[a-1+(b*(c*(d-1)))]=0
                active[a-1+(b*(c*d))]=e
            return 2
            
        def GRID_DISPLAY():   # displays the grid after a move with appropriate spacing
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
                
        def WIN_CHECK():   #for checking if the winning number is attained in the grid
            for i in grid:
                if i.count(w)>0:
                    return 1
            return 0
        
        def LOSE_CHECK():   #to check if the player has lost        
            for i in range(n):
                for j in range(n-1):
                    if grid[i][j]==grid[i][j+1] or grid[j][i]==grid[j+1][i]:
                        return 0
            if active.count(0)==0:
                return 1

        def random_two():   #for generating a 2 randomly on any empty posiyon once the player makes a move
            position=random.randint(1,(n*n))
            while True:
                if active[position-1]==0:
                    break
                else:
                    position=random.randint(1,(n*n))  
            active[position-1]=1
            grid_modify(position,2,grid,0,1,1,1,1)
            GRID_DISPLAY()
            

        def SWIPE():   #a function for algorithm of swiping the numbers,has four parts for 'w','a','s','d' moves
            if move==b'c' or move==b'C':
                return 
            check=0   # this variable checks gets a non zero value if the move is available...afterwards used used for telling the user if the move is valid or not
            #up swipe
            if move==b'w' or move==b'W':
                for counta,i in enumerate(horizontal):   #itterates in rows from top to bottom. 
                    if counta==0:
                        continue
                    for counti,j in enumerate(i):   #iterates element in a row and swipes them to the expected positions, counta and counti lets us acces the element in the grid.
                        if active[j-1]==1 or active[j-1]==2:   # j gives us the position of an element in the grid.
                            for k in range(1,counta+1):
                                if active[j-1-(n*k)]==0:
                                    check=grid_modify(j-(n*k) ,grid[counta-(k-1)][counti] ,grid,1,j,(-1),n,k)
                                    check=grid_modify(j-(n*(k-1)) ,0,grid,0,1,1,1,1)
                                    
                                elif (active[j-1-(n*k)]==1 and active[j-1-(n*(k-1))]!=2 and grid[counta-(k-1)][counti]==grid[counta-1-(k-1)][counti]):
                                    check=grid_modify(j-(n*k) ,2*grid[counta-(k-1)][counti] ,grid,2,j,(-1),n,k)
                                    check=grid_modify(j-(n*(k-1)) ,0,grid,0,1,1,1,1)                                      
            # down swipe
            elif move==b's' or move==b'S':
                for counta,i in enumerate(horizontal[::-1]):   # iterates from bottom to top row wise.
                    if counta==0:
                        continue
                    for counti,j in enumerate(i):   # iterates element by element. 
                        if active[j-1]==1 or active[j-1]==2 :
                            for k in range(1,counta+1):
                                if active[j-1+(n*k)]==0:
                                    check=grid_modify(j+(n*k) ,grid[n-1-counta+(k-1)][counti] ,grid,1,j,1,n,k)
                                    check=grid_modify(j+(n*(k-1)) , 0, grid,0,1,1,1,1)
                                    
                                elif (active[j-1+(n*k)]==1 and active[j-1+(n*(k-1))]!=2 and grid[n-1-counta+(k-1)][counti]==grid[n-1-counta+1+(k-1)][counti]):
                                    check=grid_modify(j+(n*k) ,2*grid[n-1-counta+(k-1)][counti] ,grid,2,j,1,n,k)
                                    check=grid_modify(j+(n*(k-1)) ,0,grid,0,1,1,1,1)                                
            #left swipe
            elif move==b'a' or move==b'A':
                for counta,i in enumerate(vertical):   # iteerates from left to right column wise
                    if counta==0:
                        continue
                    for counti,j in enumerate(i):   # iterates element by element
                        if active[j-1]==1 or active[j-1]==2:
                            for k in range(1,counta+1):
                                if active[j-1-(1*k)]==0:
                                    check=grid_modify(j-(1*k) ,grid[counti][counta-(k-1)] ,grid,1,j,(-1),1,k)
                                    check=grid_modify(j-(k-1) ,0,grid,0,1,1,1,1)
                                    
                                elif (active[j-1-(1*k)]==1 and active[j-1-(1*(k-1))]!=2 and grid[counti][counta-(k-1)]==grid[counti][counta-1-(k-1)]):
                                    check=grid_modify(j-(1*k) ,2*grid[counti][counta-(k-1)] ,grid,2,j,(-1),1,k)
                                    check=grid_modify(j-(1*(k-1)) ,0,grid,0,1,1,1,1)                                
            #right swipe
            elif move==b'd' or move==b'D':
                for counta,i in enumerate(vertical[::-1]):   # iterates from right to left column wise.
                    if counta==0:
                        continue
                    for counti,j in enumerate(i):   # iterates element by element
                        if active[j-1]==1 or active[j-1]==2:
                            for k in range(1,counta+1):
                                if active[j-1+(1*k)]==0:
                                    check=grid_modify(j+(1*k) ,grid[counti][n-1-counta+(k-1)] ,grid,1,j,1,1,k)
                                    check=grid_modify(j+(k-1) ,0,grid,0,1,1,1,1)
                                    
                                elif (active[j-1+(1*k)]==1 and active[j-1+(1*(k-1))]!=2 and grid[counti][n-1-counta+(k-1)]==grid[counti][n-1-counta+1+(k-1)]):
                                    check=grid_modify(j+(1*k) ,2*grid[counti][n-1-counta+(k-1)] ,grid ,2,j,1,1,k)
                                    check=grid_modify(j+(1*(k-1)) ,0,grid,0,1,1,1,1)                        
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
        while True:   # if player loses or wins the variable loss or win is assigned a value making the while loop end
            move=msvcrt.getch()
            while True:
                if move==b'w' or move==b'a' or move==b's' or move==b'd' or move==b'e' or move==b'r' or move==b'c' or move==b'W' or move==b'A' or move==b'S' or move==b'D' or move==b'E' or move==b'R' or move==b'C':
                    break
                else:
                    print('invalid input')
                    move=msvcrt.getch()
        
            os.system('cls')
            subprocess.call("cls",shell=True)

            if move==b'e' or move==b'E':
                break
            if move==b'r' or move==b'R':
                main()
            if move==b'c' or move==b'C':
                controls()
                GRID_DISPLAY()
                
            SWIPE()   # for swiping the elmements as per the player's move
            if LOSE_CHECK() or WIN_CHECK():
                break
            
        if LOSE_CHECK():
            print("you lose")
        else:
            print(f'you win \n winning number was {w}')
            
        print('do you want to play again?\n Give Answer In y/n:')   #asking the user after the game if he/she wants to play again
        PLAY=msvcrt.getch()
        while True:
            if PLAY==b'y' or PLAY==b'n' or PLAY==b'Y' or PLAY==b'N' :
                break
            else:
                print('invalid input')
                PLAY=msvcrt.getch()
        if PLAY==b'n' or PLAY==b'N':
            break
if __name__ == '__main__':
    main()
