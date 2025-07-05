import sys
import io
from enum  import Enum, auto
from dataclasses import dataclass

@dataclass
class Registrador:
    valor: int


class Instrucao(Enum):
    MOVI = auto()
    ADD = auto()
    ADDI = auto()
    #colocar outras coisas dps

def inicializa_registradores() -> list[Registrador]:
    lista_valores = []
    lista_registradores = []
    for i in range(32):
        lista_registradores.append(f'r{i}')
        lista_valores.append(0)
    return lista_registradores, lista_valores    

def executa_operacoes(operacao:io.TextIOWrapper, registradores:list[int], memoria:list[int]):

    linhas = operacao.readlines()
    escreve_reg = len(linhas) # programa termina quando escrever todas os resultados instruções nos registradores
    n = 0 #indice da isntrução
    
    #Impressão inicial como visto nos exemplos:
    for op in linhas:
        linha = op.split(" ")
        instrucao = linha[0].upper()
        resto =linha[1]
        if instrucao == Instrucao.MOVI.name:
            reg, imm  = resto.split(",")
            rd = int(reg[1:])
            rs = None
            rt = None
            imm = int() 
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{op}"')
           
           
        elif instrucao == Instrucao.ADD.name:
            regs  = resto.split(",")
            rd = Registrador(int(regs[0][1:]))
            rs = Registrador(int(regs[1][1:]))
            rt = Registrador(int(regs[2][1:]))
            imm = None
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{op}"')
           
        elif instrucao == Instrucao.ADDI.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = None
            imm = int(regs[2])
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{op}"')
        
           
        else:
            print('Esta instrução não existe')
            
        n += 1
        

    while escreve_reg > 0:
        escreve_reg = 0
   
def add(rd: Registrador, rs:Registrador, rt:Registrador):
    rd.valor = rs.valor + rt.valor #soma
    return rd

def movi(rd:Registrador, rs:Registrador):
    rd.valor = rs.valor #atribuição
    return rd

def main() -> None:
    if len(sys.argv) == 2:
        nomeArq = sys.argv[1] 
        operacao = open(nomeArq, 'r')
        registradores, memoria = inicializa_registradores() #registradores = 0
        executa_operacoes(operacao, registradores, memoria)
    
    else:
        print("Faltou comandos na linha de parâmetro, deve conter: Script e Arquivo_Operações")



if __name__ == "__main__":
    main()