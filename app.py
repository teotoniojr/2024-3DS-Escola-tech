import os

alunos = [{'nome':'João José', 'matéria':'front-end', 'ativo':True},
          {'nome': 'Maria Ana', 'matéria':'back-and', 'ativo':False},
          {'nome': 'José Carlos', 'matéria':'Ux-design', 'ativo':True}]

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

    def exibir_subtitulo(texto):
        os.system('clear')
        print(texto)
        print('')
    
    def retorna_menu():
        input(' Digite uma tecla para voltar ao menu principal ')
        main()

    def cadastra_aluno():
        exibir_subtitulo('Cadastrar aluno')
        nome_aluno = input(' Digite o nome do aluno que deseja cadastrar: ')
        alunos.append(nome_aluno)
        print(f' O aluno {nome_aluno} foi cadastrado com sucesso\n')
        retorna_menu()
        
    
    def listar_alunos():
        exibir_subtitulo('Lista de alunos cadastrados')
        for aluno in alunos:
            nome_aluno = aluno['nome']
            materia_aluno = aluno['matéria']
            ativo = aluno['ativo']
            print(f' - {nome_aluno} | {materia_aluno} | {ativo}')
        retorna_menu()
    
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
            cadastra_aluno()
        elif opcao_escolhida == 2:
            listar_alunos()
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