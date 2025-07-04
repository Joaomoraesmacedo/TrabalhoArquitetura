import sys
import io
from enum  import Enum, auto

class Instrucao(Enum):
    MOVI = auto()
    ADD = auto()
    ADDI = auto()
    #colocar outras coisas dps




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
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{op}"')
           
           
        elif instrucao == Instrucao.ADD.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
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
   


def main() -> None:
    if len(sys.argv) == 2:
        nomeArq = sys.argv[1] 
        operacao = open(nomeArq, 'r')
        registradores = []
        memoria = []
        for i in range(32):
            registradores.append(0)
            memoria.append(0)
        executa_operacoes(operacao, registradores, memoria)
    
    else:
        print("Faltou comandos na linha de parâmetro, deve conter: Script e Arquivo_Operações")



if __name__ == "__main__":
    main()