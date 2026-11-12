import subprocess
import sys
import os


grupo = ("Gabriela do Rozario", "Henrique Luiz", "João Vitor", "Lucas Salvador", "Milenna de Moraes")
erro = "Opção desconhecida"


def opcao1():

    try:

        subprocess.run([sys.executable, "cidadao.py"])

    except Exception:

        print("Erro ao abrir")

def opcao2():
    try:
        subprocess.run([sys.executable, "admin.py"])
    except Exception:
        print("Erro ao abrir")
def integrantes():
    limpar()
    print("M2G team\n\n")
    for integrante in grupo:
        print(integrante + "\n")
    continuar()
def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')
def continuar():
    input("Aperte qualquer tecla para voltar")
    limpar()
    main() 
def main():
    limpar()
    print("\t--MyHood--\nSeu bairro na palma da sua mão \n\n1- Entrar como Cidadao \n2- Entrar como Administrador \n3- Ver Grupo\n4- Sair do Sistema\n")
    opcao = input("Insira uma opção: ")

    match opcao:
        case "1":
            opcao1()
        case "2":
            opcao2()
        case "3":
            integrantes()
        case "4":
            print("Saindo do sistema...")
            sys.exit(0)
        case _:
            print(erro)
            input("Aperte Enter para tentar novamente...")
            main()



if __name__ == '__main__':
    main()
