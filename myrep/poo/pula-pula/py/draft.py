class Kid:
  def __init__(self, name: str, age: int):
    self.__name: str = ''
    self.__age: int = 0
    self.setAge(age)
    self.setName(name)

  def getName(self):
    return self.__name
  
  def setName(self, name):
    self.__name = name

  def getAge(self):
    return self.__age

  def setAge(self, age):
    self.__age = age

  def __str__(self):
    return f"{self.__name}:{self.__age}"

class Trampoline:
  def __init__(self):
    self.__playing: list[Kid] = []
    self.__waiting: list[Kid] = []

  def arrive(self, kid: Kid):
    self.__waiting.insert(0, kid)

  def enter(self):
    if len(self.__waiting) == 0:
      return
    
    kid = self.__waiting.pop()
    self.__playing.insert(0, kid)

  def leave(self):
    if len(self.__playing) == 0:
      return
    
    kid = self.__playing.pop()
    self.__waiting.insert(0, kid)

  def remove(self, name: str):
    kid = self.__removeFromList(name, self.__playing)
    if kid is not None:
      return
    
    kid = self.__removeFromList(name, self.__waiting)
    if kid is not None:
      return
    
    print(f"fail: {name} nao esta no pula-pula")

  def __removeFromList(self, name: str, lst: list[Kid]) -> Kid | None:
    for i in range(len(lst)):
      if lst[i].getName() == name:
        return lst.pop(i)
    return None
  
  def __str__(self):
    playing_str = ', '.join(str(kid) for kid in self.__playing)
    waiting_str = ', '.join(str(kid) for kid in self.__waiting)
    return f"[{waiting_str}] => [{playing_str}]"

pulaPula = Trampoline()
def main():
  while True:
    command = input()
    print("$" + command)
    args = command.split()
    
    if args[0] == "arrive":
      kid = Kid(args[1], int(args[2]))
      pulaPula.arrive(kid)
    elif args[0] == "enter":
      pulaPula.enter()
    elif args[0] == "leave":
      pulaPula.leave()
    elif args[0] == "remove":
      pulaPula.remove(args[1])
    elif args[0] == "show":
      print(pulaPula)
    elif args[0] == "end":
      break
    else:
      print("Unknown command.")

if __name__ == "__main__":
  main()