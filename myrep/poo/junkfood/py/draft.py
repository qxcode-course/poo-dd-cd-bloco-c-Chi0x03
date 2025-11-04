class Slot:
  def __init__(self, name: str = "empty", price: float = 0.0, quantity: int = 0):
    self.__name: str = name
    self.__price: float = price
    self.__quantity: int = quantity

  def getName(self) -> str:
    return self.__name

  def getPrice(self) -> float:
    return self.__price

  def getQuantity(self) -> int:
    return self.__quantity

  def setName(self, name: str) -> None:
    self.__name = name

  def setPrice(self, price: float) -> None:
    self.__price = price

  def setQuantity(self, quantity: int) -> None:
    self.__quantity = quantity

  def __str__(self):
    return f"[{self.__name:>8} : {self.__quantity} U : {self.__price:.2f} RS]"

class Machine:
  def __init__(self, capacity: int):
    self.__capacity: int = capacity
    self.__cash: float = 0.0
    self.__profit: float = 0.0
    self.__slots: list[Slot] = [Slot() for _ in range(capacity)]

  def getSlot(self, index: int) -> Slot:
    return self.__slots[index]
  
  def setSlot(self, index: int, slot: Slot) -> None:
    if index < 0 or index >= self.__capacity:
      print("fail: indice nao existe")
      return
    
    self.__slots[index] = slot

  def clearSlot(self, index: int) -> None:
    if index < 0 or index >= self.__capacity:
      print("fail: indice nao existe")
      return
    self.__slots[index] = Slot()

  def insertCash(self, amount: float) -> None:
    if amount <= 0:
      print("fail: valor invalido")
      return
    self.__cash += amount

  def withdrawCash(self) -> float:
    withdrawn: float = self.__cash
    self.__cash = 0.0
    print(f"voce recebeu {withdrawn:.2f} RS")
    return withdrawn
  
  def buyItem(self, index: int) -> None:
    if index < 0 or index >= self.__capacity:
      print("fail: indice nao existe")
      return
    
    slot: Slot = self.__slots[index]
    if slot.getQuantity() == 0:
      print("fail: espiral sem produtos")
      return
    
    price: float = slot.getPrice()
    if self.__cash < price:
      print("fail: saldo insuficiente")
      return
    
    self.__cash -= price
    self.__profit += price
    slot.setQuantity(slot.getQuantity() - 1)
    print(f"voce comprou um {slot.getName()}")

  def __str__(self) -> str:
    finalStr: str = f"saldo: {self.__cash:.2f}\n"
    for i in range(self.__capacity):
      slot: Slot = self.__slots[i]
      finalStr += f"{i} {str(slot)}"
      if i < self.__capacity - 1:
        finalStr += "\n"
    
    return finalStr

def main():
  maquina = Machine(0)
  while True:
    cmd = input()
    print(f"${cmd}")
    args = cmd.split()
    if args[0] == "end":
      break
    elif args[0] == "show":
      print(maquina)
    elif args[0] == "set":
      index = int(args[1])

      name = args[2]
      quantity = int(args[3])
      price = float(args[4])

      slot = Slot(name, price, quantity)
      maquina.setSlot(index, slot)
    elif args[0] == "limpar":
      index = int(args[1])
      maquina.clearSlot(index)
    elif args[0] == "dinheiro":
      amount = float(args[1])
      maquina.insertCash(amount)
    elif args[0] == "troco":
      maquina.withdrawCash()
    elif args[0] == "comprar":
      index = int(args[1])
      maquina.buyItem(index)
    elif args[0] == "init":
      maquina = Machine(int(args[1]))

if __name__ == "__main__":
  main()