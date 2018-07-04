import sys

l=[["-","-","-"],["-","-","-"],["-","-","-"]]




def print_board():
    for i in range(3):
        print l[i]




def player1():
    print("Enter index where you want to place 0")
    x=int(raw_input())
    y=int(raw_input())
    if l[x][y]=='-':
        l[x][y]='0'
        print_board()
    else:
        print("Place already filled!!!!!! try again")
        player1()
     



def player2():
    print("Enter index where you want to place *")
    x=int(raw_input())
    y=int(raw_input())
    if l[x][y]=='-':
        l[x][y]='*'
        print_board()
    else:
        print("Place already filled!!!!!! try again")
        player2()   

def check1():
    if l[0][0]==l[0][1]==l[0][2]=='0':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[1][0]==l[1][1]==l[1][2]=='0':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[2][0]==l[2][1]==l[2][2]=='0':
        print("-----------------player 1 WON-----------------")
        sys.exit()
            
    elif l[0][0]==l[1][0]==l[2][0]=='0':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[0][1]==l[1][1]==l[2][1]=='0':
        print("-----------------player 1 WON-----------------")   
        sys.exit()
        
    elif l[0][2]==l[1][2]==l[2][2]=='0':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[0][0]==l[1][1]==l[2][2]=='0':
        print("-----------------player 1 WON-----------------")
        sys.exit()
        
    elif l[0][2]==l[1][1]==l[2][0]=='0':
        print("-----------------player 1 WON-----------------")  
        sys.exit()


def check2():
    if l[0][0]==l[0][1]==l[0][2]=='*':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[1][0]==l[1][1]==l[1][2]=='*':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[2][0]==l[2][1]==l[2][2]=='*':
        print("-----------------player 2 WON-----------------")
        sys.exit()
            
    elif l[0][0]==l[1][0]==l[2][0]=='*':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[0][1]==l[1][1]==l[2][1]=='*':
        print("-----------------player 2 WON-----------------")   
        sys.exit()
        
    elif l[0][2]==l[1][2]==l[2][2]=='*':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[0][0]==l[1][1]==l[2][2]=='*':
        print("-----------------player 2 WON-----------------")
        sys.exit()
        
    elif l[0][2]==l[1][1]==l[2][0]=='*':
        print("-----------------player 2 WON-----------------") 
        sys.exit()    
        
print_board()
a='y'
while(a=='y'):
    print("Player 1 :")
    player1()
    check1()
    print("Player 2 :")
    player2()
    check2()


