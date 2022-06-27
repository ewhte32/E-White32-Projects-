from graphics import *
import time
import random 

def Batman():

    winx=GraphWin("EW",900,600)
    winx.setBackground("green")

    #inserting the picture 
    image=Image(Point(460,300),"pic1.gif")
    image.draw(winx)
    winx.getMouse()
    image.undraw()

    # the top 3 winners
    firstplace=Text(Point(450,200),"1st place --> Mike")
    firstplace.setTextColor("blue")
    firstplace.draw(winx)

    secondplace=Text(Point(450,250),"2nd place --> Jessica")
    secondplace.setTextColor("red")
    secondplace.draw(winx)

    thirdplace=Text(Point(450,300),"3rd place --> Nick")
    thirdplace.setTextColor("pink")
    thirdplace.draw(winx)
    winx.getMouse()

    firstplace.undraw()
    secondplace.undraw()
    thirdplace.undraw()

    #create a Text and draw it
    txtW=Text(Point(140,95),"Enter Name")

    #txtW.setSize(16)
    txtW.setTextColor("black")
    txtW.draw(winx)

    #creates an Entry object
    inpt=Entry(Point(220,95),10)
    inpt.setFill("white")
    inpt.draw(winx)

    #movement of line and circle
    Bat1=Line(Point(400,600),Point(500,600))
    Bat1.setWidth(6)
    Bat1.draw(winx)
    winx.getMouse()

    #score info
    winx.getMouse()
    txt=Text(Point(300,50), "Highest Score "+ "31")
    txt.draw(winx)

    txt=Text(Point(400,60), "your Score")
    txt.draw(winx)
    scorebox=Entry(Point(640,60),3)
    scorebox.setTExt(" 0")
    score.draw(winx)

    
    

    
 
              
    for i in range(100):

            rNum=random.randint(0,900)
            print(rNum)
            time.sleep(1.2)
            crcl=Circle(Point(450,0),20)
            crcl.setFill("blue")
            crcl.draw(winx)

           

    for i in range(70):

            time.sleep(0.02)
            crcl.move(0,13)
            EDW=winx.checkKey()

            if EDW=="Right":
                nfl.move(20,0)

            if EDW=="Left":
                nfl.move(-20,0)

                time.sleep(0.03)
                nfl.move(0,20)

        #End of Game




Batman()
