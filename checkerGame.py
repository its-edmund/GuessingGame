from tkinter import *


class CheckerBoard():
    def __init__(self):
        self.board = {}
        for row in range(8):
            for column in range(8):
                coords = (row,column)
                if row % 2 != column % 2 and row<3:
                   self.board[coords] = 1
                elif (row % 2 != column % 2) and (row>=5):
                   self.board[coords] = 0
                else:
                    self.board[coords] = None
                
        self.currentPlayer = 0

        
    def get_piece(self, coords):
        '''ReversiBoard.get_piece(coords) -> int
        returns the piece at coords'''
        return self.board[coords]
    
    def set_piece(self,coords,currentPlayer):
        self.board[coords] = currentPlayer
    
    def check_legal_moves_firsSelect(self,coords):
        if self.board[coords] is None: 
            #print("Nopiece")
            return False
        elif self.board[coords] == self.currentPlayer:
            #print("firstSelect")
            return True                
        
    def check_legal_moves_secondSelect(self,firstcoords,secondcoords):
        if self.board[secondcoords] is not None:
            return False
        elif self.board[firstcoords] == self.currentPlayer:
            return True
        
    def try_move(self,coords):
        if self.board[coords] is not None:
            return False
        
    

class CheckerSquare(Canvas):
    def __init__(self, master, r, c, color):#, piece, player):
        '''ReversiSquare(master,r,c)
        creates a new blank Reversi square at coordinate (r,c)'''
        # create and place the widget
        Canvas.__init__(self,master,width=50,height=50,bg=color,highlightthickness=0)
        self.selected = False
#        self.piece = piece
        #self.player = player
        self.row = r
        self.column = c
        self.grid(row=r, column=c, sticky='nsew')
        # set the attributes
        self.position = (r,c)
        self.isKing = False
        
        # bind button click to placing a piece
        self.bind('<Button>',master.get_click)
        
    def select(self):
        self.create_line(0,0,0,50,fill="black",width=8)
        self.create_line(0,0,50,0,fill="black",width=8)
        self.create_line(50,0,50,50,fill="black",width=8)
        self.create_line(0,50,50,50,fill="black",width=8)
    
    def removeSelect(self):
        self.create_line(0,0,0,50,fill="dark green",width=8)
        self.create_line(0,0,50,0,fill="dark green",width=8)
        self.create_line(50,0,50,50,fill="dark green",width=8)
        self.create_line(0,50,50,50,fill="dark green",width=8)
    

    def get_position(self):
        return self.position

    def make_color(self,color):
        ovalList = self.find_all()
        for oval in ovalList:
            self.delete(oval)
    
        self.create_oval(6,6,44,44,fill =color)
       
        if self.isKing:
            self.create_text(27,27,text="*",fill="black",font="Times 30 italic bold")
    def remove_piece(self):
        ovalList = self.find_all()
        for oval in ovalList:
            self.delete(oval)
    
    def find_piece(self):
        ovalList = self.find_all()
        
    def checkIsKing(self):
        return self.isKing
        
   # def get_legal_moves(self):

class CheckerGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.board = CheckerBoard()
        self.squares = {}
        self.colors=('red','white')
        for row in range(8):
            for column in range(8):
                rc = (row, column)
                if row % 2 == column % 2:
                    self.squares[rc] = CheckerSquare(self, row, column, 'blanched almond')
                else:
                    self.squares[rc] = CheckerSquare(self, row, column, 'dark green')
                    

        self.turnSquares=CheckerSquare(self, row, column, 'light gray')
        self.turnSquares.grid(row=9,column=2)
        self.turnLabel=Label(self,text = 'Turn:',font=('Arial',18))
        self.turnLabel.grid(row=9,column=0,columnspan=2)
        self.turnSquares.make_color(self.colors[self.board.currentPlayer])
        self.update_display()
        self.firstcoords=None
        self.forwardPosition = -1
        self.needToMakeAnotherMove = False
        self.anotherTurnLabel=Label(self,text = '',font=('Arial',18))
        self.anotherTurnLabel.grid(row=9,column=4,columnspan=6)
        
    def get_click(self,event):
        selected = event.widget.get_position() 
        if selected is None:
            return
        
#        if self.firstcoords is None or self.board.get_piece(selected) is not None:
#            if len(self.getAvailableJump())>0 and selected not in self.getAvailableJump():
#                print("len(self.getAvailableJump())")
#                print(len(self.getAvailableJump()))
#                return
#            elif len(self.getAvailableJump())>0 and selected in self.getAvailableJump():
#                self.firstcoords = selected
#                self.squares[selected].select()
#                return
        
        if self.needToMakeAnotherMove:
    
            selected = event.widget.get_position() 
            if self.board.get_piece(selected) is None:
                if self.makeAnotherMove(self.firstcoords, selected, self.forwardPosition):
                     #print("selected")
                     #print(selected)
                     if self.checkAnotherMove(selected,self.forwardPosition) == False:  
                        self.board.currentPlayer = 1- self.board.currentPlayer
                        self.turnSquares.make_color(self.colors[self.board.currentPlayer])
                        self.forwardPosition = -self.forwardPosition               
        else:
           selected = event.widget.get_position() 
          
            #if self.firstcoords is None or self.board.check_legal_moves_firsSelect(selected):
           if self.firstcoords is None or self.board.get_piece(selected) is not None:
               if self.board.get_piece(selected) == self.board.currentPlayer:
#                    print("firstcoords")
#                    print(firstcoords)
#                    #len(self.getAvailableJump()")
#                    print(len(self.getAvailableJump())
                    if len(self.getAvailableJump())>0 :
                        print(len(self.getAvailableJump()))
                        if selected in self.getAvailableJump():
                            if self.firstcoords is not None:
                                self.squares[self.firstcoords].removeSelect()
                            self.firstcoords = selected
                            self.squares[selected].select()
                            return
                    else:
                        print(selected)
                        print(self.firstcoords)
                        if self.firstcoords is not None:
                            self.squares[self.firstcoords].removeSelect()
                        self.firstcoords = selected    
                        self.squares[selected].select()
           elif self.firstcoords is not None:
                selected = event.widget.get_position() 
    
                if self.board.get_piece(selected) is None:
                    self.trySecondMove(self.firstcoords,selected,self.forwardPosition)
#                    if self.trySecondMove(self.firstcoords,selected,self.forwardPosition):
#                        self.firstcoords = None
#                    if self.checkAnotherMove(selected,self.forwardPosition) == False: 
#                        self.board.currentPlayer = 1- self.board.currentPlayer
#                        self.turnSquares.make_color(self.colors[self.board.currentPlayer])
#                        self.forwardPosition = -self.forwardPosition             

    def getAvailableJump(self):
        print("GetAvailableJump")
        moves = []
        for row in range(8):
            for column in range(8):
                coords = (row,column)
                if self.board.get_piece(coords) is not None and \
                    self.board.get_piece(coords) ==self.board.currentPlayer and \
                    self.checkAvailableJump(coords):
                    moves.append(coords)
        print(len(moves))
        return moves
    
    def checkAvailableJump(self, coords):
        for dr in [self.forwardPosition]:
            for dc in [-1,1]:  
                (row,col) = (coords[0]+dr,coords[1]+dc)
                if (0 <= row < 8) and (0 <= col < 8):
                  if  self.board.get_piece((row,col)) == 1-self.board.currentPlayer:
                         (row1,col1) = (coords[0]+dr+dr,coords[1]+dc+dc)
                         if (0 <= row1 < 8) and (0 <= col1 < 8) and self.board.get_piece((row1,col1)) is None:
#                             print(row,col) 
#                             print(coords) 
#                             self.squares[(row,col)].create_text(27,27,text="7797",fill="black",font="Times 30 italic bold")
##                             self.squares[(row,col)].isKing = True
##                             self.squares[(row,col)].make_color(self.colors[self.board.currentPlayer])
##                             print(self.board.currentPlayer) 
#                             print(self.board.get_piece((row,col)))
                             return True
        return False
                

    def checkAnotherMove(self,secondcoords, forwardPosition):
         #print(secondcoords)
         if secondcoords[0]+forwardPosition<0 or secondcoords[0]+forwardPosition==8:
             #print("test123")
             self.squares[secondcoords].isKing = True
             self.squares[secondcoords].make_color(self.colors[self.board.currentPlayer])
             self.endOfTurn()    
             return
         for dr in [forwardPosition]:
            for dc in [-1,1]:  
                (row,col) = (secondcoords[0]+dr,secondcoords[1]+dc)
                if (0 <= row < 8) and (0 <= col < 8):
                  if  self.board.get_piece((row,col)) == 1-self.board.currentPlayer:
                         (row1,col1) = (secondcoords[0]+dr+dr,secondcoords[1]+dc+dc)
                         if (0 <= row1 < 8) and (0 <= col1 < 8) and self.board.get_piece((row1,col1)) is None:
                            self.needToMakeAnotherMove = True
                            self.anotherTurnLabel=Label(self,text = 'Make another move:',font=('Arial',16))
                            self.anotherTurnLabel.grid(row=9,column=4,columnspan=6)
                            self.squares[secondcoords].select()
                            self.firstcoords = secondcoords 
                            return True
         return False
                
                        
                        
    def makeAnotherMove(self,firstCoords, secondCoords, forwardPosition):
        for dr in [forwardPosition]:
            for dc in [-1,1]:  
                (row,col) = (firstCoords[0]+dr,firstCoords[1]+dc)
                if (0 <= row < 8) and (0 <= col < 8):
                  if  self.board.get_piece((row,col)) == 1-self.board.currentPlayer:
                         (row1,col1) = (firstCoords[0]+dr+dr,firstCoords[1]+dc+dc)
                         if (0 <= row1 < 8) and (0 <= col1 < 8) :
                            if (row1,col1)==secondCoords:
                                self.squares[self.firstcoords].remove_piece()
                                self.board.set_piece(self.firstcoords,None)
                                self.squares[row,col].remove_piece()
                                self.board.set_piece((row,col),None)
                                self.board.set_piece(secondCoords,self.board.currentPlayer)
                                self.squares[secondCoords].make_color(self.colors[self.board.currentPlayer])                      
                                self.needToMakeAnotherMove = False
                                self.anotherTurnLabel.destroy()

                                return True      


    def trySecondMove(self, coords,secondcoords,forwardPosition):  
        if len(self.getAvailableJump()) ==0:
            for dr in [forwardPosition]:
                for dc in [-1,1]:
                    
                    (row,col) = (coords[0]+dr,coords[1]+dc)
                    if (0 <= row < 8) and (0 <= col < 8):
                        if(row,col)==secondcoords:
                            #print("test111")
                            self.squares[self.firstcoords].remove_piece()
                            self.board.set_piece(self.firstcoords,None)
                            self.squares[secondcoords].make_color(self.colors[self.board.currentPlayer])
                            self.board.set_piece(secondcoords,self.board.currentPlayer)
                            self.firstcoords is None
                            self.endOfTurn()
                            return True
                        elif self.board.get_piece((row,col)) == 1-self.board.currentPlayer:
                             #print("test222")
                             (row1,col1) = (coords[0]+dr+dr,coords[1]+dc+dc)
                             if (0 <= row1 < 8) and (0 <= col1 < 8):
                                if (row1,col1)==secondcoords:
                                    self.squares[self.firstcoords].remove_piece()
                                    self.board.set_piece(self.firstcoords,None)
                                    self.squares[row,col].remove_piece()
                                    self.board.set_piece((row,col),None)
                                    self.squares[secondcoords].make_color(self.colors[self.board.currentPlayer])
                                    self.board.set_piece(secondcoords,self.board.currentPlayer)
                                    self.firstcoords = None
                                    print(secondcoords)
                                    if self.checkAnotherMove(secondcoords,self.forwardPosition) == False: 
                                        self.endOfTurn()
#                                        self.board.currentPlayer = 1- self.board.currentPlayer
#                                        self.turnSquares.make_color(self.colors[self.board.currentPlayer])
#                                        self.forwardPosition = -self.forwardPosition             
                                    return True      
        else:
            for dr in [forwardPosition]:
                for dc in [-1,1]:
                    
                    (row,col) = (coords[0]+dr,coords[1]+dc)
                    if (0 <= row < 8) and (0 <= col < 8):
                       if self.board.get_piece((row,col)) == 1-self.board.currentPlayer:
                             #print("test222")
                             (row1,col1) = (coords[0]+dr+dr,coords[1]+dc+dc)
                             if (0 <= row1 < 8) and (0 <= col1 < 8):
                                if (row1,col1)==secondcoords:
                                    self.squares[self.firstcoords].remove_piece()
                                    self.board.set_piece(self.firstcoords,None)
                                    self.squares[row,col].remove_piece()
                                    self.board.set_piece((row,col),None)
                                    self.squares[secondcoords].make_color(self.colors[self.board.currentPlayer])
                                    self.board.set_piece(secondcoords,self.board.currentPlayer)
                                    self.firstcoords = None
                                    print(secondcoords)
                                    if self.checkAnotherMove(secondcoords,self.forwardPosition) == False: 
                                        self.endOfTurn()
#                                        self.board.currentPlayer = 1- self.board.currentPlayer
#                                        self.turnSquares.make_color(self.colors[self.board.currentPlayer])
#                                        self.forwardPosition = -self.forwardPosition             
                                    return True      
                
                    
        return False
                    
    def endOfTurn(self):
        self.board.currentPlayer = 1- self.board.currentPlayer
        self.turnSquares.make_color(self.colors[self.board.currentPlayer])
        self.forwardPosition = -self.forwardPosition   

    def removePiece(self,coords):
        self.squares[coords].remove_piece()
        self.board.set_piece(coords,None)  
    
    def addPiece(self,coords):
        self.squares[coords].remove_piece()
        self.board.set_piece(coords,None)  
                
    def check_legal_moves_secondSelect(self,secondcoords):
        #print("test2")
        if self.squares[secondcoords] is not None:
            #print("test3")
            return False
        elif self.board.get_piece(self.firstcoords) == self.board.currentPlayer:
            #print("test1")
            return True

            
    def update_display(self):
         for row in range(8):
             for column in range(8):
                 rc=(row,column)
                 piece = self.board.get_piece(rc)
                 if piece is not None:
                     self.squares[rc].make_color(self.colors[piece])
                    
def playCheckers():
    root = Tk()
    root.title('Checkers')
    CG = CheckerGame(root)
    CG.mainloop()
    
playCheckers()