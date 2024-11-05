import os

restaurantes = [{'nome':'sushi aki', 'categoria': 'japonesa', 'ativo':False}, 
                {'nome':'só suco', 'categoria': 'Brasileria', 'ativo':True}]

def exibir_nome_do_programa():
    print('🅢🅐🅑🅞🅡 🅔🅧🅟🅡🅔🅢🅢\n')

def exibir_opcao():
    print('1. Cadastrar')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando app')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção invalida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante:')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    
    voltar_ao_menu_principal()
   
def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')

    print(f'{'Nome do restaurante'.ljust(19)} | {'Categoria'.ljust(17)} | Status')

    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(17)} | {categoria.ljust(17)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = (
            f'O restaurante {nome_restaurante} foi ativado com sucesso'
            if restaurante['ativo'] 
            else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            )
            print(mensagem)
            voltar_ao_menu_principal()
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
        voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcao()
    escolher_opcao()
    

if __name__ == '__main__':
    main() 



"""numero = int(input('Insira o numero:'))

if numero % 2 == 0:
    print(f'{numero} é par')
else:
    print(f'{numero} é impar')

idade = int(input('Escreva sua idade:'))

if idade <= 12:
    print(f'{idade} anos ainda é criança')
elif 13 <= idade <= 18:
    print(f'{idade} anos ainda é adolescente')
else:  
    print(f'{idade} anos ja é adulto')

nome = input('Nome de usuario :')
senha = int(input('Senha: '))

if nome == 'Heitor' and senha == 100679:
    print('Login realizado com sucesso')
else:
    print('dados incorretos')"""



    






