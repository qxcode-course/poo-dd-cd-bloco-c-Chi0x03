class Lead:
  def __init__(
    self,
    thickness: float,
    hardness: str,
    size: int
  ):
    self.__thickness = 0.0
    self.__hardness = ''
    self.__size = size
    self.__setThickness(thickness)
    self.__setHardness(hardness)

  def __setThickness(self, thickness: int):
    self.__thickness = thickness

  def getThickness(self) -> float:
    return self.__thickness

  def getHardness(self) -> str:
    return self.__hardness

  def getSize(self) -> int:
    return self.__size
  
  def setSize(self, size: int):
    self.__size = size

  def __setHardness(self, hardness: str):
    if hardness != "HB" \
      and hardness != "2B" \
      and hardness != "4B" \
      and hardness != "6B":
      print('fail: dureza invalida')
      return
    
    self.__hardness = hardness

  def usagePerSheet(self):
    match self.getHardness():
      case "HB":
        return 1
      case "2B":
        return 2
      case "4B":
        return 4
      case "6B":
        return 6
      case _:
        return 0
  
  def __str__(self) -> str:
    return f"[{self.getThickness()}:{self.getHardness()}:{self.getSize()}]"


class Pencil:
  def __init__(self, thickness: int):
    self.__thickness: int = thickness
    self.__tip: Lead | None = None
    self.__barrel: list[Lead] = []

  def insert(self, lead: Lead) -> bool:
    if lead.getThickness() != self.__thickness:
      print("fail: calibre incompatível")
      return False

    self.__barrel.append(lead)
    return True
  
  def remove(self) -> Lead | None:
    tip = self.__tip
    self.__tip = None
    return tip
  
  def pull(self):
    if self.__tip != None:
      # self.remove()
      print("fail: ja existe grafite no bico")
      return

    if len(self.__barrel) == 0:
      print("fail: vazio")
      return
    
    self.__tip = self.__barrel.pop(0)

  def writePage(self):
    if self.__tip == None:
      print("fail: nao existe grafite no bico")
      return
    
    usage = self.__tip.usagePerSheet()

    if self.__tip.getSize() == 10:
      print("fail: tamanho insuficiente")
      return

    if self.__tip.getSize() - usage < 10:
      print("fail: folha incompleta")
      self.__tip.setSize(10)
      return
    
    self.__tip.setSize(self.__tip.getSize() - usage)
    
  def __str__(self) -> str:
    tipStr = "[]" if self.__tip == None else str(self.__tip)
    barrelStr = ''.join([str(lead) for lead in self.__barrel])
    return f"calibre: {self.__thickness}, bico: {tipStr}, tambor: <{barrelStr}>"
    

lapiseira = Pencil(0.5)
def main():
  while True:
    command = input().strip()
    parts = command.split()
    print("$" + command)
    cmd = parts[0]

    if cmd == 'end':
      break
    elif cmd == 'init':
      lapiseira = Pencil(float(parts[1]))
    elif cmd == 'show':
      print(lapiseira)
    elif cmd == 'insert':
      lead = Lead(float(parts[1]), parts[2], int(parts[3]))
      lapiseira.insert(lead)
    elif cmd == 'remove':
      lapiseira.remove()
    elif cmd == 'pull':
      lapiseira.pull()
    elif cmd == 'write':
      lapiseira.writePage()
    else:
      print('fail: comando invalido')

if __name__ == '__main__':
  main()