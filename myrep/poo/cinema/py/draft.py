class Client:
  def __init__(self, id: str, name: str, phone: int) -> None:
    self.__id = id
    self.__name = name
    self.__phone = phone

  def getName(self) -> str:
    return self.__name

  def __str__(self) -> str:
    return f"{self.__name}:{self.__phone}"


class Theater:
  def __init__(self, capacity: int) -> None:
    self.__capacity = capacity
    self.__seats: list[Client | None] = [None] * capacity

  def getSeats(self) -> list[Client | None]:
    return self.__seats
  
  def reserve(self, id: str, name: str, phone: int, index: int) -> bool:
    if not self.__verifyIndex(index):
      print("fail: cadeira nao existe")
      return False
    if self.__seats[index] is not None:
      print("fail: cadeira ja esta ocupada")
      return False
    if self.__search(name) != -1:
      print("fail: cliente ja esta no cinema")
      return False
    self.__seats[index] = Client(id, name, phone)
    return True
  
  def cancel(self, name: str) -> bool:
    index = self.__search(name)
    if index == -1:
      print("fail: cliente nao esta no cinema")
      return False
    self.__seats[index] = None
    return True

  def __verifyIndex(self, index: int) -> bool:
    return 0 <= index < self.__capacity

  def __search(self, name: str):
    for i, client in enumerate(self.__seats):
      if client is not None and client.getName() == name:
        return i
    return -1
  
  def __str__(self):
    seats_str = ["-" if seat is None else str(seat) for seat in self.__seats]
    return f"[{' '.join(seats_str)}]"
  
def main():
  cinema = Theater(0)
  while True:
    cmd = input()
    print("$" + cmd)
    args = cmd.split()

    if args[0] == "end":
      break
    elif args[0] == "show":
      print(cinema)
    elif args[0] == "init":
      cinema = Theater(int(args[1]))
    elif args[0] == "reserve":
      name = args[1]
      phone = int(args[2])
      seat = int(args[3])
      cinema.reserve(id, name, phone, seat)
    elif args[0] == "cancel":
      name = args[1]
      cinema.cancel(name)
    else:
      print("fail: comando invalido")

if __name__ == "__main__":
  main()