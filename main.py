from tkinter import *
import random
import math
#Resolution 1280x720 
####################################import modules####################################


#######################################################################
###########################Set Global Variables########################
WIDTH = 1280
HEIGHT = 720
gameStatus = 1
gameTime = 0
mx = 0 
my = 0 
un_entry = 0
un_window = 0
final_score = 0
highscores = []
myButton = 0
username = ""
buttonLeaderboard = 0
buttonLeaderboard2 = 0
bindbutton = 0
resumebutton = 0
savebutton = 0

NewKeyBindUp = ""
NewKeyBindDown = ""
NewKeyBindLeft = ""
NewKeyBindRight =""
changeKeyDown = 0
submitKeyChangeDown = 0
changeKeyUp = 0
submitKeyChangeUp = 0
changeKeyLeft = 0
submitKeyChangeLeft = 0
changeKeyRight = 0
submitKeyChangeRight = 0
backtomenufromkeybinds = 0
score = 0


loadPressed = False 
loadSuccess = False

character_list = []
ball_list = []
personwewant = []
listofballs = []
loadbutton = 0
loaded = 0
saved = False 
savecharacterattributes = []

key = ""
radius = 0
colors = ['#fa867f', '#ce5fed', '#ff73a4', 'pink', '#ff9912', '#FFB90F', '#BF3EFF', 
          '#82ffec', 'red', '#82ffda', '#FFD700', '#00FF00']
####################################load keybinds####################

keybinds = open("keybinds.txt", "r")
lines = keybinds.readlines()
if lines == []:
    controls = ["Up", "Down", "Left", "Right"]

else: 
    controls = eval(lines[0])
keybinds.close()


    #controls = ["Up", "Down", "Left", "Right"]

MovePlayerUp = controls[0]
MovePlayerDown = controls[1]
MovePlayerLeft = controls[2]
MovePlayerRight = controls[3]

######################################################################
### Set highscores

def myFunc(e):
    return e['score']
file = open("cache.txt", "r")
lines = file.readlines()
if lines == []:
    highscores = [{'user': 'kyan', 'score': 100}, {'user': 'cool', 'score': 150}, {'user': 'he/him', 'score': 200},{'user': 'Josh', 'score': 600}]
else:
    highscores = eval(lines[0])
highscores.sort(key=myFunc, reverse = True)
file.close()

#######################################################################
###########################---Character and NPC Class---###############

def create_circle(x, y, r, canvas_name, color):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas_name.create_oval(x0, y0, x1, y1, outline='white', fill=color, tag = "npc")

#

class Ball:
    def __init__(self, speedx, speedy, radius, top_left_corner, bottom_right_corner, color):
        self.one = speedx
        self.two = speedy
        self.three = radius
        self.four = top_left_corner
        self.five = bottom_right_corner
        self.six = color
        self.ball = create_circle(self.four, self.five, self.three, canvas, self.six)
        self.movement()

    def movement(self):
        global gameStatus, key
        if gameStatus == 2:
            someting = canvas.coords(self.ball)
            if len(someting) == 4:
                (leftPos, topPos, rightPos, bottomPos) = canvas.coords(self.ball)
                #wall boundary


                if (len(ball_list) != 0):
                    for this_ball in ball_list:
                        if (this_ball != self):
                            this_ball_pos = canvas.coords(this_ball.ball)
                            this_ball_x = this_ball_pos[0] + this_ball.three
                            this_ball_y = this_ball_pos[1] + this_ball.three
                            ball_x = leftPos +self.three
                            ball_y = topPos + self.three
                            dx = this_ball_x - ball_x
                            dy = this_ball_y - ball_y
                            distance = math.sqrt( dx ** 2 + dy ** 2)

                            if(distance <= this_ball.three + self.three):
                                if dx < abs((ball_x - self.one) - this_ball_x):
                                    self.one *= -1
                                if dy < abs ((ball_y - self.two) - this_ball_y):
                                    self.two *= -1
               

                if (leftPos + self.one) < 0 or (rightPos + self.one) > WIDTH:
                    self.one = -self.one

                if (topPos + self.two) < 0 or (bottomPos + self.two) > HEIGHT:
                    self.two = -self.two


        if gameStatus == 2:
            if key == "o":
                self.one *= 0.9
                self.two *= 0.9
            canvas.move(self.ball, self.one, self.two)

        canvas.after(10, self.movement)

class Character:
    def __init__(self, x1, y1, x0,y0, color):
        self.square = canvas.create_oval(x1, y1, x0, y0, fill = color)
        self.one = x1
        self.two = y1
        self.three = x0
        self.four = y0
        self.five = color
        self.speedx = mx
        self.speedy = my
        self.length = 25/2
        self.playercontrol()

    def playercontrol(self):
        global key, gameStatus, mx, my, score, character_leftpos, MovePlayerUp, MovePlayerDown, MovePlayerLeft, MovePlayerRight, ball_list 
        mx = 5
        my = 5 

        
        if gameStatus == 2 and score != 0:
            someting = canvas.coords(self.square)
            if len(someting) == 4:
                (leftPos, topPos, rightPos, bottomPos) = canvas.coords(self.square)
                self.one = leftPos
                self.two = topPos
                self.three = rightPos
                self.four = bottomPos
                if (len(ball_list) != 0):
                    for i in range(8):
                        this_ball_pos = canvas.coords(ball_list[i].ball)
                        this_ball_x = this_ball_pos[0] + 40
                        this_ball_y = this_ball_pos[1] + 40
                        character_x = leftPos + 25/2
                        character_y = topPos + 25/2
                        dx = this_ball_x - character_x
                        dy = this_ball_y - character_y
                        distance = math.sqrt( dx**2 + dy**2)
                        if(distance <= ball_list[i].three + self.length):
                            if score > 50:
                                gameStatus = 4

                if (key == MovePlayerUp) and topPos >2:

                    canvas.move(self.square, 0, -my) 

                if (key == MovePlayerDown) and bottomPos < HEIGHT -2:

                    canvas.move(self.square, 0, my) 

                if (key == MovePlayerLeft) and leftPos > 2 :

                    canvas.move(self.square, -mx, 0) 

                if (key == MovePlayerRight) and rightPos < WIDTH-2:   

                    canvas.move(self.square, mx, 0)




        canvas.after(10, self.playercontrol)










#######################################################################
####################Buttons and Button Functions#######################


def clickerMenu(event):
    global buttonLeaderboard, gameStatus
    buttonLeaderboard.destroy()
    buttonLeaderboard = 0

    gameStatus = 1


def clickerMenu2(event):
    global buttonLeaderboard2, gameStatus, myButton, un_entry, un_window, bindbutton, loadbutton
    if buttonLeaderboard2 != 0 and un_entry != 0 and un_window != 0 and bindbutton != 0 and myButton != 0: 
        myButton.destroy()
        myButton = 0
        un_entry.destroy()
        un_entry = 0
        un_window = 0
        buttonLeaderboard2.destroy()
        buttonLeaderboard2 = 0
        bindbutton.destroy()
        bindbutton = 0
        loadbutton.destroy()
        loadbutton = 0
    gameStatus = 6
    highscores.sort(key=myFunc, reverse = True)

def changeKeyUpFunction(event):
    global NewKeyBindUp, key
    root.bind("<KeyRelease>", pressKey)
    NewKeyBindUp = key

def changeKeyDownFunction(event):
    global NewKeyBindDown, key
    root.bind("<KeyRelease>", pressKey)
    NewKeyBindDown = key


def changeKeyLeftFunction(event):
    global NewKeyBindLeft, key
    root.bind("<KeyRelease>", pressKey)
    NewKeyBindLeft = key

def changeKeyRightFunction(event):
    global NewKeyBindRight, key
    root.bind("<KeyRelease>", pressKey)
    NewKeyBindRight = key


def submitKeyChangeFunctionUp(event):
    global MovePlayerUp, NewKeyBindUp, controls
    NewKeyBindUp = key
    MovePlayerUp = NewKeyBindUp
    root.bind("<KeyRelease>", releaseKey)
    controls[0] = MovePlayerUp
    file = open("keybinds.txt", "w")
    file.write(str(controls))
    file.close()


def submitKeyChangeFunctionDown(event):
    global MovePlayerDown, NewKeyBindDown
    NewKeyBindDown = key
    MovePlayerDown = NewKeyBindDown
    root.bind("<KeyRelease>", releaseKey)
    controls[1] = MovePlayerDown
    file = open("keybinds.txt", "w")
    file.write(str(controls))
    file.close()

def submitKeyChangeFunctionLeft(event):
    global MovePlayerLeft, NewKeyBindLeft
    NewKeyBindLeft = key
    MovePlayerLeft = NewKeyBindLeft
    root.bind("<KeyRelease>", releaseKey)
    controls[2] = MovePlayerLeft
    file = open("keybinds.txt", "w")
    file.write(str(controls))
    file.close()

def submitKeyChangeFunctionRight(event):
    global MovePlayerRight, NewKeyBindRight
    NewKeyBindRight = key
    MovePlayerRight = NewKeyBindRight
    root.bind("<KeyRelease>", releaseKey)
    controls[3] = MovePlayerRight
    file = open("keybinds.txt", "w")
    file.write(str(controls))
    file.close()

def backtomenufromkeybindsfunction(event):
    global changeKeyUp, changeKeyDown, changeKeyLeft, changeKeyRight, submitKeyChangeUp, submitKeyChangeDown, submitKeyChangeLeft, submitKeyChangeRight, backtomenufromkeybinds, gameStatus
    if changeKeyUp != 0 and changeKeyDown != 0 and changeKeyLeft != 0 and changeKeyRight != 0 and submitKeyChangeRight != 0 and submitKeyChangeLeft !=0 and submitKeyChangeDown != 0 and submitKeyChangeUp != 0:
        changeKeyUp.destroy()
        changeKeyUp = 0
        changeKeyDown.destroy()
        changeKeyDown = 0
        changeKeyRight.destroy()
        changeKeyRight = 0
        changeKeyLeft.destroy()
        changeKeyLeft = 0
        submitKeyChangeUp.destroy()
        submitKeyChangeDown.destroy()
        submitKeyChangeLeft.destroy()
        submitKeyChangeRight.destroy()
        submitKeyChangeUp = 0
        submitKeyChangeDown = 0
        submitKeyChangeLeft = 0
        submitKeyChangeRight = 0
        backtomenufromkeybinds.destroy()
        backtomenufromkeybinds = 0
        gameStatus = 1

def exitfunction(event):
    global gameStatus, resumebutton, ball_list, character_list, savebutton
    canvas.delete(ALL)
    ball_list = []
    character_list = []
    gameStatus = 1
    resumebutton.destroy()
    resumebutton = 0
    if savebutton != 0:
        savebutton.destroy()
        savebutton = 0

def bindbuttonfunction(event):
    global myButton, gameStatus, myLabel, image, un_entry, un_window, username, buttonLeaderboard2, bindbutton, loadbutton
    canvas.delete("welcome1")
    username = un_entry.get()
    myButton.destroy()
    myButton = 0
    un_entry.destroy()
    un_entry = 0
    un_window = 0
    canvas.delete("spaceman")
    buttonLeaderboard2.destroy()
    buttonLeaderboard2 = 0
    bindbutton.destroy()
    bindbutton = 0
    loadbutton.destroy()
    loadbutton = 0
    gameStatus = 7

def clicker(event):
    global myButton, gameStatus, myLabel, image, un_entry, un_window, username, buttonLeaderboard2, bindbutton, personwewant, loadbutton
    if myButton!= 0 and un_entry!=0 and un_window!=0 and username!=0 and buttonLeaderboard2!=0 and bindbutton!=0:
        username = un_entry.get()
        myButton.destroy()
        myButton = 0
        un_entry.destroy()
        un_entry = 0
        un_window = 0
        canvas.delete("spaceman")
        buttonLeaderboard2.destroy()
        buttonLeaderboard2 = 0
        bindbutton.destroy()
        bindbutton = 0
        loadbutton.destroy()
        loadbutton = 0
        gameStatus = 2


def loader(event):
    global loadbutton, personwewant, un_entry, un_window, username, loadPressed, score, listofballs, loadSuccess
    username = un_entry.get()
    file = open("charactersave.txt", "r")
    lines = file.readlines()
    if lines == []:
        charactersave =[{'duckwarrior102': [135.0, 630.0, 160.0, 655.0, '#FFB90F', 605]}]
    else:       
        charactersave = eval(lines[0])
    file.close()
    counter = 0
    loadPressed = True
    loadSuccess = False
    if loadbutton != 0:
        loadbutton.destroy()
        loadbutton = 0
    for userdict in charactersave:
        if username in userdict:
            personwewant = userdict[username]
            break

    file = open("npcsave.txt", "r")
    lines = file.readlines()
    if lines == []:
        npcsave = [{'duckwarrior102': [[0.07630408489538924, 0.11445612734308383, 40, 781, 426, '#ff9912'], [0.1526081697907785, -0.1526081697907785, 40, 709, 558, '#FFD700'], [-0.1526081697907785, -0.1526081697907785, 40, 540, 495, 'pink'], [0.34336838202925124, -0.07630408489538924, 40, 504, 356, '#82ffda'], [-0.11445612734308383, -0.1526081697907785, 40, 365, 324, '#FFB90F'], [0.34336838202925124, -0.1526081697907785, 40, 543, 480, '#BF3EFF'], [-0.19076021223847292, -0.1526081697907785, 40, 464, 420, '#ff9912'], [0.22891225468616766, 0.11445612734308383, 40, 340, 731, '#ff9912']]}]
    else:
        npcsave = eval(lines[0])
    file.close()

    for userdict in npcsave:
        if username in userdict:
            listofballs = userdict[username]
            gameStatus = 2
            counter = 1
            loadSuccess = True
            canvas.create_text(640,315, font= ('consolas', 40), text = "Success!", tag = "inputsuccess")
            canvas.after(150)
            break

    if loadSuccess == False:
        canvas.create_text(640,315, font= ('consolas', 40), text = "Try Again!", tag = "inputerror")
        canvas.after(150)



    

def saver(event):
    global savebutton, savecharacterattributes, personwewant, username, character_list, saved, listofballs, ball_list

    file = open("charactersave.txt", "r")
    lines = file.readlines()
    if lines == []:
        charactersave =[{'duckwarrior102': [135.0, 630.0, 160.0, 655.0, '#FFB90F', 605]}]
    else:       
        charactersave = eval(lines[0])
    file.close()
    counter = 0
    saved = False
    savecharacterattributes = [character_list[0].one, character_list[0].two, character_list[0].three, character_list[0]. four, character_list[0].five, score]
    if saved == False:
        #######################################################
        ###############save character##########################
        for userdict in charactersave:
            if username in userdict:
                userdict[username] = savecharacterattributes
                counter = 1
                break
        if counter == 0:
            newdict = {}
            newdict[username] = savecharacterattributes
            charactersave.append(newdict)

        file = open("charactersave.txt", "w")
        file.write(str(charactersave))

        file.close()


    file = open("npcsave.txt", "r")
    lines = file.readlines()
    if lines == []:
        npcsave = [{'duckwarrior102': [[0.07630408489538924, 0.11445612734308383, 40, 781, 426, '#ff9912'], [0.1526081697907785, -0.1526081697907785, 40, 709, 558, '#FFD700'], [-0.1526081697907785, -0.1526081697907785, 40, 540, 495, 'pink'], [0.34336838202925124, -0.07630408489538924, 40, 504, 356, '#82ffda'], [-0.11445612734308383, -0.1526081697907785, 40, 365, 324, '#FFB90F'], [0.34336838202925124, -0.1526081697907785, 40, 543, 480, '#BF3EFF'], [-0.19076021223847292, -0.1526081697907785, 40, 464, 420, '#ff9912'], [0.22891225468616766, 0.11445612734308383, 40, 340, 731, '#ff9912']]}]
    else:
        npcsave = eval(lines[0])
    savenpcattributes = []
    for i in range(8):
        emptyarray = [ball_list[i].one, ball_list[i].two, ball_list[i].three, ball_list[i].four,ball_list[i].five, ball_list[i].six ]
        savenpcattributes.append(emptyarray)

    if saved == False: 

    #     ######################################################
    #     #####################save npc#########################
        counter = 0
        for userdict in npcsave:
            if username in userdict:
                userdict[username] = savenpcattributes
                counter = 1
                break
        if counter == 0:
            newdict = {}
            newdict[username] = savenpcattributes
            npcsave.append(newdict)

        file=open("npcsave.txt", "w")
        file.write(str(npcsave))
        file.close()
        if savebutton != 0:
            savebutton.destroy()
            savebutton = 0
        canvas.create_text(640,350, font= ('consolas', 40), text = "Success!", tag = "savesuccess")
        canvas.after(125)
        canvas.delete("savesuccess")

        saved = True

##############################key presses
def pressKey(e):
    global key
    key = e.keysym

def releaseKey(e):
    global key
    if key == e.keysym:
        key = ""

#######################################################################
##########################Main Game state functions ##################################
def gameTitle():

    global gameStatus, myButton, un_entry, un_window, buttonLeaderboard2, username, bindbutton, loaded, loadbutton
    if key == "Return":
        if myButton!= 0 and un_entry!=0 and un_window!=0 and username!=0 and buttonLeaderboard2!=0 and bindbutton!=0 and loadbutton!=0:
            username = un_entry.get()
            myButton.destroy()
            myButton = 0
            un_entry.destroy()
            un_entry = 0
            un_window = 0
            canvas.delete("spaceman")
            buttonLeaderboard2.destroy()
            buttonLeaderboard2 = 0
            bindbutton.destroy()
            bindbutton = 0
            gameStatus = 2
            loadbutton.destroy()
            loadbutton = 0
    if key == "Tab":
        gameStatus =5

def gameMain():
    global gameStatus
    global score
    gameStatus = 2
    score = score + 1 
    if key == "Tab":
        gameStatus =5
    if key == "Escape":
        gameStatus = 5

def gamePaused():

    global gameStatus, score, gameTime, resumebutton, savebutton
    score = score
    gameTime = gameTime
    if key == "space":
        if resumebutton != 0 and savebutton !=0:
            resumebutton.destroy()
            savebutton.destroy()
            resumebutton = 0
            savebutton = 0
        gameStatus = 2
    if key == "Tab":
        gameStatus =5

def gameOver():

    global gameStatus, score, gameTime, key, ball_list, character_list, final_score, highscores, username
    final_score = score
    if final_score > (highscores[3].get("score")): #### if higher than the lowest score
        myDict = {}
        if username == "":
            myDict['user'] = "DEFAULT_USER"
        else:
            myDict['user'] = username
        myDict['score'] = final_score
        highscores[3] = myDict
        file = open("cache.txt", "w")
        file.write(str(highscores))
        file.close()
    gameTime = 0

    ball_list = []
    character_list = []
    
    if key == "space":
        canvas.after(100)
        gameStatus = 2
    if key == "m":
        gameStatus = 1
    if key == "Tab":
        gameStatus =5

def gameBoss():
    global gameStatus, score, gameTime, key, ball_list, character_list, final_score
    if key == "Escape":
        if final_score == score: 
            if score == 0:
                gameStatus = 1
            else:
                gameStatus = 4
        else: 
            gameStatus = 3

def gameLeaderboard():
    global gameStatus, key, highscores, back, buttonLeaderboard
    gameStatus = 6
    highscores.sort(key=myFunc, reverse = True)
    file = open("cache.txt", "w")
    file.write(str(highscores))
    file.close()
    if key == "Tab":
        gameStatus =5
        if buttonLeaderboard!=0:
            buttonLeaderboard.destroy()
            buttonLeaderboard = 0

def gameBind():
    global score, gameStatus, gameTime, myButton, un_entry, un_window, buttonLeaderboard2
    global changeKeyUp, changeKeyDown, changeKeyLeft, changeKeyRight, submitKeyChangeUp, submitKeyChangeDown, submitKeyChangeLeft, submitKeyChangeRight, backtomenufromkeybinds, gameStatus
    gameStatus = 7
    if key == "Tab":
        gameStatus = 5

def removeCanvasButtons():

    canvas.delete("paused")
    canvas.delete("score")
    canvas.delete("gameover")
    canvas.delete("final_score")
    canvas.delete("welcome1")
    canvas.delete("welcome2")
    canvas.delete("spaceman")
    canvas.delete("boss")
    canvas.delete("leaderboardtext")
    canvas.delete("leaderboardtext1")
    canvas.delete("leaderboardtext2")
    canvas.delete("leaderboardtext3")
    canvas.delete("leaderboardtext4")
    canvas.delete("keybindtext")
    canvas.delete("uptext1")
    canvas.delete("downtext1")
    canvas.delete("lefttext1")
    canvas.delete("righttext1")
    canvas.delete("inputsuccess")
    canvas.delete("inputerror")
    canvas.delete("gameOverScreen")
def drawScreen():

    global gameTime, radius, ball_list, score_list, character_list, rectangle, final_score, score, un_entry, un_window, myButton, buttonLeaderboard, submitKeyChangeUp, submitKeyChangeDown, submitKeyChangeLeft, submitKeyChangeRight, resumebutton
    global buttonLeaderboard2, bindbutton, MovePlayerUp, MovePlayerDown, MovePlayerLeft, MovePlayerRight, NewKeyBindUp, loadbutton, listofballs, loadSuccess, loadPressed
    global NewKeyBindDown, NewKeyBindLeft, NewKeyBindRight, changeKeyDown, changeKeyUp, changeKeyLeft, changeKeyRight, backtomenufromkeybinds, personwewant, loaded, savebutton
    global loaded
    removeCanvasButtons()
    if gameStatus == 1: ##############TITLE
        score = 0   
        final_score = 0
        canvas.create_text(640, 200, font =('consolas', 70), text = "", tag = "welcome1")
        canvas.create_image(640,360, image = square, tag = "spaceman")

        #create entry place
        if un_entry == 0:
            un_entry = Entry(root, font=("Helvetica", 24), width =25,fg= "#336d92", bd=0)

        #create window
        if un_window == 0:
            un_window = canvas.create_window(465, 350, anchor="nw", window = un_entry)

        if myButton == 0:
            myButton = Button(root, text = "Play")
            myButton.bind("<Button-1>", clicker)
            myButton.place(x=620, y =500)

        if buttonLeaderboard2 == 0:
            buttonLeaderboard2 = Button(root, text = "Leaderboard")
            buttonLeaderboard2.bind("<Button-1>", clickerMenu2)
            buttonLeaderboard2.place(x=380, y=500)

        if bindbutton == 0:
            bindbutton = Button(root, text = "Key Binds")
            bindbutton.bind("<Button-1>", bindbuttonfunction)
            bindbutton.place(x=800, y=500)

        if loadbutton == 0:
            loadbutton = Button(root, text = "Load Game Save For User")
            loadbutton.bind("<Button-1>", loader)
            loadbutton.place(x=1000, y=100)

            
######################################## main game if



    if gameStatus == 2:
        if (score == final_score):
            score = 0
            final_score = 0
            ball_list = []
            character_list = []
        canvas.create_text(60, 30, font=("Helvetica", 24), text="Score: "+ str(score), tag="score")
        if len(ball_list) == 0:
            if loadSuccess and loadPressed == True:
                ball_list = []
                character_list = []
                for i in range(8):
                    ballobject = Ball(listofballs[i][0], listofballs[i][1], listofballs[i][2], listofballs[i][3], listofballs[i][4], listofballs[i][5] )
                    ball_list.append(ballobject)
            else:
                ball_list = [Ball(random.randint(2, 7), random.randint(2, 4), random.randint(30, 50), random.randint(200, 800), random.randint(200, 800), random.choice(colors)) for i in range(8)]
        
        if len(character_list) == 0:
            if loadSuccess and loadPressed == True:
                character_list = [Character(personwewant[0], personwewant[1], personwewant[2], personwewant[3], personwewant[4]  )]
                score = personwewant[5]
            else:
                character_list = [Character(200, 200, 225, 225, "#FFB90F")]
        
        loadPressed = False
        loadSuccess = False            



    if gameStatus == 3:							###################GAME PAUSED SCREEN
        canvas.create_image(640,360, image = pauseScreen, tag = "paused")
        canvas.create_text(60, 30, font=("Helvetica", 24), text="Score: "+ str(score), tag="score")
        if resumebutton == 0:
            resumebutton = Button(root, text = "Exit")
            resumebutton.bind("<Button-1>", exitfunction)
            resumebutton.place(x=1000, y= 30)

        if savebutton == 0:
            savebutton
            savebutton = Button(root, text = "save")
            savebutton.bind("<Button-1>", saver)
            savebutton.place(x=1000, y= 80)



    if gameStatus == 4:  ###################GAME OVER SCREEN
        canvas.delete(ALL)
        #canvas.create_text(640, 300, font =('consolas', 40), text = "GAME OVER", tag = "gameover")
        #canvas.create_text(640, 400, font =('consolas', 40), text = "Press 'm' for menu or 'space' to restart.", tag = "gameover")
        canvas.create_image(640,360, image = gameOverScreen, tag = "gameOverScreen")
        canvas.create_text(640, 500, font=('Times New Roman', 20), text = "Final Score: " + str(final_score), tag = "final_score")
        canvas.create_text(640, 550, font=('Times New Roman', 20), text = "Highest Score: " + str(highscores[0].get("score")), tag = "final_score")

    if gameStatus == 5: #####ultimate boss key 
        canvas.create_image(640, 360, image = bossbackground, tag ="boss")
        if myButton != 0 and un_entry != 0 and buttonLeaderboard2 != 0 and bindbutton != 0 and loadbutton!= 0:
            myButton.destroy()
            myButton = 0
            un_entry.destroy()
            un_entry = 0
            buttonLeaderboard2.destroy()
            buttonLeaderboard2 = 0
            bindbutton.destroy()
            bindbutton = 0
            loadbutton.destroy()
            loadbutton = 0
        if resumebutton != 0 and savebutton != 0 :
            resumebutton.destroy()
            resumebutton = 0
            savebutton.destroy()
            savebutton = 0
        un_window = 0
        canvas.delete("spaceman")

    if gameStatus == 6:  ################### Leaderboard
        canvas.create_text(640, 200, font =('consolas', 70), text = "Leaderboard", tag = "leaderboardtext")
        canvas.create_text(640, 350, font =('consolas', 20), text = "1ST - " + str(highscores[0].get("user")) + ": " + str(highscores[0].get("score")), tag = "leaderboardtext1")
        canvas.create_text(640, 400, font =('consolas', 20), text = "2ND - " + str(highscores[1].get("user")) + ": " + str(highscores[1].get("score")), tag = "leaderboardtext2")
        canvas.create_text(640, 450, font =('consolas', 20), text = "3RD - " + str(highscores[2].get("user")) + ": " + str(highscores[2].get("score")), tag = "leaderboardtext3")
        canvas.create_text(640, 500, font =('consolas', 20), text = "4TH - " + str(highscores[3].get("user")) + ": " + str(highscores[3].get("score")), tag = "leaderboardtext4")

        if buttonLeaderboard == 0:
            buttonLeaderboard = Button(root, text = "Back to Menu")
            buttonLeaderboard.bind("<Button-1>", clickerMenu)
            buttonLeaderboard.place(x=1000, y =30)

    if gameStatus == 7:        ##############  key bind page
        canvas.create_text(640, 200, font =('consolas', 70), text = "Key Binds", tag = "keybindtext")
        canvas.create_text(300, 300, font =('consolas', 20), text = "Move Player Up: " + MovePlayerUp, tag = "uptext1")


        if changeKeyUp == 0:
            changeKeyUp = Button(root, text = "Change Key bind")
            changeKeyUp.bind("<Button-1>", changeKeyUpFunction)
            changeKeyUp.place(x=500, y =285)

        if submitKeyChangeUp == 0:
            submitKeyChangeUp = Button(root, text = "Submit Key bind")
            submitKeyChangeUp.bind("<Button-1>", submitKeyChangeFunctionUp)
            submitKeyChangeUp.place(x=700, y =285) 


        canvas.create_text(300, 400, font =('consolas', 20), text = "Move Player Down: " + MovePlayerDown, tag = "downtext1")


        if changeKeyDown == 0:
            changeKeyDown = Button(root, text = "Change Key bind")
            changeKeyDown.bind("<Button-1>", changeKeyDownFunction)
            changeKeyDown.place(x=500, y =385)

        if submitKeyChangeDown == 0:
            submitKeyChangeDown = Button(root, text = "Submit Key bind")
            submitKeyChangeDown.bind("<Button-1>", submitKeyChangeFunctionDown)
            submitKeyChangeDown.place(x=700, y =385)    


        canvas.create_text(300, 500, font =('consolas', 20), text = "Move Player Left: " + MovePlayerLeft, tag = "lefttext1")
        

        if changeKeyLeft == 0:
            changeKeyLeft = Button(root, text = "Change Key bind")
            changeKeyLeft.bind("<Button-1>", changeKeyLeftFunction)
            changeKeyLeft.place(x=500, y =485)

        if submitKeyChangeLeft == 0:
            submitKeyChangeLeft = Button(root, text = "Submit Key bind")
            submitKeyChangeLeft.bind("<Button-1>", submitKeyChangeFunctionLeft)
            submitKeyChangeLeft.place(x=700, y =485) 



        canvas.create_text(300, 600, font =('consolas', 20), text = "Move Player Right: " + MovePlayerRight, tag = "righttext1")

        if changeKeyRight == 0:
            changeKeyRight = Button(root, text = "Change Key bind")
            changeKeyRight.bind("<Button-1>", changeKeyRightFunction)
            changeKeyRight.place(x=500, y =585)

        if submitKeyChangeRight == 0:
            submitKeyChangeRight = Button(root, text = "Submit Key bind")
            submitKeyChangeRight.bind("<Button-1>", submitKeyChangeFunctionRight)
            submitKeyChangeRight.place(x=700, y =585) 

        if backtomenufromkeybinds == 0:
            backtomenufromkeybinds = Button(root, text="Back to Menu")
            backtomenufromkeybinds.bind("<Button-1>", backtomenufromkeybindsfunction)
            backtomenufromkeybinds.place(x=1000, y=100)





def main():

    global gameStatus

	################################### Title Screen
    if gameStatus == 1:     ######loading screen
        gameTitle()


	################################### Main game function Screen
    if gameStatus == 2: 
        gameMain()

	################################### Paused Screen
    if gameStatus == 3: 
        canvas.after(10, gamePaused())

	################################### Gameover Screen
    if gameStatus == 4: 
        gameOver()

	################################### Boss Screen
    if gameStatus == 5: 
        gameBoss()

    ################################### Leaderboard Screen
    if gameStatus == 6: 
        gameLeaderboard()

	################################### Controls Screen
    if gameStatus == 7: 
        gameBind()    

    drawScreen()  # ############# execute draw screen function

    root.after(10, main)		# ###### run main loop

###########################################################################
###########################################################################
# Create root window and set up canvas to work on
root = Tk()

root.geometry("1280x720")
root.resizable(False, False)
root.title("A Very Cool Game")
root.bind("<KeyPress>", pressKey)
root.bind("<KeyRelease>", releaseKey)
canvas = Canvas(root, width=1280, height=720, bg="white")
canvas.pack(fill="both", expand=True)

#################################################################
# load images
bossbackground = PhotoImage(file="blackboard.png")
square = PhotoImage(file="titlescreen.png")
pauseScreen = PhotoImage(file="paused.png")
gameOverScreen = PhotoImage(file="gameover.png")

main()
root.mainloop()
