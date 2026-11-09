import json
from main import limpar
from cidadao import consultarPedido ,voltarMenu


def definirStatus():
    limpar()
    print("Definir Status de Pedidos\n")
    print("Digite 'voltar' para cancelar e voltar ao menu do administrador\n")

    try:
        with open("pedidos.json", "r", encoding="utf-8") as f:
            pedidos = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        pedidos = []

    if not pedidos:
        print("Não há pedidos cadastrados ainda.")
        input("\nAperte Enter para voltar ao menu do administrador...")
        admin()
        return

    def ler_campo(mensagem, tipo=str):
        while True:
            valor = input(mensagem).strip()
            if valor.lower() == "voltar":
                return "voltar"
            if tipo == int:
                try:
                    return int(valor)
                except ValueError:
                    print("Entrada inválida. Digite apenas números.")
                    continue
            return valor

    pedido_id = ler_campo("Digite o ID do pedido: ", tipo=int)

    if pedido_id == "voltar":
        admin()
        return

    if not (1 <= pedido_id <= len(pedidos)):
        print(f"\nID {pedido_id} não encontrado. Os IDs válidos vão de 1 a {len(pedidos)}.")
        input("Aperte Enter para tentar novamente...")
        definirStatus()
        return

    pedido = pedidos[pedido_id - 1]
    print(f"\nPedido encontrado:")
    print(f"Nome: {pedido.get('nome')}")
    print(f"Pedido: {pedido.get('pedido')}")
    print(f"Status atual: {pedido.get('status')}\n")

    print("Escolha o novo status:")
    print("1 - Em andamento")
    print("2 - Pendente")
    print("3 - Concluído")
    print("0 - Cancelar / Voltar\n")

    opcaoStatus = ler_campo("Digite o número do status: ", tipo=int)

    if opcaoStatus == "voltar" or opcaoStatus == 0:
        admin()
        return

    if opcaoStatus == 1:
        novoStatus = "Em andamento"
    elif opcaoStatus == 2:
        novoStatus = "Pendente"
    elif opcaoStatus == 3:
        novoStatus = "Concluído"
    else:
        print("Opção inválida.")
        input("Aperte Enter para tentar novamente...")
        definirStatus()
        return

    pedidos[pedido_id - 1]["status"] = novoStatus

    with open("pedidos.json", "w", encoding="utf-8") as f:
        json.dump(pedidos, f, indent=4, ensure_ascii=False)

    print(f"\nStatus do pedido {pedido_id} atualizado com sucesso para '{novoStatus}'.")
    input("Aperte Enter para voltar ao menu do administrador...")
    admin()


def admin():
    limpar()
    print("Bem-vindo ao Sistema do Administrador")
    print(
        "\nO que deseja fazer?\n1- Editar Pedidos\n2- Definir Status de Pedidos\n3- Checar Lista de Pedidos\n4- Voltar para o menu principal\n"
    )
    opcao = input("Insira uma opção: ")
    if opcao == "1":
        pass 
    elif opcao == "2":
        definirStatus()
    elif opcao == "3":
        consultarPedido()
    elif opcao == "4":
        voltarMenu()
    else:
        print("Opção desconhecida")
        input("Aperte Enter para tentar novamente...")
        admin()


if __name__ == "__main__":
    admin()