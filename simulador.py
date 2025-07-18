import sys
import io
from enum  import Enum, auto
from dataclasses import dataclass
from typing import Optional


class Comando(Enum):
    ADD = auto()
    ADDI = auto()
    SUB = auto()
    SUBI = auto()
    MUL = auto()
    DIV = auto()
    MOD = auto()
    BLT = auto()
    BGT = auto()
    BEQ = auto()
    J = auto()
    LW = auto()
    SW = auto()
    MOV = auto()
    MOVI = auto()

@dataclass
class Instrucao:
    inst: Comando
    rd: Optional[int]
    rs: Optional[int]
    rt: Optional[int]
    imm: Optional[int]
    text: str

@dataclass
class Resultado:
    inst: Comando
    posi: Optional[int] 
    valor: Optional[int] 

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
           
        if instrucao == Comando.ADD.name:
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
        
        elif instrucao == Comando.SUB.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.SUB, rd, rs, rt, imm, text)
            lista.append(executa)
        
        elif instrucao == Comando.SUBI.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = None
            imm = int(regs[2])
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.SUBI, rd, rs, rt, imm, text)
            lista.append(executa)
        
        elif instrucao == Comando.MUL.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.MUL, rd, rs, rt, imm, text)
            lista.append(executa)
        
        elif instrucao == Comando.DIV.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.DIV, rd, rs, rt, imm, text)
            lista.append(executa)
        
        elif instrucao == Comando.MOD.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.MOD, rd, rs, rt, imm, text)
            lista.append(executa)
        
        elif instrucao == Comando.BLT.name:
            regs  = resto.split(",")
            rd = None
            rs = int(regs[0][1:])
            rt = int(regs[1][1:])
            imm = int(regs[2])
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.BLT, rd, rs, rt, imm, text)
            lista.append(executa)
        
        elif instrucao == Comando.BGT.name:
            regs  = resto.split(",")
            rd = None
            rs = int(regs[0][1:])
            rt = int(regs[1][1:])
            imm = int(regs[2])
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.BGT, rd, rs, rt, imm, text)
            lista.append(executa)
        
        elif instrucao == Comando.BEQ.name:
            regs  = resto.split(",")
            rd = None
            rs = int(regs[0][1:])
            rt = int(regs[1][1:])
            imm = int(regs[2])
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.BEQ, rd, rs, rt, imm, text)
            lista.append(executa)
        
        elif instrucao == Comando.J.name:
            rd = None
            rs = None
            rt = None
            imm = linha[2]
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.J, rd, rs, rt, imm, text)
            lista.append(executa)
    
        elif instrucao == Comando.LW.name:
            regs = resto.split(",")
            rd =  int(regs[0][1:])
            valor = regs[1].split("(")
            imm = int(valor[0])
            rs = int(valor[1].strip()[1:].replace(")", ""))
            rt = None
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.LW, rd, rs, rt, imm, text)
            lista.append(executa)


        elif instrucao == Comando.SW.name:
            regs = resto.split(",")
            rs =  int(regs[0][1:])
            valor = regs[1].split("(")
            imm = int(valor[0])
            rt = int(valor[1].strip()[1:].replace(")", ""))
            rd = None
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.SW, rd, rs, rt, imm, text)
            lista.append(executa)
        
        elif instrucao == Comando.MOV.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = None
            rt = None
            imm = int(regs[2])
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.MOV, rd, rs, rt, imm, text)
            lista.append(executa)

        elif instrucao == Comando.MOVI.name:
            reg, imm_str  = resto.split(",")
            rd = int(reg[1:])
            rs = None
            rt = None
            imm = int(imm_str)
            print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
            executa = Instrucao(Comando.MOVI, rd, rs, rt, imm, text)
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

def executa_inst(pipeline: list[Instrucao], valor_reg: list[int], memoria: list[int], resultados: list[Resultado]) -> bool:
    '''Retorna se houve jump'''
    if pipeline[2] is not None: 
            instrucao: Instrucao = pipeline[2]
            rd = instrucao.rd  
            rs = instrucao.rs
            rt = instrucao.rt 
            imm = instrucao.imm

            
            if instrucao.inst == Comando.ADD:
                posi = rd
                valor = valor_reg[rs] + valor_reg[rt]
                result = Resultado(Comando.ADD,posi, valor)

            elif instrucao.inst == Comando.ADDI:
                posi = rd
                valor = valor_reg[rs] + imm
                result = Resultado(Comando.ADD,posi, valor)

            elif instrucao.inst == Comando.SUB:
                posi = rd
                valor = valor_reg[rs] - valor_reg[rt]
                result = Resultado(Comando.SUB,posi, valor)
            
            elif instrucao.inst == Comando.SUBI:  
               posi = rd    
               valor = valor_reg[rs] - imm
               result = Resultado(Comando.SUBI,posi, valor)
            
            elif instrucao.inst == Comando.MUL:  
               posi = rd    
               valor = valor_reg[rs] * valor_reg[rt]
               result = Resultado(Comando.MUL,posi, valor)

            elif instrucao.inst == Comando.DIV:  
               posi = rd    
               valor = valor_reg[rs] / valor_reg[rt]
               result = Resultado(Comando.DIV,posi, valor)
            
            elif instrucao.inst == Comando.MOD:  
               posi = rd    
               valor = valor_reg[rs] % valor_reg[rt]
               result = Resultado(Comando.MOD,posi, valor)

            elif instrucao.inst == Comando.BLT:  
               posi = None
               if valor_reg[rs] < valor_reg[rt]:
                    valor = imm #Verificar depois para atribuir o PC
                    result = Resultado(Comando.BLT, posi, valor)
                    resultados.append(result)
                    return True
               else:
                   valor = None
               result = Resultado(Comando.BLT, posi, valor)
            
            elif instrucao.inst == Comando.BGT:   
               posi = None
               if valor_reg[rs] > valor_reg[rt]:
                    valor = imm #Verificar depois para atribuir o PC
                    result = Resultado(Comando.BGT,posi, valor)
                    resultados.append(result)
                    return True
               else:
                   valor = None
               result = Resultado(Comando.BGT,posi, valor)
            
            elif instrucao.inst == Comando.BEQ:  
               posi = None
               if valor_reg[rs] == valor_reg[rt]:
                    valor = imm #Verificar depois para atribuir o PC
                    result = Resultado(Comando.BEQ,posi,valor)
                    resultados.append(result)
                    return True
               else:
                   valor = None
               result = Resultado(Comando.BEQ,posi,valor)
            
            elif instrucao.inst == Comando.J:  
               posi = None
               valor = imm
               result = Resultado(Comando.J, posi, valor)
               return True
            
            elif instrucao.inst == Comando.LW:  
               posi = rd    
               valor = memoria[imm + rs]
               result = Resultado(Comando.LW,posi, valor)
            
            elif instrucao.inst == Comando.SW:  
               posi = imm + valor_reg[rt]
               valor = valor_reg[rs]
               result = Resultado(Comando.SW,posi, valor)
            
            elif instrucao.inst == Comando.MOV:  
               posi = rd    
               valor = rs
               result = Resultado(Comando.MOV,posi, valor)
            
            elif instrucao.inst == Comando.MOVI:  
               posi = rd    
               valor = imm
               result = Resultado(Comando.MOVI,posi, valor)
           
            resultados.append(result)
    return False

def escreve_reg(pipeline: list[Instrucao], valor_reg: list[int], memoria: list[int], resultados: list[Resultado], pc: int) -> int:
    if pipeline[4] is not None:
        if resultados[0] is not None:
            if resultados[0].inst == Comando.SW:
                posi = resultados[0].posi
                memoria[posi] = resultados[0].valor
                resultados.pop(0)
            else: 
                posi = resultados[0].posi
                valor_reg[posi] = resultados[0].valor
                resultados.pop(0)
    return pc

def executa_jump(resultados: list[Resultado], pipeline: list[Instrucao], lista_inst:list[Instrucao], pc: int) -> int:
    pc = resultados[-1].valor
    pipeline[0] = None
    pipeline[1] = None  
    pipeline[3] = None 
    resultados.clear() 
    return pc


def finaliza(pipeline, lista_inst, pc) -> bool:
    comando = True
    verifica_noop = True 
    for i in pipeline:
        if i != None:
            verifica_noop = False
    if verifica_noop and pc>= len(lista_inst):
        comando = False
    return comando

def executa_operacoes(operacao:io.TextIOWrapper, nome_reg:list[str], valor_reg:list[int], memoria:list[int]):

    linhas = operacao.readlines()
    lista_inst: list[Instrucao] = lista_instrucoes(linhas)
    pipeline: list[Instrucao] = [None,None,None,None,None] #pipeline com as operacoes 
    tam = len(pipeline) - 1
    pc = 0 #inicia o pc 
    resultados = []
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
            novo_pc = busca_inst(pipeline, lista_inst, pc)
            pc = novo_pc

       

        
        #Verifica se o jump foi tomado e armazena os resultados das instruções em resultados 
        jump = executa_inst(pipeline, valor_reg, memoria, resultados)
        print(jump)
     

        #Print
        saida = ''
        for i in pipeline:
            if i is not None:
                saida += f"|{calcula_caracteres(i.text)}|" 
            else:
                saida += f"|{calcula_caracteres("NOOP")}|" 

        print(str_pipeline)
        print(saida)
        print("Registradores: ")
        for nome in nome_reg:
            print(f"{nome:<5}", end=" ")
        print()
        for valor in valor_reg:
            print(f"{str(valor):<5}", end=" ")
        print()

        print(f"Memória: {memoria}")
        print(f"PC:{pc} ")
        print(f"rd:  rs:  rt:  imm:  opcode: text: ")  
        print()
        print()

        if len(resultados) > 0: 
            pc = escreve_reg(pipeline, valor_reg, memoria, resultados, pc)

        if jump:
            novo_pc = executa_jump(resultados, pipeline, lista_inst, pc) 
            pc = novo_pc
            print(resultados)

        comando = finaliza(pipeline, lista_inst, pc)
     
       
def main() -> None:
    if len(sys.argv) == 3:
        nomeArq = sys.argv[1] 
        tam_memoria = int(sys.argv[2])
        operacao = open(nomeArq, 'r')
        nome_reg, valor_reg = inicializa_registradores() #registradores = 0
        memoria = [] #VERIFICAR COMO QUE INICIALIZA A MEMORIA 
        for i in range(tam_memoria):
            memoria.append(0)
        
        print(memoria)

        executa_operacoes(operacao, nome_reg, valor_reg, memoria)
    
    else:
        print("Faltou comandos na linha de parâmetro, deve conter: Script, Arquivo_Operações e um inteiro indicando o tamanho da memória")



if __name__ == "__main__":
    main()