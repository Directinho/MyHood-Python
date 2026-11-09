import json
from main import limpar
from cidadao import consultarPedido, voltarMenu


def ler_campo(mensagem, tipo=str, valor_atual=None):
    while True:
        valor = input(mensagem).strip()

        if valor.lower() == "voltar":
            return "voltar"

        if valor.lower() == "pular" or valor == "":
            return valor_atual

        if tipo == int:
            try:
                return int(valor)
            except ValueError:
                print("Entrada inválida. Digite apenas números.")
                continue

        return valor


def editarPedido():
    limpar()
    print("Editar Pedido\n")
    print("Digite 'voltar' a qualquer momento para cancelar.\n")

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

    pedido_id = ler_campo("Digite o ID do pedido: ", tipo=int)

    if pedido_id == "voltar":
        admin()
        return

    if not (1 <= pedido_id <= len(pedidos)):
        print(f"\nID {pedido_id} não encontrado. Os IDs válidos vão de 1 a {len(pedidos)}.")
        input("Aperte Enter para tentar novamente...")
        editarPedido()
        return

    pedido = pedidos[pedido_id - 1]

    limpar()
    print(f"Editando Pedido de id: {pedido_id} ===\n")
    print(f"Nome atual: {pedido.get('nome')}")
    print(f"CPF atual: {pedido.get('cpf')}")
    print(f"Nível atual: {pedido.get('nivel')}")
    print(f"Pedido atual: {pedido.get('pedido')}")
    print(f"CEP atual: {pedido.get('cep')}")
    print(f"Cidade atual: {pedido.get('cidade')}")
    print(f"Status atual: {pedido.get('status')}")
    print("\nDigite o novo valor ou 'pular' (ou Enter) para manter o atual.\n")

    nome = ler_campo(f"Novo nome [{pedido.get('nome')}]: ", valor_atual=pedido.get("nome"))
    if nome == "voltar":
        admin()
        return

    cpf = ler_campo(f"Novo CPF [{pedido.get('cpf')}]: ", valor_atual=pedido.get("cpf"))
    if cpf == "voltar":
        admin()
        return

    nivel = ler_campo(f"Novo nível (1-5) [{pedido.get('nivel')}]: ", tipo=int, valor_atual=pedido.get("nivel"))
    if nivel == "voltar":
        admin()
        return

    pedido_texto = ler_campo(f"Novo pedido [{pedido.get('pedido')}]: ", valor_atual=pedido.get("pedido"))
    if pedido_texto == "voltar":
        admin()
        return

    cep = ler_campo(f"Novo CEP [{pedido.get('cep')}]: ", valor_atual=pedido.get("cep"))
    if cep == "voltar":
        admin()
        return

    cidade = ler_campo(f"Nova cidade [{pedido.get('cidade')}]: ", valor_atual=pedido.get("cidade"))
    if cidade == "voltar":
        admin()
        return

    status = ler_campo(f"Novo status [{pedido.get('status')}]: ", valor_atual=pedido.get("status"))
    if status == "voltar":
        admin()
        return

    pedidos[pedido_id - 1] = {
        "nome": nome,
        "cpf": cpf,
        "nivel": nivel,
        "pedido": pedido_texto,
        "cep": cep,
        "cidade": cidade,
        "status": status
    }

    with open("pedidos.json", "w", encoding="utf-8") as f:
        json.dump(pedidos, f, indent=4, ensure_ascii=False)

    print(f"\nPedido de id: {pedido_id} atualizado com sucesso!")
    input("Aperte Enter para voltar ao menu do administrador...")
    admin()


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
        "\nO que deseja fazer?\n"
        "1- Editar Pedidos\n"
        "2- Definir Status de Pedidos\n"
        "3- Checar Lista de Pedidos\n"
        "4- Voltar para o menu principal\n"
    )
    opcao = input("Insira uma opção: ")

    if opcao == "1":
        editarPedido()
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