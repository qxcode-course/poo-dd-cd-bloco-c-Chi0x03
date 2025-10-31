class Foo:
  def __init__(self, x):
    self.x = x

  def __str__(self):
    return f"Foo({self.x})"

lista_vazia: list[int] = []
lista_preenchida: list[int] = [1, 2, 3, 4, 5]
lista_preenchida_objetos: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]

lists_objetos_str = [str(obj) for obj in lista_preenchida_objetos]

lista_preenchida_objetos.pop()

print("Lista vazia:", lista_vazia)
print("Lista preenchida:", lista_preenchida)
# print("Lista preenchida com objetos:", lista_preenchida_objetos)
print("Lista preenchida com objetos (strings):", lists_objetos_str)