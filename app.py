import os

def mostra_titulo():
    print("""

    ░█▀▀▀ █▀▀ █▀▀ █▀▀█ █── █▀▀█ 　 ▀▀█▀▀ █▀▀ █▀▀ █──█ 
    ░█▀▀▀ ▀▀█ █── █──█ █── █▄▄█ 　 ─░█── █▀▀ █── █▀▀█ 
    ░█▄▄▄ ▀▀▀ ▀▀▀ ▀▀▀▀ ▀▀▀ ▀──▀ 　 ─░█── ▀▀▀ ▀▀▀ ▀──▀
        
    """);

def mostra_escolhas():
    print("1. Cadastrar Aluno")
    print("2. Listar Alunos")
    print("3. Ativar matricula")
    print("4. Sair")


def escolhe_opcao():

    def finalizar_programa():
        os.system('clear')
        print('Finalizando o programa\n')
    
    def opcao_invalida():
        print('Esse carácter não é permitido\n')
        input('Aperte qualquer tecla para voltar')
        main()
    
    try:
        opcao_escolhida = int(input("Escolha uma opção:"))

        if opcao_escolhida == 1:
            print('Você escolheu Cadastrar Aluno')
        elif opcao_escolhida == 2:
            print('Você escolheu Listar alunos')
        elif opcao_escolhida == 3:
            print('Você escolheu Ativar matricula')
        elif opcao_escolhida == 4:
            finalizar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    mostra_titulo()
    mostra_escolhas()
    escolhe_opcao()

if __name__ == '__main__':
    main()