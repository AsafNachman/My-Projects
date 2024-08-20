
import menu
import consts
import pygame
import time
import os
import random
import keyboard


Script_Path = os.path.dirname(os.path.abspath(__file__))

LoseVideos = []
LoseVideos.append(os.path.join(Script_Path,"videos\\Fuck You Wii Bowling.mp4"))
LoseVideos.append(os.path.join(Script_Path,"videos\\amogus twerk.mp4"))
LoseVideos.append(os.path.join(Script_Path,"videos\\MaYo oN aN EsCaLaToR.mp4"))
LoseVideos.append(os.path.join(Script_Path,"videos\\You just got coconut malled.mp4"))
LoseVideos.append(os.path.join(Script_Path,"videos\\i fucked your mom and dad.mp4"))

NiceCockPath = os.path.join(Script_Path,"videos\\Nice Cock Wii Bowling.mp4")
wtfPath = os.path.join(Script_Path,"videos\\How.mp4")


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Connect Four Ai")

class GameRunner():

    def __int__(self):
        import time

        self.win = pygame.display.set_mode((consts.WIN_WIDTH,consts.WIN_HEIGHT))
        self.Board = self.GetBoard()
        self.Pasued = True
        self.PlayerTurn1 = True
        self.PlayerTurn2 = False
        self.Winner = 0 # function: 0 = no one won, 1 = player 1 won, 2 = player 2 won
        self.MouseClickPos = False # True = get mouse pos printed when clicked
        self.time=time

        self.LeftKey = pygame.K_LEFT
        self.RightKey = pygame.K_RIGHT
        self.UpKey = pygame.K_DOWN
        self.StartKey = pygame.K_UP or pygame.K_SPACE
        self.PauseKey = pygame.K_ESCAPE

        self.Menu = menu.MainMenu()
        self.Menu.__int__()
        self.update_settings()

    def GetBoard(self): # board[x][y]
        board = [[],[],[],[],[],[],[]]
        for x in range(0, 7):
            for y in range(0, 6):
                board[x].append(0)
        return board

    def PrintBoard(self):
        for y in range(5, -1,-1):
            for x in range(0, 7):
                print(self.Board[x][y], end=" ")
            print()

    def GetCopyBoard(self, Board):
        board = []
        for x in range(0,7):
            board.append([Board[x][0]])
            for y in range(1,6):
                board[x].append(Board[x][y])
        return board


    def ChangeColor(self,Color):
        return 1 if Color==2 else 2

    def GetNextPos(self,x,y,Forward=None,Up=None,Diagonal=None):
        if (Diagonal == None):
            if (Up == None):
                x += 1 if Forward else -1
            else:
                y += 1 if Up else -1
        else:
            if (Up):
                x, y = (x + 1, y + 1) if Forward else (x - 1, y + 1)
            else:
                x, y = (x + 1, y - 1) if Forward else (x - 1, y - 1)
        return x,y


    def GetRowPossiblePos(self,Board,Col,coord=False): # coord(coordinates): True for getting pos(x,y) and False for getting place in Board
        if(0>Col or Col>6):
            return -1
        if(Board[Col][5]==0):
            for row in range(0, 6):
                if(Board[Col][row]==0):
                    if(not coord):
                        return row
                    else:
                        return (Col * consts.PIECE_WIDTH, (5 - row) * consts.PIECE_HEIGHT)
        return -1

    def update_settings(self):
        self.ColorPlayer1 = self.Menu.AllColors[self.Menu.DiscColor1]
        self.ColorPlayer2 = self.Menu.AllColors[self.Menu.DiscColor2]
        self.BattleMode = self.Menu.BattleMode[self.Menu.ModeLevel1][self.Menu.ModeLevel2].split()
        self.TypePlayer1 = self.BattleMode[0]
        self.TypePlayer2 = self.BattleMode[2]

    def Draw_Transparent_Rect(self,Pos,Color=(255, 0, 0)):
        if(Pos==-1):
            return
        s = pygame.Surface((consts.PIECE_WIDTH, consts.PIECE_HEIGHT))  # the size of your rect
        s.set_alpha(140)  # alpha level
        s.fill(Color)  # this fills the entire surface
        self.win.blit(s, Pos)


    def GenerateAllPossibleMoves(self,Board):
        Moves = []
        for x in range(0,7):
            if(Board[x][5]==0):
                Moves.append(x)
        return Moves


    def OpenFileWithDelay(self,os_loc,delay=500):
        os.startfile(os_loc)
        pygame.time.delay(delay)
        keyboard.press_and_release("alt+tab")

    def FunnyFunction(self,Future=False):
        if(Future):
            print("The bot see's that you have already lost")
        else:
            if (self.Winner == 1 and self.TypePlayer1=="Player" or self.Winner == 2 and self.TypePlayer2=="Player"):
                self.OpenFileWithDelay(NiceCockPath)
            elif (self.Winner == 1 and self.TypePlayer1=="RandomBot" or self.Winner == 2 and self.TypePlayer2=="RandomBot"):
                self.OpenFileWithDelay(wtfPath)
            elif(self.Winner == 1 and self.TypePlayer1=="AiBot" or self.Winner == 2 and self.TypePlayer2=="AiBot"):
                self.OpenFileWithDelay(LoseVideos[random.randint(0, len(LoseVideos) - 1)])

    def GetConnectionValue(self,Board,x,y,Color,Forward=None,Up=None,Diagonal=None, Print=False): # returns the value of a connection
        Value = 0
        Conter=0
        MaxPlayer = 0
        lst = []

        lastColor = Board[x][y]

        while((x >= 0 and x < 7) and (y >= 0 and y < 6)): # Get List
            currentColor = Board[x][y]
            if(lastColor!=currentColor):
                lst.append([lastColor,Conter])
                Conter=0
            Conter+=1
            lastColor = currentColor
            x, y = self.GetNextPos(x, y, Forward=Forward, Up=Up, Diagonal=Diagonal)
        if (Conter != 0):
            lst.append([lastColor, Conter])

        for i in range(len(lst)):
            if(lst[i][0]!=0):
                if(lst[i][1]>=4): # if 4 in a row
                    Value += 400 if(lst[i][0]==Color) else -400
                elif (lst[i][1] == 3): # if 3 in a row
                    if(i>0): # if thers a possiblity of a connection from the left +30 value
                        if(lst[i-1][0]==0):
                            Value += 30 if (lst[i][0]==Color) else -30
                    if(i<len(lst)-1): # if thers a possiblity of a connection from the right +30 value
                        if (lst[i + 1][0] == 0):
                            Value += 30 if (lst[i][0] == Color) else -30
        return Value


    def Evalute(self,Board,Color,Print=False):  # Evaluates the position by getting value of all the connections
        Value = 0
        for y in range(0,6): # getting the value of all the straight forward line connections
            Value += self.GetConnectionValue(Board,0,y,Color,Forward=True,Up=None,Diagonal=None)

        for x in range(0,7): # getting the value of all the down to up line connections
            Value += self.GetConnectionValue(Board, x, 0, Color, Forward=None, Up=True, Diagonal=None)

        for x in range(0,3): # getting the value of all dignal connections
            # getting Values from down to up dignals
            Value += self.GetConnectionValue(Board, x+1, 0, Color, Forward=True, Up=True, Diagonal=True)
            y = x  # just for making it easier to read and understand the code
            Value += self.GetConnectionValue(Board, 0, y, Color, Forward=True, Up=True, Diagonal=True)

            # getting Values from up to down dignals
            Value += self.GetConnectionValue(Board, x+1, 5, Color, Forward=True, Up=False, Diagonal=True)
            Value += self.GetConnectionValue(Board, 0, 5-y, Color, Forward=True, Up=False, Diagonal=True)
        if(Print):
            print(f"Bot{Color} Evaluation of his possition:",Value)
        return Value



    # the function simulates all the next Depth number of moves ahead and finds the best evalution if both players play the best moves

    def Search(self,Board, Depth, alpha=-1000, beta=1000, Color=2, OriginalColor = 1): # summery: evalutes all possibilities and return best one
        val = self.Evalute(Board,OriginalColor)

        if(Depth==0 or abs(val)> consts.Win_Value):
            return val


        AllMoves = self.GenerateAllPossibleMoves(Board)

        if(Color == OriginalColor):
            maxEval = -1000
            for move in AllMoves:
                row = self.GetRowPossiblePos(Board, move)
                if (row != -1):
                    Board[move][row] = Color
                    eval = self.Search(Board, Depth - 1, alpha, beta, self.ChangeColor(Color),OriginalColor)
                    maxEval = max(eval, maxEval)
                    alpha = max(alpha, maxEval)
                    Board[move][row] = 0
                    if(beta<=alpha):
                        break
            if(maxEval == -1000):
                return 0
            return maxEval

        elif(Color==self.ChangeColor(OriginalColor)):
            minEval = 1000
            for move in AllMoves:
                row = self.GetRowPossiblePos(Board, move)
                if (row != -1):
                    Board[move][row] = Color
                    eval = self.Search(Board, Depth - 1, alpha, beta, self.ChangeColor(Color),OriginalColor)
                    minEval = min(eval, minEval)
                    beta = min(beta, minEval)
                    Board[move][row] = 0
                    if (beta <= alpha):
                        break
            return minEval





    def BestMove(self,Board, Depth,Color=1): # find best move
        AllMoves = self.GenerateAllPossibleMoves(Board)
        evaluations = [-1000,-1000,-1000,-1000,-1000,-1000,-1000]
        BestMove = 0

        for move in AllMoves:
            row = self.GetRowPossiblePos(Board,move)
            if (row != -1):
                Board[move][row]=Color
                evaluations[move] = self.Search(Board, Depth,Color=self.ChangeColor(Color),OriginalColor = Color)
                Board[move][row] = 0

        if(self.GetRowPossiblePos(Board,3)!=5):
            evaluations[3] +=50

        evaluations[4] += 3
        evaluations[2] += 3

        evaluations[5] += 2
        evaluations[1] += 2

        evaluations[6] += 1
        evaluations[0] += 1

        BestVal = evaluations[0]
        for i in range(1,len(evaluations)):
            if(BestVal < evaluations[i]):
                BestVal = evaluations[i]
                BestMove=i

        if (self.Menu.Funny): # if funny function on/off
            if (evaluations[BestMove] > consts.Win_Value): # if bot think he will win funny video pops up
                self.FunnyFunction(Future=True)

        print(f"Bot{Color} Best Possition Eval:",evaluations[BestMove])
        print(f"Bot{Color} Best Move:", BestMove)
        return BestMove



    # summery - check if someone won or if there is a tie

    # explanation: return = bool,int = True/False, 0/1/2/3
    # True = Pause game, False = Game Not Paused
    # 0 = no one won, 1 = player 1 won, 2 = player 2 won, 3 = Tie
    def CheckWinner(self,Board):
        val = self.Evalute(Board, 1)
        if (abs(val) > consts.Win_Value):
            if (val > 0):
                return True, 1
            else:
                return True, 2
        for x in range(0,7):
            if(Board[x][5]!=0):
                pass
            else:
                return False, 0
        return True, 3


    def AiBot(self, BotColor, Random=False):
        if(Random):
            self.Random_Bot(BotColor)  # Random Bot
        else:
            Depth = self.Menu.DepthBot1 if (BotColor == 1) else self.Menu.DepthBot2  # get the depth of the bot by their number
            bestMove = self.BestMove(self.GetCopyBoard(self.Board), Depth, Color=BotColor)  # get best move # finding the best move with a copy of the board
            pygame.time.delay(2000)
            row = self.GetRowPossiblePos(self.Board,bestMove) # get lowest row to put the piece

            if(self.win!=None): # after it found best move, put it on the Real board
                Color = self.ColorPlayer1 if(BotColor==1) else self.ColorPlayer2
                self.PieceFallingAnimation(bestMove, row, self.get_colors_by_turns()[1])  # piece falling animation
            self.Board[bestMove][row] = BotColor  # puting the piece in the connect 4 matrix


    def PlayerFunction(self, PlayerColor, Animation=True, Color=consts.RED):
        col = int(pygame.mouse.get_pos()[0] / 100)
        row = self.GetRowPossiblePos(self.Board, col)
        if (row != -1):
            if(Animation):
                self.PieceFallingAnimation(col, row, Color)
            self.Board[col][row] = PlayerColor
        else:
            return False
        return True


    def Random_Bot(self,BotColor,Animation=True): # Bot that plays random moves
        row = -1
        while (row == -1):
            col = random.randint(0, 7)
            row = self.GetRowPossiblePos(self.Board, col)
        if (Animation):
            self.PieceFallingAnimation(col, row, self.get_colors_by_turns()[1])
        self.Board[col][row] = BotColor
        pygame.time.delay(300)


    def PieceFallingAnimation(self, col, row, color):
        y = -consts.PIECE_HEIGHT
        Goal_Of_Y = consts.PIECE_HEIGHT * (5 - row) + 50
        while (y != Goal_Of_Y):  # Falling Animation
            pygame.draw.rect(self.win, consts.WHITE, pygame.Rect(0, 0, consts.WIN_WIDTH, consts.WIN_WIDTH))  # Draw consts.WHITE Background
            pygame.draw.circle(self.win, color,(consts.PIECE_WIDTH * col+50, y) , 50) # Draw Piece
            self.draw_window(Animation=True)
            y += 5


    def draw_board_and_pieces(self):
        for y in range(5, -1, -1): # Draw pieces
            for x in range(0, 7):
                if (self.Board[x][y] == 1):  # draw consts.YELLOW
                    pygame.draw.rect(self.win, self.ColorPlayer1, pygame.Rect(consts.PIECE_WIDTH * x, consts.PIECE_HEIGHT * (5 - y), consts.PIECE_WIDTH, consts.PIECE_HEIGHT))
                if (self.Board[x][y] == 2):  # draw consts.RED
                    pygame.draw.rect(self.win, self.ColorPlayer2, pygame.Rect(consts.PIECE_WIDTH * x, consts.PIECE_HEIGHT * (5 - y), consts.PIECE_WIDTH, consts.PIECE_HEIGHT))
        self.win.blit(consts.BOARD_IMG, (0, 0))


    def get_colors_by_turns(self): # if player x turn, change the values being sent
        if (self.PlayerTurn1):
            return 1, self.ColorPlayer1
        elif (self.PlayerTurn2):
            return 2, self.ColorPlayer2


    def change_turns(self):
        self.PlayerTurn1 = False if (self.PlayerTurn1) else True
        self.PlayerTurn2 = False if (self.PlayerTurn2) else True


    def draw_text(self):
        play_text = self.Menu.create_text("Click right click to start", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT / 4,consts.WIN_HEIGHT / 10)
        back_text = self.Menu.create_text("Back", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT * 0.7, consts.WIN_WIDTH / 8,consts.DARK_PURPLE)
        self.win.blit(play_text[0], play_text[1])
        self.win.blit(back_text[0], back_text[1])

        if (self.Winner != 0):
            if (self.Winner == 1):
                txt = "Player1 Won!"
                text_color = consts.GREEN
            elif (self.Winner == 2):
                txt = "Player2 Won"
                text_color = consts.ORANGE
            elif (self.Winner == 3):
                txt = "Player1 And Player2 Tied"
                text_color = consts.CYAN
            winner_text = self.Menu.create_text(txt, consts.WIN_WIDTH / 2, consts.WIN_HEIGHT / 4 + 100,consts.WIN_HEIGHT / 12, text_color=text_color)
            self.win.blit(winner_text[0], winner_text[1])


    def draw_window(self, Animation=False , TransColor=consts.RED):
        if(not Animation): # draw Transparent circle where the piece will fall into
            pygame.draw.rect(self.win, consts.WHITE, pygame.Rect(0, 0, consts.WIN_WIDTH, consts.WIN_WIDTH))
            self.Draw_Transparent_Rect(self.GetRowPossiblePos(self.Board, int(pygame.mouse.get_pos()[0] / 100), coord=True), Color= TransColor)

        self.draw_board_and_pieces() # draw board and pieces function

        if (self.Pasued): # if paused draw text
            self.draw_text()

        pygame.display.update() # update window


    def main(self):
        BackText = self.Menu.create_text("Back", consts.WIN_WIDTH / 2, consts.WIN_HEIGHT * 0.7, consts.WIN_WIDTH / 8,consts.DARK_PURPLE)
        self.update_settings()
        while True:
            clock.tick(30)

            if self.Menu.in_menu:
                self.Menu.game_menu()

            if self.Menu.in_settings:
                self.Menu.game_settings()

            if self.Menu.in_guide:
                self.Menu.game_guide()

            if not self.Menu.in_menu and not self.Menu.in_settings:
                self.update_settings()
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN: # if pressed on keyboard
                        if (self.PauseKey): # if pressed on PauseKey(Esc), unpause game
                            self.Pasued = True
                        if event.key == self.StartKey and self.Pasued: # if pressed on StartKey(Up arrow), unpause game and create new Board
                            self.Board = self.GetBoard()
                            self.Pasued = False
                    elif event.type == pygame.MOUSEBUTTONUP and self.Pasued: # if pressed on mouse
                        if self.Menu.is_click_on_rect(BackText[1]): # if click on back, return to menu
                            self.Menu.in_menu = True
                        elif event.button == 3: # if pressed on StartKey(Right Click), unpause game and create new Board
                            self.Board = self.GetBoard()
                            self.Pasued = False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if (self.MouseClickPos): # True = get mouse pos printed when clicked - for devloper reasons
                        if (event.type == pygame.MOUSEBUTTONUP):
                            print(pygame.mouse.get_pos())

                    if(not self.Pasued): # player event function
                        for i,type in enumerate([self.TypePlayer1,self.TypePlayer2],1):
                            if(type=="Player"):

                                PlayerColor,Color = self.get_colors_by_turns() # if player x turn, change the values being sent
                                if(PlayerColor==i):
                                    if event.type == pygame.MOUSEBUTTONUP:
                                        if event.button == 1:
                                            Possible = self.PlayerFunction(PlayerColor,Animation=True,Color=Color)
                                            if(Possible):
                                                self.change_turns()
                                                break
                                    elif event.type == pygame.KEYDOWN:
                                        pos = pygame.mouse.get_pos()
                                        val = consts.PIECE_WIDTH
                                        if event.key == self.LeftKey and pos[0]-val>0:
                                            pygame.mouse.set_pos(pos[0]-val,pos[1])
                                        if event.key == self.RightKey and pos[0]+val<consts.WIN_WIDTH:
                                            pygame.mouse.set_pos(pos[0]+val,pos[1])
                                        if(event.key == self.UpKey):
                                            Possible = self.PlayerFunction(PlayerColor,Animation=True,Color=Color)
                                            if (Possible):
                                                self.change_turns()
                                                break
                                    self.Pasued, self.Winner = self.CheckWinner(self.Board)
                                    if(self.Pasued):
                                        break

                if (not self.Pasued):
                    self.Pasued, self.Winner = self.CheckWinner(self.Board)

                    if(self.Menu.Funny):
                        self.FunnyFunction(Future=False)

                    for i,type in enumerate([self.TypePlayer1, self.TypePlayer2],1):
                        if(type != "Player"):
                            TurnNumber=1 if(self.PlayerTurn1) else 2
                            if (TurnNumber == i):
                                if(type == "AiBot"):
                                    self.AiBot(i)
                                elif(type == "RandomBot"):
                                    self.AiBot(i,Random=True)
                                self.change_turns()
                                self.Pasued, self.Winner = self.CheckWinner(self.Board)
                                if (self.Pasued or type == "AiBot"):
                                    break

                TransColor=self.ColorPlayer1 if(self.PlayerTurn1) else self.ColorPlayer2
                self.draw_window(Animation=False, TransColor=TransColor)




if __name__ == "__main__":
    gameClass = GameRunner()
    gameClass.__int__()
    gameClass.main()