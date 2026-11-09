import json
import os
import subprocess
import sys
import urllib.request
from main import limpar


def cadastrarPedido():
    limpar()
    print("Cadastro de pedido\n\n")
    print(
        "Digite 'pular' em qualquer campo para pular o campo indicado\nDigite 'voltar' para cancelar e voltar ao menu do cidadão\n\n"
    )

    def ler_campo(mensagem, tipo=str):
        while True:
            valor = input(mensagem).strip()
            if valor.lower() == "voltar":
                return "voltar"
            if valor.lower() == "pular":
                return "Nao informado"

            if tipo == int:
                try:
                    return int(valor)
                except ValueError:
                    print("Entrada inválida. Digite apenas números.")
                    continue
            return valor

    nome = ler_campo("Digite seu nome: ")
    if nome == "voltar":
        cidadao()
        return

    cpf = ler_campo("Digite seu CPF: ")
    if cpf == "voltar":
        cidadao()
        return

    nivel = ler_campo("Digite seu nível de prioridade (1-5): ", tipo=int)
    if nivel == "voltar":
        cidadao()
        return

    pedido = ler_campo("Digite o pedido: ")
    if pedido == "voltar":
        cidadao()
        return

    cep_input = ler_campo("Digite o CEP da cidade: ")
    if cep_input == "voltar":
        cidadao()
        return

    if cep_input == "Nao informado":
        cidade_formatada = "Nao informado"
    else:
        clean_cep = cep_input.replace("-", "").replace(".", "").replace(" ", "")
        try:
            url = f"https://viacep.com.br/ws/{clean_cep}/json/"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode("utf-8"))

                if "erro" in data:
                    print("Aviso: CEP não encontrado na base de dados.")
                    cidade_formatada = f"{clean_cep} | CEP Não Encontrado"
                else:
                    logradouro = data.get("logradouro", "")
                    bairro = data.get("bairro", "")
                    localidade = data.get("localidade", "")
                    uf = data.get("uf", "")

                    cidade_formatada = " | ".join(
                        filter(None, [logradouro, bairro, localidade, uf])
                    )
        except Exception:
            print("Erro ao conectar à API do ViaCEP.")
            cidade_formatada = f"{clean_cep} | Erro na consulta"

    novo_pedido = {
        "nome": nome,
        "cpf": cpf,
        "nivel": nivel,
        "pedido": pedido,
        "cep": (
            clean_cep
            if cep_input != "Nao informado" and "clean_cep" in locals()
            else "Nao informado"
        ),
        "cidade": cidade_formatada,
        "status": "Em análise",
    }

    pedidos_existentes = []
    if os.path.exists("pedidos.json") and os.path.getsize("pedidos.json") > 0:
        try:
            with open("pedidos.json", "r", encoding="utf-8") as f:
                pedidos_existentes = json.load(f)
                if not isinstance(pedidos_existentes, list):
                    pedidos_existentes = []
        except Exception:
            pedidos_existentes = []

    pedidos_existentes.append(novo_pedido)

    with open("pedidos.json", "w", encoding="utf-8") as f:
        json.dump(pedidos_existentes, f, ensure_ascii=False, indent=4)

    print("\nPedido cadastrado com sucesso!")
    input("\nAperte qualquer tecla para voltar ao menu do cidadão...")
    cidadao()
def consultarPedido():
    limpar()
    print("Consulta de pedidos\n")

    if not os.path.exists("pedidos.json") or os.path.getsize("pedidos.json") == 0:
        print("Nenhum pedido foi cadastrado ainda.")
    else:
        try:
            with open("pedidos.json", "r", encoding="utf-8") as f:
                pedidos_existentes = json.load(f)

            if not isinstance(pedidos_existentes, list) or len(pedidos_existentes) == 0:
                print("Nenhum pedido foi cadastrado ainda.")
            else:
                for i, pedido in enumerate(pedidos_existentes, start=1):
                    print(f"Pedido {i}:")
                    print(f"Nome: {pedido.get('nome', 'N/A')}")
                    print(f"CPF: {pedido.get('cpf', 'N/A')}")
                    print(f"Nível de prioridade: {pedido.get('nivel', 'N/A')}")
                    print(f"Pedido: {pedido.get('pedido', 'N/A')}")
                    print(f"CEP: {pedido.get('cep', 'N/A')}")
                    print(f"Cidade: {pedido.get('cidade', 'N/A')}\n")
                    print(f"Status: {pedido.get('status', 'N/A')}\n")
        except Exception:
            print("Nenhum pedido foi cadastrado ainda.")

    input("\nAperte qualquer tecla para voltar ao menu...")
    cidadao()

    input("\nAperte qualquer tecla para voltar ao menu...")
    cidadao()

def voltarMenu():
    try:
        subprocess.run([sys.executable, "main.py"])
    except Exception:
        print("Erro ao abrir o menu principal")


def cidadao():
    limpar()
    print("Bem-vindo ao Sistema de Cidadão")
    print(
        "\nO que deseja fazer?\n1- Cadastrar pedido\n2- Consultar Pedido\n3- Voltar para o menu principal\n"
    )
    opcao = input("Insira uma opção: ")
    if opcao == "1":
        cadastrarPedido()
    elif opcao == "2":
        consultarPedido()
    elif opcao == "3":
        voltarMenu()
    else:
        print("Opção desconhecida")
        input("Aperte Enter para tentar novamente...")
        cidadao()


if __name__ == "__main__":
    cidadao()
