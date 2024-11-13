import json
import random


# Funções para salvar e carregar dados em um arquivo JSON
def salvar_dados(dados, arquivo='dados_agricultura.json'):
    with open(arquivo, 'w') as f:
        json.dump(dados, f, indent=4)


def carregar_dados(arquivo='dados_agricultura.json'):
    try:
        with open(arquivo, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Funções de validação
def validar_numero(mensagem, tipo=int):
    while True:
        try:
            valor = tipo(input(mensagem))
            if valor < 0:
                raise ValueError("O valor não pode ser negativo.")
            return valor
        except ValueError as e:
            print(f"Erro: {e}")


def validar_opcao(mensagem, opcoes):
    while True:
        opcao = input(mensagem).strip().lower()
        if opcao in opcoes:
            return opcao
        else:
            print("Opção inválida. Tente novamente.")


# Funções para o sistema
def cadastrar_plantacao(dados):
    nome = input("Nome da Plantação: ")
    tamanho = validar_numero("Tamanho da Plantação (em hectares): ", float)
    energia_solar = validar_numero("Energia Solar Produzida (em kWh): ", float)
    dados['plantacoes'].append({
        "nome": nome,
        "tamanho": tamanho,
        "energia_solar": energia_solar,
        "uso_IA": False  # Por padrão, o uso de IA é falso
    })
    print("Plantação cadastrada com sucesso!")


def listar_plantacoes(dados):
    if not dados['plantacoes']:
        print("Nenhuma plantação cadastrada.")
        return
    print("\nPlantações cadastradas:")
    for idx, plantacao in enumerate(dados['plantacoes'], start=1):
        print(
            f"{idx}. Nome: {plantacao['nome']}, Tamanho: {plantacao['tamanho']} ha, Energia Solar: {plantacao['energia_solar']} kWh, Uso de IA: {plantacao['uso_IA']}")


def ativar_ia(dados):
    listar_plantacoes(dados)
    escolha = validar_numero("Escolha a plantação para ativar IA (0 para cancelar): ", int) - 1
    if 0 <= escolha < len(dados['plantacoes']):
        dados['plantacoes'][escolha]['uso_IA'] = True
        print("Inteligência Artificial ativada para a plantação selecionada.")

        # Simulações de funcionalidades da IA
        monitorar_clima()
        otimizar_energia(dados['plantacoes'][escolha]['energia_solar'])
        analisar_crescimento()
    else:
        print("Nenhuma alteração realizada.")


def monitorar_clima():
    clima = random.choice(["ensolarado", "nublado", "chuvoso", "ventoso"])
    print(
        f"A IA prevê que o clima para os próximos dias será {clima}. Ações recomendadas serão ajustadas para essas condições.")


def otimizar_energia(energia_solar):
    if energia_solar < 100:
        print("A IA recomenda economizar energia e priorizar o uso para irrigação e sistemas essenciais.")
    elif energia_solar < 300:
        print("A IA recomenda dividir a energia entre irrigação e sistemas de monitoramento.")
    else:
        print("A IA sugere utilizar parte da energia para irrigação e parte para sistemas de monitoramento avançado.")


def analisar_crescimento():
    crescimento = random.uniform(0.5, 1.5)
    print(
        f"A IA analisou os dados de crescimento e sugere que a taxa de crescimento das plantas será {crescimento:.2f} vezes a média esperada para as condições atuais.")


def calcular_media_energia(dados):
    if not dados['plantacoes']:
        print("Nenhuma plantação cadastrada.")
        return
    total_energia = sum(p['energia_solar'] for p in dados['plantacoes'])
    media_energia = total_energia / len(dados['plantacoes'])
    print(f"Média de Energia Solar Produzida: {media_energia:.2f} kWh")


def menu():
    dados = carregar_dados()
    if 'plantacoes' not in dados:
        dados['plantacoes'] = []

    while True:
        print("\n--- Sistema de Agricultura Sustentável ---")
        print("1. Cadastrar nova plantação")
        print("2. Listar plantações")
        print("3. Ativar Inteligência Artificial em uma plantação")
        print("4. Calcular média de energia solar produzida")
        print("5. Sair")

        opcao = validar_opcao("Escolha uma opção: ", ['1', '2', '3', '4', '5'])

        if opcao == '1':
            cadastrar_plantacao(dados)
        elif opcao == '2':
            listar_plantacoes(dados)
        elif opcao == '3':
            ativar_ia(dados)
        elif opcao == '4':
            calcular_media_energia(dados)
        elif opcao == '5':
            salvar_dados(dados)
            print("Saindo do sistema. Dados salvos.")
            break


# Executar o menu principal
if __name__ == "__main__":
    menu()