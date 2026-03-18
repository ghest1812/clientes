# Função para cadastrar um novo cliente
def cadastrar_cliente(clientes):
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")

    cliente = {
        'nome': nome,
        'email': email,
        'telefone': telefone
    }
    
    clientes.append(cliente)
    print("\nCliente cadastrado com sucesso!")

# Função para listar todos os clientes cadastrados
def listar_clientes(clientes):
    if len(clientes) == 0:
        print("\nNenhum cliente cadastrado!")
    else:
        print("\nLista de Clientes Cadastrados:")
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")

# Função para buscar um cliente pelo nome
def buscar_cliente(clientes):
    nome_busca = input("Digite o nome do cliente para buscar: ")
    encontrados = [cliente for cliente in clientes if nome_busca.lower() in cliente['nome'].lower()]
    
    if encontrados:
        print("\nClientes encontrados:")
        for cliente in encontrados:
            print(f"Nome: {cliente['nome']}, Email: {cliente['email']}, Telefone: {cliente['telefone']}")
    else:
        print("\nNenhum cliente encontrado com esse nome.")

# Função para exibir o menu
def menu():
    clientes = []
    
    while True:
        print("\n--- Menu de Cadastro de Clientes ---")
        print("1. Cadastrar Cliente")
        print("2. Listar Clientes")
        print("3. Buscar Cliente")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_cliente(clientes)
        elif opcao == '2':
            listar_clientes(clientes)
        elif opcao == '3':
            buscar_cliente(clientes)
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama o menu para o programa começar
menu()