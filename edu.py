import sys
import io
from enum  import Enum, auto
from dataclasses import dataclass
from typing import Optional


class Comando(Enum):
    MOVI = auto()
    ADD = auto()
    ADDI = auto()
    #colocar outras coisas dps

@dataclass
class Instrucao:
    inst: Comando
    rd: Optional[int]
    rs: Optional[int]
    rt: Optional[int]
    imm: Optional[int]

def inicializa_registradores() -> list:
    lista_valores = []
    lista_registradores = []
    for i in range(32):
        lista_registradores.append(f'R{i}')
        lista_valores.append(0)
    return lista_registradores, lista_valores  

def lista_instrucoes(linhas:list[str]) -> list[Instrucao]:
    lista: list[Instrucao] = []
    n = 0 #indice da isntrução

    
    #Impressão inicial como visto nos exemplos:
    for op in linhas:
        linha = op.split(" ")
        instrucao = linha[0].upper()
        resto =linha[1]
        if instrucao == Comando.MOVI.name:
            reg, imm  = resto.split(",")
            rd = int(reg[1:])
            rs = None
            rt = None
            imm = int() 
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{op}"')
            executa = Instrucao(Comando.MOVI, rd, rs, rt, imm)
            
           
           
        elif instrucao == Comando.ADD.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{op}"')
            executa = Instrucao(Comando.ADD, rd, rs, rt, imm)
           
        elif instrucao == Comando.ADDI.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = None
            imm = int(regs[2])
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{op}"')
            executa = Instrucao(Comando.ADDI, rd, rs, rt, imm)
        
           
        else:
            print('Esta instrução não existe')
            
        n += 1
        lista.append(executa)
        print(lista)
        return lista

def executa_operacoes(operacao:io.TextIOWrapper, nome_reg:list[str], valor_reg:list[int], memoria:list[int]):

    linhas = operacao.readlines()
    escreve_reg = len(linhas) # programa termina quando escrever todas os resultados instruções nos registradores
    lista_inst = lista_instrucoes(linhas)
    
        

    while escreve_reg > 0:
        escreve_reg = 0
   


def main() -> None:
    if len(sys.argv) == 2:
        nomeArq = sys.argv[1] 
        operacao = open(nomeArq, 'r')
        nome_reg, valor_reg = inicializa_registradores() #registradores = 0
        memoria = [] #VERIFICAR COMO QUE INICIALIZA A MEMORIA 
        for i in range(32):
            memoria.append(0)
        executa_operacoes(operacao, nome_reg, valor_reg, memoria)
    
    else:
        print("Faltou comandos na linha de parâmetro, deve conter: Script e Arquivo_Operações")



if __name__ == "__main__":
    main()