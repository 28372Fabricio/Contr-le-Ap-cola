import csv

# Definição dos arquivos CSV
data_apiarios = "apiarios.csv"
data_colheitas = "colheitas.csv"

# Dicionário para armazenar os apiários e suas colheitas temporariamente
apiarios = {}

# Função para inicializar os arquivos CSV
def inicializar_arquivos():
    with open(data_apiarios, "a", newline="") as file:
        if file.tell() == 0:  # Verifica se o arquivo está vazio
            writer = csv.writer(file)
            writer.writerow(["Nome", "Localizacao", "Num_Colmeias"])
    
    with open(data_colheitas, "a", newline="") as file:
        if file.tell() == 0:  # Verifica se o arquivo está vazio
            writer = csv.writer(file)
            writer.writerow(["Apiario", "Data", "Quantidade", "Qualidade"])

# Função para cadastrar um novo apiário
def cadastrar_apiario():
    nome = input("Nome do apiário: ")
    localizacao = input("Localização: ")
    num_colmeias = input("Número de colmeias: ")
    
    # Adiciona o apiário ao dicionário
    apiarios[nome] = {"localizacao": localizacao, "num_colmeias": num_colmeias, "colheitas": []}
    
    # Salva o apiário no arquivo CSV
    with open(data_apiarios, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nome, localizacao, num_colmeias])
    
    print("Apiário cadastrado!")

# Função para listar todos os apiários cadastrados
def listar_apiarios():
    if not apiarios:
        print("Nenhum apiário cadastrado.")
    else:
        for nome, dados in apiarios.items():
            print(f"Nome: {nome}, Localização: {dados['localizacao']}, Colmeias: {dados['num_colmeias']}")

# Função para editar um apiário existente
def editar_apiario():
    nome_editar = input("Nome do apiário que deseja editar: ")
    if nome_editar not in apiarios:
        print("Apiário não encontrado!")
        return
    
    # Edita os dados do apiário
    nova_localizacao = input("Nova localização: ")
    novo_num_colmeias = input("Novo número de colmeias: ")
    
    apiarios[nome_editar]["localizacao"] = nova_localizacao
    apiarios[nome_editar]["num_colmeias"] = novo_num_colmeias
    
    # Atualiza o arquivo CSV
    with open(data_apiarios, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Localizacao", "Num_Colmeias"])  # Reescreve o cabeçalho
        for nome, dados in apiarios.items():
            writer.writerow([nome, dados["localizacao"], dados["num_colmeias"]])
    
    print("Apiário editado com sucesso!")

# Função para excluir um apiário
def excluir_apiario():
    nome_excluir = input("Nome do apiário que deseja excluir: ")
    if nome_excluir not in apiarios:
        print("Apiário não encontrado!")
        return
    
    # Remove o apiário do dicionário
    del apiarios[nome_excluir]
    
    # Atualiza o arquivo CSV
    with open(data_apiarios, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Localizacao", "Num_Colmeias"])  # Reescreve o cabeçalho
        for nome, dados in apiarios.items():
            writer.writerow([nome, dados["localizacao"], dados["num_colmeias"]])
    
    print("Apiário excluído com sucesso!")

# Função para registrar uma nova colheita
def registrar_colheita():
    nome_apiario = input("Nome do apiário: ")
    if nome_apiario not in apiarios:
        print("Apiário não encontrado!")
        return
    
    data = input("Data da colheita: ")
    quantidade = input("Quantidade coletada (kg): ")
    qualidade = input("Qualidade do mel (Boa/Regular/Ruim): ")
    
    # Adiciona a colheita ao apiário correspondente
    colheita = [data, quantidade, qualidade]
    apiarios[nome_apiario]["colheitas"].append(colheita)
    
    # Salva a colheita no arquivo CSV
    with open(data_colheitas, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nome_apiario, data, quantidade, qualidade])
    
    print("Colheita registrada!")

# Função para consultar a produção de um apiário
def consultar_producao():
    nome_apiario = input("Nome do apiário: ")
    if nome_apiario not in apiarios:
        print("Apiário não encontrado!")
        return
    
    colheitas = apiarios[nome_apiario]["colheitas"]
    if not colheitas:
        print("Nenhuma colheita registrada para este apiário.")
    else:
        for colheita in colheitas:
            print(f"Data: {colheita[0]}, Quantidade: {colheita[1]}kg, Qualidade: {colheita[2]}")

# Função do menu interativo
def menu():
    while True:
        print("\n1. Cadastrar Apiário")
        print("2. Registrar Colheita")
        print("3. Consultar Produção")
        print("4. Listar Apiários")
        print("5. Editar Apiário")
        print("6. Excluir Apiário")
        print("7. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_apiario()
        elif opcao == "2":
            registrar_colheita()
        elif opcao == "3":
            consultar_producao()
        elif opcao == "4":
            listar_apiarios()
        elif opcao == "5":
            editar_apiario()
        elif opcao == "6":
            excluir_apiario()
        elif opcao == "7":
            break
        else:
            print("Opção inválida. Tente novamente.")

# Função para iniciar o sistema
def iniciar_sistema():
    inicializar_arquivos()
    menu()

# Inicia o sistema
iniciar_sistema()
