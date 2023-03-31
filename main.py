import sys
from GuiFunction import *
from functools import partial
#------------------------------------
YOB=QtWidgets.QApplication(sys.argv)
#Window de jouer :
windowTicTacToo=windowF(300,305,"Tic Tac Too","","")
windowTicTacToo.setStyleSheet("background-color:#fff2f4;")
Joueur1=labelF(10,10,190,30,"Background-color:red;color:white;font-size:20px;",windowTicTacToo,"")
Joueur2=labelF(10,40,190,30,"Background-color:green;color:white;font-size:20px;",windowTicTacToo,"")
button1=buttonF(10,80,90,70,"Background-color:#7ac5cd;color:yellow;font-size:30px",windowTicTacToo,"")
button2=buttonF(103,80,90,70,"Background-color:#7ac5cd;color:yellow;font-size:30px",windowTicTacToo,"")
button3=buttonF(198,80,90,70,"Background-color:#7ac5cd;color:yellow;font-size:30px",windowTicTacToo,"")
button4=buttonF(10,155,90,70,"Background-color:#7ac5cd;color:yellow;font-size:30px",windowTicTacToo,"")
button5=buttonF(103,155,90,70,"Background-color:#7ac5cd;color:yellow;font-size:30px",windowTicTacToo,"")
button6=buttonF(198,155,90,70,"Background-color:#7ac5cd;color:yellow;font-size:30px",windowTicTacToo,"")
button7=buttonF(10,230,90,70,"Background-color:#7ac5cd;color:yellow;font-size:30px",windowTicTacToo,"")
button8=buttonF(103,230,90,70,"Background-color:#7ac5cd;color:yellow;font-size:30px",windowTicTacToo,"")
button9=buttonF(198,230,90,70,"Background-color:#7ac5cd;color:yellow;font-size:30px",windowTicTacToo,"")
buttonChangerName=buttonF(205,30,90,30,'font-size:20px;background-color:black;color:white;',windowTicTacToo,"Changer")
#Winner Window
winnerWindow=windowF(300,150,"Winner","","")
winnerWindow.setStyleSheet("background-color:#f0f8ff;color:#19e59e;")
labelWinner=labelF(35,15,250,90,"font-size:20px;color:black;",winnerWindow,"")
buttonNouvelleJoue=buttonF(100,105,100,40,'background-color:#19e59e;color:white;font-size:20px;',winnerWindow,"next game")
numbre=1
#Joueur window
windowJoueur=windowF(300,150,"Tic Tac Too","","")
labelNameJoueur1=labelF(5,7,100,50,'font-size:20px',windowJoueur,'Joueur 1 : ')
labelNameJoueur2=labelF(5,67,100,50,'font-size:20px',windowJoueur,'Joueur 2 : ')
inputNameJoueur1=inputF(110,10,180,40,'font-size:20px',windowJoueur,'Nom Joueur 1')
inputNameJoueur2=inputF(110,70,180,40,'font-size:20px',windowJoueur,'Nom Joueur 2')
buttonNameJoueur=buttonF(100,115,100,30,'font-size:25px;',windowJoueur,'Ok')
windowJoueur.show()
def joueurName():
    Joueur1.setText("Joueur 1 : "+inputNameJoueur1.text())
    Joueur2.setText("Joueur 2 : "+inputNameJoueur2.text())
    windowJoueur.close()
    windowTicTacToo.show()
def winners():
    global numbre
    if(button1.text()==button2.text()==button3.text()!='' or button4.text()==button5.text()==button6.text()!='' or button7.text()==button8.text()==button9.text()!='' or button1.text()==button5.text()==button9.text()!='' or button3.text()==button5.text()==button7.text()!='' or button1.text()==button4.text()==button7.text()!='' or button2.text()==button5.text()==button8.text()!='' or button3.text()==button6.text()==button9.text()!=''):
        if(numbre%2==1):
            labelWinner.setText("The winner is : "+inputNameJoueur2.text())
        else:
            labelWinner.setText("The winner is : "+inputNameJoueur1.text())
        winnerWindow.show()
    elif numbre == 10:
        labelWinner.setStyleSheet("font-size:20px;color:red;")
        labelWinner.setText("               Draw")
        winnerWindow.show()
def fun(button):
    global numbre
    if button.text()=='':
        if numbre%2==1:
            button.setStyleSheet("color:red;font-size:25px;background-color:#d9ead3;")
            button.setText("X")
        else :
            button.setStyleSheet("color:green;font-size:25px;background-color:#d9ead3;")
            button.setText("O")
        numbre+=1
        winners()
def nouveauxJeu():
    global numbre
    button1.setText("")
    button2.setText("")
    button3.setText("")
    button4.setText("")
    button5.setText("")
    button6.setText("")
    button7.setText("")
    button8.setText("")
    button9.setText("")
    button1.setStyleSheet("background-color:#7ac5cd;font-size:25px;")
    button2.setStyleSheet("background-color:#7ac5cd;font-size:25px;")
    button3.setStyleSheet("background-color:#7ac5cd;font-size:25px;")
    button4.setStyleSheet("background-color:#7ac5cd;font-size:25px;")
    button5.setStyleSheet("background-color:#7ac5cd;font-size:25px;")
    button6.setStyleSheet("background-color:#7ac5cd;font-size:25px;")
    button7.setStyleSheet("background-color:#7ac5cd;font-size:25px;")
    button8.setStyleSheet("background-color:#7ac5cd;font-size:25px;")
    button9.setStyleSheet("background-color:#7ac5cd;font-size:25px;")
    numbre=1
    winnerWindow.close()
    windowTicTacToo.show()
def changeName():
    nouveauxJeu()
    windowTicTacToo.close()
    windowJoueur.show()
buttonNouvelleJoue.clicked.connect(nouveauxJeu)
button1.clicked.connect( partial( fun, button=button1))
button2.clicked.connect( partial( fun, button=button2) )
button3.clicked.connect( partial( fun, button=button3) )
button4.clicked.connect( partial( fun, button=button4) )
button5.clicked.connect( partial( fun, button=button5) )
button6.clicked.connect( partial( fun, button=button6) )
button7.clicked.connect( partial( fun, button=button7) )
button8.clicked.connect( partial( fun, button=button8) )
button9.clicked.connect( partial( fun, button=button9) )
buttonNameJoueur.clicked.connect(joueurName)
buttonChangerName.clicked.connect(changeName)
YOB.exec_()