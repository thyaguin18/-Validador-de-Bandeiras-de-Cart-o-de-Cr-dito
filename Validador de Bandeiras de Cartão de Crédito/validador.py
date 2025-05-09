"""
Módulo com a lógica de validação e identificação da bandeira do cartão de crédito.
"""
import re
from padroes_cartoes import PADROES_BANDEIRAS

def limpar_numero_cartao(numero_cartao: str) -> str:
    """Remove espaços e hífens do número do cartão."""
    return numero_cartao.replace(" ", "").replace("-", "")

def validar_luhn(numero_cartao: str) -> bool:
    """
    Valida o número do cartão usando o algoritmo de Luhn.
    Adaptado de várias implementações de referência.
    """
    if not numero_cartao.isdigit():
        return False

    soma = 0
    num_digitos = len(numero_cartao)
    paridade = num_digitos % 2

    for i, digito_char in enumerate(numero_cartao):
        digito = int(digito_char)
        if i % 2 == paridade:
            soma += digito
        elif digito > 4:
            soma += 2 * digito - 9
        else:
            soma += 2 * digito
    return soma % 10 == 0

def identificar_bandeira(numero_cartao: str) -> str | None:
    """
    Identifica a bandeira do cartão de crédito com base no número.
    Utiliza as expressões regulares definidas em PADROES_BANDEIRAS.
    Retorna o nome da bandeira ou None se não for identificada.
    """
    numero_limpo = limpar_numero_cartao(numero_cartao)

    for bandeira, padrao_regex in PADROES_BANDEIRAS.items():
        if re.match(padrao_regex, numero_limpo):
            # Verifica também com Luhn antes de confirmar a bandeira
            # Embora a identificação da bandeira seja primariamente pelo BIN/prefixo e comprimento,
            # uma verificação Luhn adicional pode ser útil, mas não é estritamente para identificação de bandeira.
            # Para este projeto, focaremos na correspondência do padrão regex para a bandeira.
            return bandeira
    return None

def validar_e_identificar_cartao(numero_cartao: str) -> tuple[bool, str | None, str]:
    """
    Processo completo: limpa, valida com Luhn e identifica a bandeira.
    Retorna uma tupla: (luhn_valido, nome_da_bandeira, mensagem_status).
    """
    numero_limpo = limpar_numero_cartao(numero_cartao)

    if not numero_limpo.isdigit() or not (12 <= len(numero_limpo) <= 19):
        return False, None, "Número de cartão inválido (formato ou comprimento)."

    luhn_valido = validar_luhn(numero_limpo)
    bandeira_identificada = None

    # Tenta identificar a bandeira mesmo que Luhn seja inválido, pois o objetivo é identificar.
    for bandeira, padrao_regex in PADROES_BANDEIRAS.items():
        if re.match(padrao_regex, numero_limpo):
            bandeira_identificada = bandeira
            break # Para na primeira correspondência
    
    mensagem = f"Número: {numero_cartao}\nLimpo: {numero_limpo}\nLuhn Válido: {luhn_valido}\nBandeira: {bandeira_identificada if bandeira_identificada else 'Desconhecida'}"
    
    if not luhn_valido and bandeira_identificada:
        mensagem += " (Atenção: Padrão da bandeira corresponde, mas falhou na validação Luhn.)"
    elif not luhn_valido and not bandeira_identificada:
         mensagem = f"Número: {numero_cartao}\nLimpo: {numero_limpo}\nLuhn Válido: {luhn_valido}\nBandeira: Desconhecida. Número inválido ou bandeira não suportada."

    return luhn_valido, bandeira_identificada, mensagem

if __name__ == '__main__':
    # Exemplos de uso (para teste rápido)
    test_cards = [
        "4539780000000000",  # Visa válido
        "5100000000000000",  # MasterCard válido
        "370000000000000",   # Amex válido
        "1234567890123456",  # Inválido genérico
        "4539780000000001",  # Visa, Luhn inválido
        "6011000000000000", # Discover válido
    ]

    for card in test_cards:
        valido_luhn, bandeira, msg = validar_e_identificar_cartao(card)
        print(f"Cartão: {card}")
        print(f"  Luhn Válido: {valido_luhn}")
        print(f"  Bandeira: {bandeira}")
        print(f"  Mensagem: {msg}")
        print("---")

