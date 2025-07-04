import sys
import io
from enum  import Enum, auto

class Instrucao(Enum):
    MOVI = auto()
    ADD = auto()
    ADDI = auto()
    #colocar outras coisas dps



def executa_operacoes(operacao:io.TextIOWrapper):
    linhas = operacao.readlines()
    for op in linhas:
        linha = op.split(" ")
        instrucao = linha[0].upper()
        if instrucao == Instrucao.MOVI.name:
            executa_muvi()



    

   


def main() -> None:
    if len(sys.argv) > 2:
        nomeArq = sys.argv[1] 
        operacao = open(nomeArq, 'r')
        executa_operacoes(operacao)
    
    else:
        print("Faltou comandos na linha de parâmetro, deve conter: Script e Arquivo_Operações")



if __name__ == "__main__":
    main()