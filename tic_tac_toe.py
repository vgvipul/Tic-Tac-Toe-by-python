import sys
import random
 
l=[["-","-","-"],["-","-","-"],["-","-","-"]]




def print_board():
    for i in range(3):
        print l[i]




def player1():
    print("Enter index where you want to place O")
    x=int(raw_input())
    y=int(raw_input())
    if l[x][y]=='-':
        l[x][y]='O'
        print_board()
    else:
        print("Place already filled!!!!!! try again")
        player1()
     



def player2():
    print("Enter index where you want to place X")
    x=int(raw_input())
    y=int(raw_input())
    if l[x][y]=='-':
        l[x][y]='X'
        print_board()
    else:
        print("Place already filled!!!!!! try again")
        player2()   

def check1():
    if l[0][0]==l[0][1]==l[0][2]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[1][0]==l[1][1]==l[1][2]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[2][0]==l[2][1]==l[2][2]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
            
    elif l[0][0]==l[1][0]==l[2][0]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[0][1]==l[1][1]==l[2][1]=='O':
        print("-----------------player 1 WON-----------------")   
        sys.exit()
        
    elif l[0][2]==l[1][2]==l[2][2]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[0][0]==l[1][1]==l[2][2]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[0][2]==l[1][1]==l[2][0]=='O':
        print("-----------------player 1 WON-----------------")  
        sys.exit()


def check2():
    if l[0][0]==l[0][1]==l[0][2]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[1][0]==l[1][1]==l[1][2]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[2][0]==l[2][1]==l[2][2]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
            
    elif l[0][0]==l[1][0]==l[2][0]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[0][1]==l[1][1]==l[2][1]=='X':
        print("-----------------player 2 WON-----------------")   
        sys.exit()
        
    elif l[0][2]==l[1][2]==l[2][2]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[0][0]==l[1][1]==l[2][2]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[0][2]==l[1][1]==l[2][0]=='X':
        print("-----------------player 2 WON-----------------") 
        sys.exit()    


print("WELCOME to the game of TIC TAC TOE developed by me, Vipul Gupta")
print("read all the instructions carefully")
print("-Index to place 0 and * are in the form of matrix i.e [0][0]")
print("-Values for indeces varies between 0 to 2")
print("Are you ready for thr game?(y/n)")
v=raw_input()
if v=='y':
    print_board()
    r=random.randint(1,2)
    a='y'
    while(a=='y'):
        if r==1:
            print("-------PLAYER 1 HAS WON THE TOSS-------")
            print("Player 1 :")
            player1()
            check1()
            print("Player 2 :")
            player2()
            check2()
        elif r==2:
            print("-------PLAYER 2 HAS WON THE TOSS-------")
            print("Player 2 :")
            player2()
            check2()
            print("Player 1 :")
            player1()
            check1()
else:
    sys.exit()

    

