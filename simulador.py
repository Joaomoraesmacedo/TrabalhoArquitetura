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
    text: str


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
    
    for op in linhas:
        text = op.strip()
        linha = op.split(" ")
        instrucao = linha[0].upper()
        resto =linha[1]
        
        if instrucao == Comando.MOVI.name:
            reg, imm_str  = resto.split(",")
            rd = int(reg[1:])
            rs = None
            rt = None
            imm = int(imm_str)
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.MOVI, rd, rs, rt, imm, text)
            lista.append(executa)
           
           
        elif instrucao == Comando.ADD.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.ADD, rd, rs, rt, imm, text)
            lista.append(executa)
           
        elif instrucao == Comando.ADDI.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = None
            imm = int(regs[2])
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.ADDI, rd, rs, rt, imm, text)
            lista.append(executa)
        
           
        else:
            print('Esta instrução não existe')
        
            
        n += 1
    return lista

def calcula_caracteres(instrucao: str)-> str:
    if len(instrucao) < 15:
        falta = 15 - len(instrucao)
        resultado = instrucao
        if falta % 2 == 0:
            for _ in range(falta // 2):
                resultado = " " + resultado
                resultado = resultado + " "
        else:
            for _ in range(falta // 2):
                resultado = " " + resultado
                resultado = resultado + " "
            resultado = " " + resultado
        return resultado
    else:
        return instrucao                 

def indentifica_noop(lista:list[str], op: int):
    if 0 <= op < len(lista):
        return lista[op].strip()
    else:
        return "NOOP"

def busca_inst(pipeline: list, lista_inst: list[Instrucao], pc: int) -> int:
    if pc < len(lista_inst):
        pipeline[0] = lista_inst[pc]
        pc +=1 
    else:
        pipeline[0] = None
    return pc

def verica_hazard(pipeline: list[Instrucao]) -> int:
    '''Retorna int do hazard que esta mais proximo da instrução, ou seja, aquele que irá demorar mais para ser resolvido'''
    if pipeline[1] is not None:
        for i in range(3,1,-1):
            if pipeline[i] is not None:
                if pipeline[1].rs == pipeline[i].rd or pipeline[1].rt == pipeline[i].rd:
                    return  pipeline[i].rd
    return None

        
def executa_operacoes(operacao:io.TextIOWrapper, nome_reg:list[str], valor_reg:list[int], memoria:list[int]):

    linhas = operacao.readlines()
    lista_inst = lista_instrucoes(linhas)
    pipeline: list[Instrucao] = [None,None,None,None,None] #pipeline com as operacoes 
    tam = len(pipeline) - 1
    pc = 0 #inicia o pc 
    str_pipeline = "|-----Busca-----||---Decodifica--||---Executa-----||---Memoria-----||----Regist-----|" #15 caracteres dentro de cada /
    comando = True
   
    while comando:
        
        hazard = verica_hazard(pipeline) 
        if hazard is not None:
            for i in range(4,2,-1):
                pipeline[i] = pipeline[i - 1]
            pipeline[2] = None


        else:
            for i in range(tam, 0, -1):
                pipeline[i] = pipeline[i - 1]

            # Busca a próxima instrução
            pc = busca_inst(pipeline, lista_inst, pc)

       

        
        #Verifica se todos os estagios do pipeline ta vazio 
        verifica_noop = True 
        for i in pipeline:
            if i != None:
                verifica_noop = False
        if verifica_noop and pc>= len(lista_inst):
            comando = False
        saida = "  "
        for i in pipeline:
            if i is not None:
                saida += i.text +"  "
            else:
                saida += "NOOP   " 

        print(str_pipeline)
        print(saida)
        nomes = "  "
        for i in nome_reg:
            nomes += i + "  "
        print(nomes)
        print(valor_reg)
        print(pc)
        if pipeline[4] is not None: #faz a execucao de instrucoes 
            instrucao: Instrucao = pipeline[4]
            rd = instrucao.rd  
            rs = instrucao.rs
            rt = instrucao.rt 
            imm = instrucao.imm

            #Dar um  jeito de armazenar esse valor e usar dps que o registro saiu desse estado
            if instrucao.inst == Comando.MOVI:      
                valor_reg[rd] = imm
            elif instrucao.inst == Comando.ADD:
                valor_reg[rd] = valor_reg[rs] + valor_reg[rt]
            elif instrucao.inst == Comando.ADDI:
                valor_reg[rd] = valor_reg[rs] + imm
        
    ''''while escreve_reg > 0:
            print(str_pipeline)
            print(f"|{calcula_caracteres(indentifica_noop(linhas, i))}||{calcula_caracteres(indentifica_noop(linhas, i - 1))}||{calcula_caracteres(indentifica_noop(linhas, i-2))}||{calcula_caracteres(indentifica_noop(linhas, i - 3))}||{calcula_caracteres(indentifica_noop(linhas, i - 4 ))}|") # pipeline 
            print(" ")
            print("Registradores: ")
            print("  ".join(nome_reg[:10]) + " ".join(nome_reg[10:])) #join junta todas as str da lista (quando o R tinha dois digitos, estava desalinhando com o valor)
            for valor in valor_reg:
                print(f"{valor}  ", end=" ") # valores registradores
            print()
            print()    
            print(f"Memória: {memoria}")
            print(f"PC:{pc} ")
            print(f"rd: rs: rt: imm: opcode: text: ")                
            print()
            print()
            i = i + 1
            escreve_reg = escreve_reg - 1
            print(f"escreve_reg restante: {escreve_reg}")

            
        
        #Escrever todo o codigo aqui primeiro BI, BO EX, EI (escreve_reg incrementa aqui) depois implementar hazards 
        #Somente utilizando a lista_inst a instrução 0 está no indice 0 e assim por diante 
        #Para saber o que esta na lista execute no terminal: python3 simulador.py add_mov.txt
        '''
   


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