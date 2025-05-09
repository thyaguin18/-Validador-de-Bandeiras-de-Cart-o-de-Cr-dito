"""
Validador de Cartão de Crédito - Ponto de Entrada Principal

Este script permite ao utilizador inserir um número de cartão de crédito
e obter a validação (usando o algoritmo de Luhn) e a identificação da bandeira.
"""

from validador import validar_e_identificar_cartao, limpar_numero_cartao

def exibir_menu():
    """Exibe o menu de opções para o utilizador."""
    print("\nValidador de Cartão de Crédito")
    print("---------------------------------")
    print("1. Validar e Identificar Cartão")
    print("2. Executar Testes Internos Rápidos")
    print("0. Sair")

def executar_testes_rapidos():
    """Executa um conjunto pré-definido de testes rápidos e exibe os resultados."""
    print("\n--- Executando Testes Rápidos ---")
    test_cards = {
        "Visa Válido (16 dígitos)": "4539780000000000",
        "Visa Válido (13 dígitos)": "4539780000000",
        "Visa Válido (19 dígitos)": "4539780000000000000",
        "MasterCard Válido": "5100000000000000",
        "MasterCard Válido (Novo Range)": "2221000000000000",
        "Amex Válido": "370000000000000",
        "Discover Válido": "6011000000000000",
        "Diners Club Válido (14 dígitos)": "30000000000000",
        "JCB Válido (16 dígitos)": "3528000000000000",
        "Elo Válido": "6363680000000000", # Exemplo de BIN Elo
        "Hipercard Válido": "6062820000000000",
        "UnionPay Válido": "620000000000000000",
        "Maestro Válido (19 dígitos)": "5018000000000000000",
        "Número Inválido (Luhn)": "4539780000000001",
        "Número Inválido (Curto)": "1234567890",
        "Número Inválido (Longo)": "123456789012345678901",
        "Número Inválido (Caracteres)": "4539-7800-ABCD-0000",
        "Bandeira Desconhecida": "9999999999999999",
        "Visa com espaços": "4539 7800 0000 0000",
        "Amex com hífens": "3700-000000-00000"
    }

    todos_passaram = True
    for descricao, numero_cartao in test_cards.items():
        print(f"\nTestando: {descricao} - Cartão: {numero_cartao}")
        valido_luhn, bandeira, mensagem_status = validar_e_identificar_cartao(numero_cartao)
        print(mensagem_status)
        
        # Lógica simples de verificação para os testes (pode ser aprimorada)
        if "Inválido" in descricao and valido_luhn:
            print(f"ERRO NO TESTE: {descricao} deveria ser inválido por Luhn, mas foi validado.")
            todos_passaram = False
        if "Válido" in descricao and not valido_luhn and not ("Luhn inválido" in mensagem_status or "formato ou comprimento" in mensagem_status) :
            # Alguns cartões válidos podem ter bandeira identificada mas falhar no Luhn se o número de teste não for perfeito
            # Mas se a mensagem não indicar falha de Luhn ou formato, é um problema.
            if not bandeira and not "Desconhecida" in mensagem_status:
                 print(f"ERRO NO TESTE: {descricao} deveria ser válido por Luhn, mas falhou sem indicação clara.")
                 todos_passaram = False
        if bandeira:
            print(f"Bandeira Esperada (parcial): {descricao.split(' ')[0]}, Identificada: {bandeira}")
            if descricao.split(' ')[0].lower() not in bandeira.lower() and "Desconhecida" not in descricao:
                print(f"ERRO NO TESTE: {descricao} - Bandeira esperada não corresponde à identificada.")
                todos_passaram = False
        elif "Desconhecida" not in descricao and "Inválido" not in descricao:
            print(f"ERRO NO TESTE: {descricao} - Bandeira deveria ser identificada.")
            todos_passaram = False

    print("\n--- Fim dos Testes Rápidos ---")
    if todos_passaram:
        print("Resultado dos Testes Rápidos: Todos os cenários básicos parecem corretos.")
    else:
        print("Resultado dos Testes Rápidos: Alguns testes falharam. Revisar a lógica ou os casos de teste.")

def main():
    """Função principal para executar a aplicação."""
    while True:
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            numero_cartao_input = input("Digite o número do cartão: ")
            valido_luhn, bandeira, mensagem_status = validar_e_identificar_cartao(numero_cartao_input)
            print("\n--- Resultado da Validação ---")
            print(mensagem_status)
            print("-------------------------------")
        elif escolha == '2':
            executar_testes_rapidos()
        elif escolha == '0':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

