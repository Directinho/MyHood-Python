import subprocess
import sys
import os


grupo = ["Gabriela do Rozario", "Henrique Luiz", "João Vitor", "Lucas Salvador", "Milenna de Moraes"]

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
    print("MyBairro \n\n1- Entrar como Cidadao \n2- Entrar como Administrador \n3- Ver Grupo\n4- Sair do Sistema\n")
    opcao = input("Insira uma opção: ")
    if opcao == "1":  
        opcao1()
    elif opcao == "2":
        opcao2()
    elif opcao == "3":
        limpar()
        integrantes()
        

    elif opcao == "4":
        limpar()
        print("Fechando programa...")

    else:
        print(erro)



if __name__ == '__main__':
    main()
