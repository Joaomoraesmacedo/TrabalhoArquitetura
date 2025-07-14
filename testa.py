import sys
import io
from enum import Enum, auto
from dataclasses import dataclass
from typing import Optional

class Comando(Enum):
    MOVI = auto()
    ADD = auto()
    ADDI = auto()

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
    reg: int
    valor: int

def inicializa_registradores() -> list:
    lista_valores = []
    lista_registradores = []
    for i in range(32):
        lista_registradores.append(f'R{i}')
        lista_valores.append(0)
    return lista_registradores, lista_valores  

def busca_inst(pipeline: list, linhas: list[str], pc: int) -> int:
    if pc < len(linhas):
        pipeline[0] = linhas[pc].strip()
        pc += 1
    else:
        pipeline[0] = None
    return pc

def decodifica(pipeline: list, linhas: list[str]):
    if pipeline[1] is None and pipeline[0] is not None:
        text = pipeline[0]
        linha = text.split(" ")
        instrucao = linha[0].upper()
        resto = linha[1]

        if instrucao == Comando.MOVI.name:
            reg, imm_str = resto.split(",")
            rd = int(reg[1:])
            instr = Instrucao(Comando.MOVI, rd, None, None, int(imm_str), text)
        elif instrucao == Comando.ADD.name:
            regs = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            rt = int(regs[2][1:])
            instr = Instrucao(Comando.ADD, rd, rs, rt, None, text)
        elif instrucao == Comando.ADDI.name:
            regs = resto.split(",")
            rd = int(regs[0][1:])
            rs = int(regs[1][1:])
            instr = Instrucao(Comando.ADDI, rd, rs, None, int(regs[2]), text)
        else:
            print("Instrução inválida:", text)
            instr = None

        pipeline[1] = instr
        pipeline[0] = None

def verica_hazard(pipeline: list) -> int:
    if pipeline[1] is not None:
        for i in range(3, 1, -1):
            if pipeline[i] is not None:
                if pipeline[1].rs == pipeline[i].rd or pipeline[1].rt == pipeline[i].rd:
                    return pipeline[i].rd
    return None

def executa_inst(pipeline: list, valor_reg: list[int], resultados: list[Resultado]) -> None:
    if isinstance(pipeline[2], Instrucao):
        instrucao: Instrucao = pipeline[2]
        rd = instrucao.rd
        rs = instrucao.rs
        rt = instrucao.rt
        imm = instrucao.imm

        if instrucao.inst == Comando.MOVI:
            valor = imm
        elif instrucao.inst == Comando.ADD:
            valor = valor_reg[rs] + valor_reg[rt]
        elif instrucao.inst == Comando.ADDI:
            valor = valor_reg[rs] + imm
        else:
            valor = 0

        resultados.append(Resultado(rd, valor))

def escreve_reg(pipeline: list, valor_reg: list[int], resultados: list[Resultado]) -> None:
    if pipeline[4] is not None and resultados:
        posi = resultados[0].reg
        valor_reg[posi] = resultados[0].valor
        resultados.pop(0)

def finaliza(pipeline: list, linhas: list[str], pc: int) -> bool:
    comando = True
    verifica_noop = True 
    for i in pipeline:
        if i != None:
            verifica_noop = False
    if verifica_noop and pc>= len(linhas):
        comando = False
    return comando


def executa_operacoes(operacao: io.TextIOWrapper, nome_reg: list[str], valor_reg: list[int], memoria: list[int]):
    linhas = operacao.readlines()
    pipeline: list = [None] * 5
    resultados = []
    pc = 0
    comando = True
    tam = len(pipeline) - 1

    str_pipeline = "|-----Busca-----||---Decodifica--||---Executa-----||---Memoria-----||----Regist-----|"

    while comando:
        hazard = verica_hazard(pipeline)
        if hazard is not None:
            for i in range(4, 2, -1):
                pipeline[i] = pipeline[i - 1]
            pipeline[2] = None
        else:
            for i in range(tam, 0, -1):
                pipeline[i] = pipeline[i - 1]
            pc = busca_inst(pipeline, linhas, pc)

        decodifica(pipeline, linhas)
        executa_inst(pipeline, valor_reg, resultados)
        # Impressão do pipeline
        saida = "  "
        for i in pipeline:
            if isinstance(i, Instrucao):
                saida += i.text + "  "
            elif isinstance(i, str):
                saida += i + "  "
            else:
                saida += "NOOP   "

        print(str_pipeline)
        print(saida)
        print("  " + "  ".join(nome_reg))
        print(valor_reg)
        print(pc)

        escreve_reg(pipeline, valor_reg, resultados)
        comando = finaliza(pipeline, linhas, pc)

        #

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

            
        #Para saber o que esta na lista execute no terminal: python3 simulador.py add_mov.txt
        '''
        

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

def main() -> None:
    if len(sys.argv) == 3:
        nomeArq = sys.argv[1]
        tam_memoria = int(sys.argv[2])
        operacao = open(nomeArq, 'r')
        nome_reg, valor_reg = inicializa_registradores()
        memoria = [0] * tam_memoria

        executa_operacoes(operacao, nome_reg, valor_reg, memoria)
    else:
        print("Faltou comandos na linha de parâmetro, deve conter: Script, Arquivo_Operações e um inteiro indicando o tamanho da memória")

if __name__ == "__main__":
    main()
