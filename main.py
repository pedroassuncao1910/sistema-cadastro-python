print("=== Sistema de Cadastro ===")

usuarios = []

while True:
    print("\n1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        usuarios.append({"nome": nome, "idade": idade})
        print("Usuário cadastrado com sucesso!")

    elif opcao == "2":
        print("\nUsuários cadastrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']} | Idade: {usuario['idade']}")

    elif opcao == "3":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
