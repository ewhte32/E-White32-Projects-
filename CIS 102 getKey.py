from graphics import *

def main():

    winx=GraphWin("EW",600,400)
    winx.setBackground("White")

    #create the circle whereever on canavas
    bal=Circle(Point(250,340),30)
    bal.setFill("Blue")
    bal.draw(winx)

    for i in range (10):
        time.sleep(1)
        dirctn=winx.checkKey()

        if dirctn=="R":
           bal.move(10,0)
        if dirctn=="L":
            bal.move(-10,0)

main()
    
