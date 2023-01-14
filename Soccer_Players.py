from tkinter import *
import random
import csv


def Create_List(filename):

    newList = []
    
    fileIn = open(filename, encoding='utf-8', errors="replace")
    fileIn.readline()
    reader = csv.reader(fileIn)

    for line in reader:

        newList.append(line)

    fileIn.close()

    return newList

def setCurrentSelection(event):
    global mainFilterList
    
    currentIndex = PlayerListbox.curselection()[0]
    
    currentSelectionPlayerVar.set(mainFilterList[currentIndex][0])
    currentSelectionNationalityVar.set(mainFilterList[currentIndex][2])

def starterList():
    global allPlayers, currentFilterList

    currentFilterList = []

    for i in range(0, 12):
        s = random.choice(allPlayers)
        currentFilterList.append(s)
        
    updatePlayerListBox(currentFilterList)

def Age_Filter(allPlayers):

    Age = AgeVar.get()
    Filter_List = []

    if(Age > 0):
        for i in range(0, len(allPlayers)):
            if(allPlayers[i][1] == str(Age)):
                Filter_List.append(allPlayers[i])
        return Filter_List
    else:
        return allPlayers

def Overall_Filter(Filter_List):

    Overall = OverallVar.get()
    Overall_Filter_List = []

    if(Overall > 0):
        for i in range(0, len(Filter_List)):
            if(Filter_List[i][3] == str(Overall)):
                Overall_Filter_List.append(Filter_List[i])
        return Overall_Filter_List
    else:
        return Filter_List

def Wage_Filter(Filter_List):

    Wage = WageVar.get()
    Wage_Filter_List = []

    if(Wage > 0):
        for i in range(0, len(Filter_List)):
            if(Filter_List[i][7] == str(Wage)):
                Wage_Filter_List.append(Filter_List[i])
        return Wage_Filter_List
    else:
        return Filter_List

def Position_Filter(Filter_List):

    Position = PositionVar.get()
    Position_Filter_List = []

    if(Position == "GoalKeeper" or Position == "Defence" or Position == "MidField" or Position == "Forward"):
        for i in range(0, len(Filter_List)):
            if(Filter_List[i][9] == Position):
                Position_Filter_List.append(Filter_List[i])
        return Position_Filter_List
    else:
        return Filter_List

def Foot_Filter(Filter_List):
    
    Right_Foot = RightVar.get()
    Left_Foot = LeftVar.get()

    Foot_Filter_List = []

    if(Right_Foot == 1 and Left_Foot == 0):
        for i in range(0, len(Filter_List)):
            if(Filter_List[i][8] == "Right"):
                Foot_Filter_List.append(Filter_List[i])
        return Foot_Filter_List

    elif(Right_Foot == 0 and Left_Foot == 2):
        for i in range(0, len(Filter_List)):
            if(Filter_List[i][8] == "Left"):
                Foot_Filter_List.append(Filter_List[i])
        return Foot_Filter_List

    else: 
        return Filter_List  

def Nationality_Filter(Filter_List):

    Nationality = CountryVar.get()
    Nationality_Filter_List = []

    if( Nationality != "None"):
        for i in range(0, len(Filter_List)):
            if(Filter_List[i][2] == Nationality):
              Nationality_Filter_List.append(Filter_List[i][2])
        return Nationality_Filter_List  
    else:
        return Filter_List

def filterPlayerList():
    global allPlayers, mainFilterList

    Filter_List = Age_Filter(allPlayers)
    Filter_List1 = Overall_Filter(Filter_List)
    Filter_List2 = Wage_Filter(Filter_List1)
    Filter_List3 = Position_Filter(Filter_List2)
    Filter_List4 = Foot_Filter(Filter_List3)
    Filter_List5 = Nationality_Filter(Filter_List4)

    mainFilterList = Filter_List5[:] 
    
    updatePlayerListBox(Filter_List5)

def updatePlayerListBox(playerList):
    
    PlayerListbox.delete(0, END)

    temp = []

    for player in playerList:
        temp.append(f'{player[0][:40]:<25} Age: {player[1]:<4}|  Overall: {player[3]:<4}| Wage(k):{player[7]:<4}|  Foot: {player[8]:<6}| Position: {player[9]:<10}| Nationality: {player[2]}')

    playerVar.set(temp)

#MAIN
#Holding frames
#########

global allPlayers
allPlayers = Create_List("fifa_wc.csv")

global currentFilterList
currentFilterList = allPlayers[:]

global mainFilterList
mainFilterList = []

global Option_Countries
Option_Countries = []

for i in range(0, len(allPlayers)):
        country = allPlayers[i][2]
        if(country not in Option_Countries):
            Option_Countries.append(allPlayers[i][2])

root = Tk()
mainframe = Frame(root)

#Widgets
#########

playerVar = StringVar()
PlayerListbox = Listbox(mainframe, listvariable = playerVar, width=100, font=("Courier", 11))
PlayerListbox.bind("<Double-Button-1>", setCurrentSelection)

updatePlayerListBox(allPlayers)

currentSelectionPlayerVar = StringVar()
currentSelectionPlayerVar.set("currently selected player ...")
currentSelectionPlayerLabel = Label(mainframe, textvariable=currentSelectionPlayerVar)

currentSelectionNationalityVar = StringVar()
currentSelectionNationalityVar.set("currently selected nationality ...")
currentSelectionNationalityLabel = Label(mainframe, textvariable=currentSelectionNationalityVar)

PositionVar = StringVar()
PositionFrame = LabelFrame(mainframe, text="Postion") 
GoalKeeperOption = Radiobutton(PositionFrame, text="GoalKeeper", variable=PositionVar, value="GoalKeeper") 
DefenderOption = Radiobutton(PositionFrame, text="Defence", variable=PositionVar, value="Defence")
MidfieldOption = Radiobutton(PositionFrame, text="MidField", variable=PositionVar, value="MidField")
ForwardOption = Radiobutton(PositionFrame, text="Forward", variable=PositionVar, value="Forward")

OverallVar = IntVar()
OverallEntry = Entry(mainframe, textvariable=OverallVar, font=("Arial",20))
OverallLabel = Label(mainframe, text="Overall", font=("Arial",20))

WageVar = IntVar()
WageEntry = Entry(mainframe, textvariable=WageVar, font=("Arial",20))
WageLabel = Label(mainframe, text="Wage (k)", font=("Arial",20))

AgeVar = IntVar()
AgeScale = Scale(mainframe, from_= 0, to= 45, variable = AgeVar, label="Age", width=20,  length=250, orient=HORIZONTAL)

Footframe = LabelFrame(mainframe, text="Preferred Foot")
RightVar = IntVar()
RightFootCheck = Checkbutton(Footframe, text="Right Foot", variable= RightVar, onvalue= 1, offvalue= 0)
LeftVar = IntVar()
LeftFootCheck = Checkbutton(Footframe, text="Left Foot", variable= LeftVar, onvalue= 2, offvalue= 0)

Option_Countries.sort()
CountryVar = StringVar()
CountryVar.set("None")
CountryOptions = OptionMenu(mainframe, CountryVar, *Option_Countries)

filterPlayersButton = Button(mainframe, text="Filter", command=filterPlayerList)


#GRID THE WIDGETS
###########
mainframe.grid(padx = 50, pady = 50)

currentSelectionPlayerLabel.grid(row=1, column=1, sticky=W)
currentSelectionNationalityLabel.grid(row=2, column=1, sticky=W)
PlayerListbox.grid(row=3, column=1, columnspan=3)

PositionFrame.grid(row=5, column=1,pady=20, sticky=W)
GoalKeeperOption.grid(row=1, column=1, sticky=W)
DefenderOption.grid(row=2, column=1, sticky=W)
MidfieldOption.grid(row=3, column=1, sticky=W)
ForwardOption.grid(row=4, column=1, sticky=W)

OverallLabel.grid(row=4, column=2, pady=(20,0))
WageLabel.grid(row=4, column=3, pady=(20,0))

OverallEntry.grid(row=5, column=2, sticky=N)
WageEntry.grid(row=5, column=3, sticky=N)

AgeScale.grid(row=5, column=2, columnspan=1)

Footframe.grid(row=6, column=2, pady=(0,10), sticky=N)
RightFootCheck.grid(row=1, column=1, sticky=N)
LeftFootCheck.grid(row=1, column=2, sticky=N, padx=(20, 0))

CountryOptions.grid(row=7,column=2)

filterPlayersButton.grid(row=7, column=1, ipadx=30, ipady=10, sticky=W)

root.mainloop()

