from enum  import Enum, auto

class Instrucao(Enum):
    MOVI = auto()

registradores = []
memoria = []
for i in range(32):
            registradores.append(i)
            memoria.append(i)
print(registradores)
if 'MOVI' == Instrucao.MOVI.name:
    print(Instrucao.MOVI.name, 'oi')


lista = [1,2,3]
resto = lista[1:]
print(resto)