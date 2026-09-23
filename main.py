import csv

ARQUIVO = "medicamentos.csv"


def carregar_medicamentos(arquivo):
    """Carrega os medicamentos salvos no arquivo."""
    medicamentos = []

    try:
        with open(arquivo, "r", newline="", encoding="utf-8") as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)

            for linha in leitor:
                medicamento = {
                    "nome": linha["nome"],
                    "categoria": linha["categoria"],
                    "quantidade": int(linha["quantidade"])
                }
                medicamentos.append(medicamento)

    except FileNotFoundError:
        medicamentos = []

    return medicamentos


def salvar_medicamentos(medicamentos, arquivo):
    """Salva todos os medicamentos no arquivo CSV."""
    with open(arquivo, "w", newline="", encoding="utf-8") as arquivo_csv:
        campos = ["nome", "categoria", "quantidade"]
        escritor = csv.DictWriter(arquivo_csv, fieldnames=campos)

        escritor.writeheader()
        escritor.writerows(medicamentos)

    return True


def cadastrar_medicamento(medicamentos):
    """Cadastra um novo medicamento e adiciona à lista."""
    print("\n--- CADASTRO DE MEDICAMENTO ---")

    # Verifica se o nome do medicamento foi preenchido.
    while True:
        nome = input("Nome: ").strip()

        if nome:
            break

        print("O nome do medicamento não pode ficar vazio.")

    # Verifica se a categoria foi preenchida.
    while True:
        categoria = input("Categoria: ").strip()

        if categoria:
            break

        print("A categoria do medicamento não pode ficar vazia.")

    # Verifica se a quantidade é válida.
    while True:
        try:
            quantidade = int(input("Quantidade em estoque: "))

            if quantidade < 0:
                print("A quantidade não pode ser negativa.")
            else:
                break

        except ValueError:
            print("Digite uma quantidade válida.")

    medicamento = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade
    }

    medicamentos.append(medicamento)

    print("Medicamento cadastrado com sucesso!")

    return medicamentos


def listar_medicamentos(medicamentos):
    """Exibe todos os medicamentos cadastrados."""
    print("\n--- MEDICAMENTOS CADASTRADOS ---")

    if len(medicamentos) == 0:
        print("Nenhum medicamento cadastrado.")
        return False

    for numero, medicamento in enumerate(medicamentos, start=1):
        print(f"\n{numero}. {medicamento['nome']}")
        print(f"   Categoria: {medicamento['categoria']}")
        print(f"   Estoque: {medicamento['quantidade']}")

    return True


def buscar_medicamento(medicamentos, nome):
    """Busca medicamentos pelo nome."""
    encontrados = []

    for medicamento in medicamentos:
        if nome.lower() in medicamento["nome"].lower():
            encontrados.append(medicamento)

    return encontrados


def exibir_busca(medicamentos):
    """Solicita um nome e exibe o resultado da busca."""
    print("\n--- BUSCAR MEDICAMENTO ---")

    nome = input("Digite o nome do medicamento: ").strip()
    resultados = buscar_medicamento(medicamentos, nome)

    if len(resultados) == 0:
        print("Medicamento não encontrado.")
        return False

    for medicamento in resultados:
        print("\nMedicamento encontrado:")
        print(f"Nome: {medicamento['nome']}")
        print(f"Categoria: {medicamento['categoria']}")
        print(f"Estoque: {medicamento['quantidade']}")

    return True


def main():
    # Carrega os dados salvos antes de iniciar o menu.
    medicamentos = carregar_medicamentos(ARQUIVO)

    while True:
        print("\n==============================")
        print("   SISTEMA DE MEDICAMENTOS")
        print("==============================")
        print("1 - Cadastrar medicamento")
        print("2 - Listar medicamentos")
        print("3 - Buscar medicamento")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            medicamentos = cadastrar_medicamento(medicamentos)
            salvar_medicamentos(medicamentos, ARQUIVO)

        elif opcao == "2":
            listar_medicamentos(medicamentos)

        elif opcao == "3":
            exibir_busca(medicamentos)

        elif opcao == "4":
            salvar_medicamentos(medicamentos, ARQUIVO)
            print("Dados salvos. Programa encerrado.")
            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 4.")


if __name__ == "__main__":
    main()
