# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:13:24 2020

@author: Hp
"""
import random
from PIL import Image
end=100

def show_board():
    img=Image.open('board.jpg')
    img.show()

def play():
    p1_name=input('enter the name of 1st player')
    p2_name=input('enter the name of 2nd player')
    pp1=0
    pp2=0
    turn=0
    while(1):
        if(turn%2==0):
            print(p1_name," your turn")
            c=input('1:continue and 0:quit')
            if c==0:
                print(p1_name,'score:',pp1)
                print(p2_name,'score:',pp2)
                break
            
            else:
                dice=random.randint(1,6)
                print("Dice value:",dice)
                pp1=pp1+dice
                pp1= check_ladder(pp1)
                pp1=check_snake(pp1)
                if pp1 >=end:       #check if the player goes beyond the board
                    pp1=end
                if reached_end(pp1):
                    print(p1_name,'WON')
                    break
                print(p1_name,'score:',pp1)
                print(p2_name,'score:',pp2)
        else:
            print(p2_name," your turn")
            c=input('1:continue and 0:quit')
            if c==0:
                print(p1_name,'score:',pp1)
                print(p2_name,'score:',pp2)
                break
            else:
                dice=random.randint(1,6)
                print("Dice value:",dice)
                pp2=pp2+dice
                pp2= check_ladder(pp2)
                pp2=check_snake(pp2)
                if pp2 >=end:       #check if the player goes beyond the board
                    pp2=end
                if reached_end(pp2):
                    print(p2_name,'WON')
                    break
                print(p1_name,'score:',pp1)
                print(p2_name,'score:',pp2)
        turn=turn+1
        
def check_ladder(point):
    if point==4:
        print('LADDER')
        return 14
    elif point==9:
        print('LADDER')
        return 31
    elif point==21:
        print('LADDER')
        return 42
    elif point==28:
        print('LADDER')
        return 84
    elif point==51:
        print('LADDER')
        return 67
    elif point==71:
        print('LADDER')
        return 91
    elif point==80:
        print('LADDER')
        return 100
    else:
        return point
    
def check_snake(point):
    if point==17:
        print('SNAKE')
        return 7
    elif point==62:
        print('SNAKE')
        return 19
    elif point==64:
        print('SNAKE')
        return 60
    elif point==54:
        print('SNAKE')
        return 34
    elif point==87:
        print('SNAKE')
        return 24
    elif point==93:
        print('SNAKE')
        return 73
    elif point==95:
        print('SNAKE')
        return 75
    elif point==98:
        print('SNAKE')
        return 79
    else:
        return point
    
def reached_end(point):
    if point==end:
        return True
    else:
        return False
    
    
    
                
                
                
    
    
    
show_board()
play()
