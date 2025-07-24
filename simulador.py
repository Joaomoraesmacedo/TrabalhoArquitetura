import sys
import io
from enum  import Enum, auto
from dataclasses import dataclass
from typing import Optional

TOT_REG = 32

class Comando(Enum):
    '''
    Classe que representa os comandos de uma instrução
    '''
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
    '''
    Representa os elementos de uma instrução , sendo eles, inst: O comando a ser executado, 
    rd: Registrador de destino, rs: Primeiro registrador de origem, rt : Segundo registrador de origem,
    imm: Valor imediato, text: Representação textual inteira da instrução

    '''
    inst: Comando
    rd: Optional[int]
    rs: Optional[int]
    rt: Optional[int]
    imm: Optional[int]
    text: str

@dataclass
class Resultado:
    '''
    Representa o resultado de uma instrução contendo o comando executado, a posição a ser alterada e o valor gerado
    '''
    inst: Comando
    posi: Optional[int] 
    valor: Optional[int] 

def inicializa_registradores() -> list:
    '''
    Inicializa os registradores em uma lista de R0 até R31 e os seus seus valores em outra lista inicialmente
    com todos os elementos igual a 0
    '''

    lista_valores = []
    lista_registradores = []
    for i in range(TOT_REG):
        lista_registradores.append(f'R{i}')
        lista_valores.append(0)
    return lista_registradores, lista_valores  

def lista_instrucoes(linhas:list[str]) -> list[Instrucao]:
    '''
    Retorna uma lista do tipo Instrucao com todas as instruções contidas no arquivo 
    que está sendo executado
    '''
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
            executa = Instrucao(Comando.ADD, rd, rs, rt, imm, text)
           
        elif instrucao == Comando.ADDI.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = None
            imm = int(regs[2])
            executa = Instrucao(Comando.ADDI, rd, rs, rt, imm, text)
            
        elif instrucao == Comando.SUB.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            executa = Instrucao(Comando.SUB, rd, rs, rt, imm, text)
        
        elif instrucao == Comando.SUBI.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = None
            imm = int(regs[2])
            executa = Instrucao(Comando.SUBI, rd, rs, rt, imm, text)
        
        elif instrucao == Comando.MUL.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            executa = Instrucao(Comando.MUL, rd, rs, rt, imm, text)
        
        elif instrucao == Comando.DIV.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            executa = Instrucao(Comando.DIV, rd, rs, rt, imm, text)
        
        elif instrucao == Comando.MOD.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            imm = None
            executa = Instrucao(Comando.MOD, rd, rs, rt, imm, text)
        
        elif instrucao == Comando.BLT.name:
            regs  = resto.split(",")
            rd = None
            rs = int(regs[0][1:])
            rt = int(regs[1][1:])
            imm = int(regs[2])
            executa = Instrucao(Comando.BLT, rd, rs, rt, imm, text)
        
        elif instrucao == Comando.BGT.name:
            regs  = resto.split(",")
            rd = None
            rs = int(regs[0][1:])
            rt = int(regs[1][1:])
            imm = int(regs[2])
            executa = Instrucao(Comando.BGT, rd, rs, rt, imm, text)
        
        elif instrucao == Comando.BEQ.name:
            regs  = resto.split(",")
            rd = None
            rs = int(regs[0][1:])
            rt = int(regs[1][1:])
            imm = int(regs[2])
            executa = Instrucao(Comando.BEQ, rd, rs, rt, imm, text)
        
        elif instrucao == Comando.J.name:
            rd = None
            rs = None
            rt = None
            imm = linha[2]
            executa = Instrucao(Comando.J, rd, rs, rt, imm, text)
    
        elif instrucao == Comando.LW.name:
            regs = resto.split(",")
            rd =  int(regs[0][1:])
            valor = regs[1].split("(")
            imm = int(valor[0])
            rs = int(valor[1].strip()[1:].replace(")", ""))
            rt = None
            executa = Instrucao(Comando.LW, rd, rs, rt, imm, text)


        elif instrucao == Comando.SW.name:
            regs = resto.split(",")
            rs =  int(regs[0][1:])
            valor = regs[1].split("(")
            imm = int(valor[0])
            rt = int(valor[1].strip()[1:].replace(")", ""))
            rd = None
            executa = Instrucao(Comando.SW, rd, rs, rt, imm, text)
        
        elif instrucao == Comando.MOV.name:
            regs  = resto.split(",")
            rd = int(regs[0][1:])
            rs = None
            rt = None
            imm = int(regs[2])
            executa = Instrucao(Comando.MOV, rd, rs, rt, imm, text)

        elif instrucao == Comando.MOVI.name:
            reg, imm_str  = resto.split(",")
            rd = int(reg[1:])
            rs = None
            rt = None
            imm = int(imm_str)
            executa = Instrucao(Comando.MOVI, rd, rs, rt, imm, text)
        
        else:
            print('Esta instrução não existe')
        
        print(f'{n} rd:"{rd}" rs:"{rs}" rt:"{rt}" imm:"{imm}" opcode:"{instrucao.lower()}" text:"{text}"')
        lista.append(executa) 
        n += 1
    return lista

def calcula_caracteres(instrucao: str)-> str:
    '''
    Calcula os espaços em branco necessários para o alinhamento
    da forma correta na Pipeline
    '''
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
    '''
    Identifica se exite uma operação, caso contrário retorna "NOOP" (Sem operação)
    '''
    if 0 <= op < len(lista):
        return lista[op].strip()
    else:
        return "NOOP"

def busca_inst(pipeline: list, lista_inst: list[Instrucao], pc: int) -> int:
    '''
    Realiza a busca da instrução e incrementa o contador de programa em 1,
    sinalizando que se iniciou uma nova Instrução
    '''
    if pc < len(lista_inst):
        pipeline[0] = lista_inst[pc]
        pc +=1 
    else:
        pipeline[0] = None
    return pc

def verica_hazard(pipeline: list[Instrucao]) -> bool:
    """
    Verifica se há hazard de dados entre a instrução em decodificação (pipeline[1])
    e as instruções que ainda estão nas etapas posteriores.
    Retorna True se houver conflito (ou seja, deve inserir bolha).
    """

    dec = pipeline[1]
    if dec is None:
        return False

    for i in range(2, 4): 
        anterior = pipeline[i]
        if anterior is not None and anterior.rd is not None:
            if dec.rs == anterior.rd or dec.rt == anterior.rd:
                return True  # ainda há conflito com uma instrução no pipeline

    return False  # nenhum conflito ele pode avançar

def executa_inst(pipeline: list[Instrucao], valor_reg: list[int],resultados: list[Resultado]) -> bool:
    '''
    Realiza a instrução, executando o comando de acordo com os valores ao registradores correspondentes, 
    criando um resultado do tipo Resultado e o inserindo em uma lista, que será usada na fase de escrita
    '''
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
                result = Resultado(Comando.ADDI,posi, valor)

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
                    valor = imm
                    result = Resultado(Comando.BLT, posi, valor)
                    resultados.append(result)
                    return True
               else:
                   valor = None
               result = Resultado(Comando.BLT, posi, valor)
            
            elif instrucao.inst == Comando.BGT:   
               posi = None
               if valor_reg[rs] > valor_reg[rt]:
                    valor = imm 
                    result = Resultado(Comando.BGT,posi, valor)
                    resultados.append(result)
                    return True
               else:
                   valor = None
               result = Resultado(Comando.BGT,posi, valor)
            
            elif instrucao.inst == Comando.BEQ:  
               posi = None
               if valor_reg[rs] == valor_reg[rt]:
                    valor = imm 
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
               valor = imm + valor_reg[rs]
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
    '''
    Escreve as instruções que passaram por todos os estágios da pipeline
    nos registradores ou na memória, caso o tamanho seja suficiente
    '''
    try:
        if pipeline[4] is not None:
            if resultados[0] is not None:
                if resultados[0].inst == Comando.SW:
                    posi = resultados[0].posi
                    memoria[posi] = resultados[0].valor
                    resultados.pop(0)
                elif resultados[0].inst == Comando.LW:
                    posi = resultados[0].posi
                    valor_reg[posi] = memoria[resultados[0].valor]
                    resultados.pop(0)

                elif (resultados[0].inst == Comando.BEQ) or (resultados[0].inst == Comando.BLT) or (resultados[0].inst == Comando.BGT) or (resultados[0].inst == Comando.J):
                    resultados.pop(0)
                else:
                    posi = resultados[0].posi
                    valor_reg[posi] = resultados[0].valor
                    resultados.pop(0)
    except IndexError as e:
        print("Indique um tamanho maior de memória para executar esse arquivo de operação!")

    return pc

def executa_jump(resultados: list[Resultado], pipeline: list[Instrucao], lista_inst:list[Instrucao], pc: int) -> int:
    '''
    Realiza o Jump, alterando o fluxo do programa e descartando as instruções
    que não serão mais executadas
    '''
    pc = resultados[-1].valor
    pipeline[0] = None
    pipeline[1] = None  
    pipeline[3] = None 
    inst_jump = resultados[-1]
    resultados.clear()
    resultados.append(inst_jump) 
    return pc


def finaliza(pipeline, lista_inst, pc) -> bool:
    '''
    Quando todas as instruções da pipelina forem igual a None, ou seja,
    se encerraram todas as instruções, o código pode finalizar, retornando 
    True, caso contrário (ainda exista op na pipeline), retorna False e o 
    código continua até a próxima verificacão
    '''
    comando = True
    verifica_noop = True 
    for i in pipeline:
        if i != None:
            verifica_noop = False
    if verifica_noop and pc>= len(lista_inst):
        comando = False
    return comando

def executa_operacoes(operacao:io.TextIOWrapper, nome_reg:list[str], valor_reg:list[int], memoria:list[int]):
    '''
    Executa um ciclo completo na pipeline, incluido busca, decodificação, execução, acesso à memoria ,
    registro, controle do fluxo de operações e tratamento de hazards, é a função principal
    '''

    linhas = operacao.readlines()
    lista_inst: list[Instrucao] = lista_instrucoes(linhas)
    pipeline: list[Instrucao] = [None,None,None,None,None] #pipeline com as operacoes 
    tam = len(pipeline) - 1
    pc = 0 #inicia o pc 
    resultados = []
    str_pipeline = "|-----Busca-----||---Decodifica--||---Executa-----||---Memoria-----||----Regist-----|" 
    comando = True
    while comando:
        
        if verica_hazard(pipeline):
            for i in range(4,2,-1):
                pipeline[i] = pipeline[i - 1]
            pipeline[2] = None

        else:
            for i in range(tam, 0, -1):
                pipeline[i] = pipeline[i - 1]

            # Busca a próxima instrução
            pc = busca_inst(pipeline, lista_inst, pc)

        #Verifica se o jump foi tomado e armazena os resultados das instruções em resultados 
        jump = executa_inst(pipeline, valor_reg, resultados)

        #Print
        saida = ''

        for i in pipeline:
            if i is not None:
                saida += f"|{calcula_caracteres(i.text)}|" 
            else:
                saida += f"|{calcula_caracteres('NOOP')}|" 

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
        if pipeline[4] is not None:
            print(f"rd:{pipeline[4].rd}  rs:{pipeline[4].rs}  rt:{pipeline[4].rt}  imm:{pipeline[4].imm}  opcode:{pipeline[4].inst.name.lower()} text:{pipeline[4].text} ")  
        else:
            print(f'rd:"None" rs:"None" rt:"None" imm:"None" opcode:"None" text:"NOOP"')
        if pipeline[2] is not None:
            print(f"rd:{pipeline[2].rd}  rs:{pipeline[2].rs}  rt:{pipeline[2].rt}  imm:{pipeline[2].imm}  opcode:{pipeline[2].inst.name.lower()} text:{pipeline[2].text} ")  
        else:
            print(f'rd:"None" rs:"None" rt:"None" imm:"None" opcode:"None" text:"NOOP"')
        print()
        print()

        pc = escreve_reg(pipeline, valor_reg, memoria, resultados, pc)

        if jump:
            pc = executa_jump(resultados, pipeline, lista_inst, pc) 

        comando = finaliza(pipeline, lista_inst, pc)
     
       
def main() -> None:
    if len(sys.argv) == 3:
        nomeArq = sys.argv[1] 
        tam_memoria = int(sys.argv[2]) #Flag para inicializar a memoria
        operacao = open(nomeArq, 'r')
        nome_reg, valor_reg = inicializa_registradores() 
        memoria = []
        for i in range(tam_memoria):
            memoria.append(0)
        
        executa_operacoes(operacao, nome_reg, valor_reg, memoria) 
    
    else:
        print("Faltou comandos na linha de parâmetro, deve conter: Script, Arquivo_Operações e um inteiro indicando o tamanho da memória")



if __name__ == "__main__":
    main()