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
    r0  = Registrador(0)
    r1  = Registrador(0)
    r2  = Registrador(0)
    r3  = Registrador(0)
    r4  = Registrador(0)
    r5  = Registrador(0)
    r6  = Registrador(0)
    r7  = Registrador(0)
    r8  = Registrador(0)
    r9  = Registrador(0)
    r10 = Registrador(0)
    r11 = Registrador(0)
    r12 = Registrador(0)
    r13 = Registrador(0)
    r14 = Registrador(0)
    r15 = Registrador(0)
    r16 = Registrador(0)
    r17 = Registrador(0)
    r18 = Registrador(0)
    r19 = Registrador(0)
    r20 = Registrador(0)
    r21 = Registrador(0)
    r22 = Registrador(0)
    r23 = Registrador(0)
    r24 = Registrador(0)
    r25 = Registrador(0)
    r26 = Registrador(0)
    r27 = Registrador(0)
    r28 = Registrador(0)
    r29 = Registrador(0)
    r30 = Registrador(0)
    r31 = Registrador(0)

    return [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9,r10, r11, r12, r13, r14, r15, r16, r17, r18, r19,
            r20, r21, r22, r23, r24, r25, r26, r27, r28, r29,r30, r31]


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
        registradores = inicializa_registradores() #registradores = 0
        memoria = []
        for i in range(32):
            registradores.append(0)
            memoria.append(0)
        executa_operacoes(operacao, registradores, memoria)
    
    else:
        print("Faltou comandos na linha de parâmetro, deve conter: Script e Arquivo_Operações")



if __name__ == "__main__":
    main()