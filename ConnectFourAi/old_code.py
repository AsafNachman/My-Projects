

def GetPieceValue(Board,x,y,Color,Forward=None,Up=None,Diagonal=None): # My first way of evaluating Position py getting value of a piece
    x,y = GetNextPos(x,y,Forward=Forward,Up=Up,Diagonal=Diagonal)

    if(x<0 or x>6 or y<0 or y>5):
        return 0

    if (Board[x][y] == 0):
        Value = 5
    if (Board[x][y] == Color):
        Value = 9
    if (Board[x][y] == ChangeColor(Color)):
        return 3
    return Value

def PieceValue(Board,x,y,Color):  # My first way of evaluating Position py getting value of a piece
    Value = GetPieceValue(Board,x,y,Color,Forward=True,Up=None,Diagonal=None)
    Value += GetPieceValue(Board, x, y, Color, Forward=False, Up=None, Diagonal=None)

    Value += GetPieceValue(Board, x, y, Color, Forward=None, Up=True, Diagonal=None)
    Value += GetPieceValue(Board, x, y, Color, Forward=None, Up=False, Diagonal=None)

    Value += GetPieceValue(Board, x, y, Color, Forward=True, Up=True, Diagonal=True)
    Value += GetPieceValue(Board, x, y, Color, Forward=False, Up=False, Diagonal=True)
    Value += GetPieceValue(Board, x, y, Color, Forward=False, Up=True, Diagonal=True)
    Value += GetPieceValue(Board, x, y, Color, Forward=True, Up=False, Diagonal=True)
    return Value




def IsThereAConection(Board,x,y,Forward=None,Up=None,Diagonal=None,flag=False):
    Conter=0
    color = 0

    while ((x >= 0 and x < 7) and (y >= 0 and y < 6)):  #
        currentColor = Board[x][y]

        if(currentColor!=0):
            if (currentColor == color):
                Conter += 1
            else:
                color = currentColor
                Conter = 1
        else:
            Conter=0
            color = 0
        if (Conter >= 4):
            return True, color
        if (Conter >= 3):
            return False, color
        x, y = GetNextPos(x, y, Forward=Forward, Up=Up, Diagonal=Diagonal)

    return False, 0


def DidSomeoneWin(Board,flag=False):
    Connections=[] #
    for y in range(0, 6):  # getting the conter of all the straight forward line connections
        Connections.append(IsThereAConection(Board, 0, y, Forward=True, Up=None, Diagonal=None))

    for x in range(0, 7):  # getting the value of all the down to up line connections
        Connections.append(IsThereAConection(Board, x, 0, Forward=None, Up=True, Diagonal=None,flag=flag))

    for x in range(0, 3):  # getting the value of all dignal connections
        # getting Values from down to up dignals
        Connections.append(IsThereAConection(Board, x + 1, 0, Forward=True, Up=True, Diagonal=True))
        y = x  # just for making it easier to read and understand the code
        Connections.append(IsThereAConection(Board, 0, y, Forward=True, Up=True, Diagonal=True))

        # getting Values from up to down dignals
        Connections.append(IsThereAConection(Board, x + 1, 5, Forward=True, Up=False, Diagonal=True))
        Connections.append(IsThereAConection(Board, 0, 5 - y, Forward=True, Up=False, Diagonal=True))

#    if(flag):
#        print(Connections)
    for dir in Connections:
        if(dir[0]):
            return True, dir[1] # could be just: return dir
    return False, 0


def ConterDirections(Board,x,y,Color,Forward=None,Up=None,Diagonal=None):
    Conections = []
    maxConter=0
    Conter=0

    while ((x > 0 and x < 7) and (y > 0 and y < 6)):  #
        color = Board[x][y]
        if (color == Color):
            Conter += 1
        elif(Conter!=0):
            Conections.append(Conter)
            Conter = 0
        x, y = GetNextPos(x, y, Forward=Forward, Up=Up, Diagonal=Diagonal)

    for num in Conections:
        maxConter = max(maxConter,num)

    print(maxConter)
    return maxConter



def Evalute(Board):
    Score = [0,0] # [yellow,red]

    for line in range(0, 2):
        color = i + 1
        Score[i] += ConnectionsValue(Board,color+1)
    return Score[0]-Score[1]







def GetPieceValue(Board,x,y,Color,Forward=None,Up=None,Diagonal=None): # My first way of evaluating Position py getting value of a piece
    x,y = GetNextPos(x,y,Forward=Forward,Up=Up,Diagonal=Diagonal)

    if(x<0 or x>6 or y<0 or y>5):
        return 0

    if (Board[x][y] == 0):
        Value = 5
    if (Board[x][y] == Color):
        Value = 9
    if (Board[x][y] == ChangeColor(Color)):
        return 3
    return Value

def PieceValue(Board,x,y,Color):  # My first way of evaluating Position py getting value of a piece
    Value = GetPieceValue(Board,x,y,Color,Forward=True,Up=None,Diagonal=None)
    Value += GetPieceValue(Board, x, y, Color, Forward=False, Up=None, Diagonal=None)

    Value += GetPieceValue(Board, x, y, Color, Forward=None, Up=True, Diagonal=None)
    Value += GetPieceValue(Board, x, y, Color, Forward=None, Up=False, Diagonal=None)

    Value += GetPieceValue(Board, x, y, Color, Forward=True, Up=True, Diagonal=True)
    Value += GetPieceValue(Board, x, y, Color, Forward=False, Up=False, Diagonal=True)
    Value += GetPieceValue(Board, x, y, Color, Forward=False, Up=True, Diagonal=True)
    Value += GetPieceValue(Board, x, y, Color, Forward=True, Up=False, Diagonal=True)
    return Value



def Evalute(Board,col):
    Score = [0,0] # [yellow,red]
    if(col!=0):
        Score[col-1]+=10000

    for y in range(0, 6):
        for x in range(0, 7):
            color = Board[x][y]
            if(color!=0):
                Score[color-1] += PieceValue(Board,x,y,color)
    return Score[0]-Score[1]







def DidSomeoneWin(Board, Color):
    Conter=[] #
    for y in range(0, 5):  # getting the conter of all the straight forward line connections
        Conter.append(ConterDirections(Board, 0, y, Color, Forward=True, Up=None, Diagonal=None))

    for x in range(0, 6):  # getting the value of all the down to up line connections
        Conter.append(ConterDirections(Board, x, 0, Color, Forward=None, Up=True, Diagonal=None))

    for x in range(0, 3):  # getting the value of all dignal connections
        # getting Values from down to up dignals
        Conter.append(ConterDirections(Board, x + 1, 0, Color, Forward=True, Up=True, Diagonal=True))
        y = x  # just for making it easier to read and understand the code
        Conter.append(ConterDirections(Board, 0, y, Color, Forward=True, Up=True, Diagonal=True))

        # getting Values from up to down dignals
        Conter.append(ConterDirections(Board, x + 1, 5, Color, Forward=True, Up=False, Diagonal=True))
        Conter.append(ConterDirections(Board, 0, 5 - y, Color, Forward=True, Up=False, Diagonal=True))

    for num in Conter:
        if(num[0]>=4):
            return True,num[1]
    return False, 0




def Search(Board, Depth,Color=2):

    val = Evalute(Board,1)

    if(Depth==0 or abs(val)>Win_Value):
        return val

    AllMoves = GenerateAllPossibleMoves(Board)
    bestEvaluation = 0


    for move in AllMoves:
        row = GetRowPossiblePos(Board,move,False)
        if(row!=-1):
            Board[move][row]=Color
            evaluation = Search(Board, Depth - 1, ChangeColor(Color))
            if(Color==1):
                bestEvaluation = max(evaluation, bestEvaluation)
            elif(Color==2):
                bestEvaluation = min(evaluation, bestEvaluation)
            Board[move][row] = 0