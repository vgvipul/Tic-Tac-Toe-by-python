import sys
import random
 
l=['-','-','-','-','-','-','-','-','-','-']





def print_board():
    print(" ")
    print(" ")
    print(l[1]+" | "+l[2]+" | "+l[3])
    print("---------")
    print(l[4]+" | "+l[5]+" | "+l[6])
    print("---------")
    print(l[7]+" | "+l[8]+" | "+l[9])
    print(" ")
    print(" ")


def player1():
    print("Enter index where you want to place O")
    x=int(raw_input())
    if l[x]=='-':
        l[x]='O'
        print_board()
    else:
        print("Place already filled!!!!!! try again")
        player1()
     



def player2():
    print("Enter index where you want to place X")
    x=int(raw_input())
    
    if l[x]=='-':
        l[x]='X'
        print_board()
    else:
        print("Place already filled!!!!!! try again")
        player2()   

def check1():
    if l[1]==l[2]==l[3]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[4]==l[5]==l[6]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[7]==l[8]==l[9]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
            
    elif l[1]==l[4]==l[7]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[2]==l[5]==l[8]=='O':
        print("-----------------player 1 WON-----------------")   
        sys.exit()
        
    elif l[3]==l[6]==l[9]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[1]==l[5]==l[9]=='O':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[3]==l[5]==l[7]=='O':
        print("-----------------player 1 WON-----------------")  
        sys.exit()


def check2():
    if l[1]==l[2]==l[3]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[4]==l[5]==l[6]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[7]==l[8]==l[9]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
            
    elif l[1]==l[4]==l[7]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[2]==l[5]==l[8]=='X':
        print("-----------------player 2 WON-----------------")   
        sys.exit()
        
    elif l[3]==l[6]==l[9]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[1]==l[5]==l[9]=='X':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[3]==l[5]==l[7]=='X':
        print("-----------------player 2 WON-----------------") 
        sys.exit()


print("WELCOME to the game of TIC TAC TOE developed by me, Vipul Gupta")
print("read all the instructions carefully")

print("-Values for indeces varies between 1 and 9")
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
        else:
            print("-------PLAYER 2 HAS WON THE TOSS-------")
            print("Player 2 :")
            player2()
            check2()
            print("Player 1 :")
            player1()
            check1()
else:
    sys.exit()

    
    

