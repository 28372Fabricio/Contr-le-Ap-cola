import csv

# Arquivos CSV para armazenar os dados
data_apiarios = "apiarios.csv"
data_colheitas = "colheitas.csv"

def inicializar_arquivos():
    """Cria os arquivos CSV se ainda não existirem."""
    for arquivo, cabecalho in [
        (data_apiarios, ["Nome", "Localizacao", "Num_Colmeias"]),
        (data_colheitas, ["Apiario", "Data", "Quantidade", "Qualidade"])
    ]:
        file = open(arquivo, "a", newline="")
        if file.tell() == 0 :
            writer = csv.writer(file)
            writer.writerow(cabecalho)
        file.close()

def cadastrar_apiario():
    """Registra um novo apiário."""
    apiario = {}
    apiario["nome"] = input("Nome do apiário: ")
    apiario["localizacao"] = input("Localização: ")
    apiario["num_colmeias"] = input("Número de colmeias: ")
    with open(data_apiarios, "a", newline="") as file:
        csv.writer(file).writerow(apiario.values())
    print("Apiário cadastrado com sucesso!")

def registrar_colheita():
    print

def consultar_producao():
    print

def listar_apiarios():
    print

def editar_apiario():
    print

def excluir_apiario():
    print

def menu():
    """Exibe o menu principal do sistema."""
    while True:
        print("[1] Cadastrar Apiário")
        print("[2] Registrar Colheita")
        print("[3] Consultar Produção")
        print("[4] Listar Apiários")
        print("[5] Editar Apiário")
        print("[6] Excluir Apiário")
        print("[7] Sair")
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
            print("Opção inválida, tente novamente!")

if __name__ == "__main__":
    inicializar_arquivos()
    menu()