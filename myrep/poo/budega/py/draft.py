class Person:
  def __init__(self, name: str):
    self.__name = ''
    self.setName(name)

  def setName(self, name: str) -> None:
    self.__name = name

  def getName(self) -> str:
    return self.__name

class Market:
  def __init__(self, countersMax: int):
    self.__counters: list[Person | None] = [None] * countersMax
    self.__countersMax = countersMax
    self.__waiting: list[Person] = []

  def arrive(self, person: Person) -> None:
    self.__waiting.append(person)

  def call(self, index: int) -> None:
    if index < 0 or index >= self.__countersMax:
      print("Counter index out of range")
      return
    
    if self.__counters[index] is not None:
      print("fail: caixa ocupado")
      return
    
    if not self.__waiting:
      print("fail: sem clientes")
      return
    
    person = self.__waiting.pop(0)
    self.__counters[index] = person

  def finish(self, index: int) -> Person | None:
    if index < 0 or index >= self.__countersMax:
      print("fail: caixa inexistente")
      return
    
    if self.__counters[index] is None:
      print("fail: caixa vazio")
      return
    
    person = self.__counters[index]
    self.__counters[index] = None
    return person

  def __str__(self) -> str:
    countersArr = [counter.getName() if counter is not None else '-----' for counter in self.__counters]
    waitingArr = [person.getName() for person in self.__waiting]
    return f"Caixas: [{", ".join(countersArr)}]\nEspera: [{", ".join(waitingArr)}]"

market = Market(3)

def main():
  while True:
    command = input()
    args = command.split()
    print("$" + command)

    if args[0] == "show":
      print(market)
    elif args[0] == "init":
      market = Market(int(args[1]))
    elif args[0] == "arrive":
      person = Person(args[1])
      market.arrive(person)
    elif args[0] == "call":
      market.call(int(args[1]))
    elif args[0] == "finish":
      person = market.finish(int(args[1]))
    elif args[0] == "end":
      break
    else:
      print("fail: comando invalido")

if __name__ == "__main__":
  main()