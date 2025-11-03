class Player:
  def __init__(self, label: int, pos: int, free: bool):
    self.__label = label
    self.__pos = pos
    self.__free = free

  def isFree(self) -> bool:
    return self.__free
  
  def getLabel(self) -> int:
    return self.__label
  
  def getPos(self) -> int:
    return self.__pos
  
  def setPos(self, pos: int):
    self.__pos = pos

  def setFree(self, free: bool):
    self.__free = free

class Board:
  def __init__(self, nPlayers: int, boardSize: int):
    self.__players = [Player(i+1, 0, True) for i in range(nPlayers)]
    self.__trapList = []
    self.__currentPlayerIndex = 0
    self.__boardSize = boardSize
    self.__gameOver = False

  def getPlayers(self) -> list[Player]:
    return self.__players

  def getBoardSize(self) -> int:
    return self.__boardSize

  def getTrapList(self) -> list[tuple[int, int]]:
    return self.__trapList

  def addTrap(self, pos: int):
    self.__trapList.append(pos)

  def rollDice(self, value):
    if self.__gameOver:
      print("game is over")
      return
  
    pIndex = self.__currentPlayerIndex
    currentPlayer = self.__players[pIndex]
    self.__currentPlayerIndex = (self.__currentPlayerIndex + 1) % len(self.__players)

    if not currentPlayer.isFree() and value % 2 == 1:
      print(f"player{currentPlayer.getLabel()} continua preso")
      return
    
    if not currentPlayer.isFree() and value % 2 == 0:
      print(f"player{currentPlayer.getLabel()} se libertou")
      currentPlayer.setFree(True)
      return
    

    currentPlayer.setPos(currentPlayer.getPos() + value)

    if currentPlayer.getPos() > self.__boardSize:
      currentPlayer.setPos(self.__boardSize)
      print(f"player{currentPlayer.getLabel()} ganhou")
      self.__gameOver = True
      return


    print(f"player{currentPlayer.getLabel()} andou para {currentPlayer.getPos()}")

    if currentPlayer.getPos() in self.__trapList:
      currentPlayer.setFree(False)
      print(f"player{currentPlayer.getLabel()} caiu em uma armadilha")

    self.__players[pIndex] = currentPlayer

  def __str__(self) -> str:
    boardStr = ""
    for player in self.__players:
      boardStr += f"player{player.getLabel()}: {self.__buildLine([player.getPos()], str(player.getLabel()))}\n"

    trapsStr = self.__buildLine(self.__trapList)

    boardStr += f"traps__: {trapsStr}"
    return boardStr
  
  def __buildLine(
      self,
      positionList: list[int],
      label: str = "x"
    ) -> str:
    lineStr = ""
    for i in range(self.__boardSize + 1):
      if i in positionList:
        lineStr += label
      else:
        lineStr += "."
    return lineStr

def main():
  board = Board(3, 20)
  while True:
    cmd = input()
    print("$" + cmd)
    args = cmd.split()

    if args[0] == "init":
      board = Board(int(args[1]), int(args[2]))
    elif args[0] == "show":
      print(board)
    elif args[0] == "addTrap":
      board.addTrap(int(args[1]))
    elif args[0] == "roll":
      board.rollDice(int(args[1]))
    elif args[0] == "end":
      break

if __name__ == "__main__":
  main()