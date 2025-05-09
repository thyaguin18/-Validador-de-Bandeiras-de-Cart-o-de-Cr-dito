"""
Módulo para armazenar os padrões (regex) e informações das bandeiras de cartão de crédito.
Os padrões são baseados em informações públicas e podem precisar de atualização periódica.
Referência inicial: https://www.tabnews.com.br/WhiteWalter75/melhor-metodo-para-identificar-bandeira-do-cartao-de-credito
"""

# Dicionário com os padrões de expressões regulares para cada bandeira de cartão.
# As chaves são os nomes das bandeiras e os valores são as expressões regulares.
# As regex consideram os BINs (Bank Identification Numbers) e os comprimentos típicos dos cartões.

PADROES_BANDEIRAS = {
    "Visa": r"^4[0-9]{12}(?:[0-9]{3}|[0-9]{6})?$",  # Começa com 4, comprimento 13, 16 ou 19
    "MasterCard": r"^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$", # Começa com 51-55 ou 2221-2720, comprimento 16
    "Amex": r"^3[47][0-9]{13}$",  # Começa com 34 ou 37, comprimento 15
    "Elo": r"^(?:401178|401179|431274|438935|451416|457393|457631|457632|504175|506699|5067[0-6][0-9]|50677[0-8]|509[0-9]{3}|627780|636297|636368|636369|65003[1-3]|65003[5-9]|65004[0-9]|65005[0-1]|65040[5-9]|6504[1-3][0-9]|65048[5-9]|65049[0-9]|65050[0-9]|65051[0-9]|6505[2-3][0-9]|65054[1-9]|6505[5-8][0-9]|65059[0-8]|65070[0-9]|65071[0-8]|65072[0-7]|65090[1-9]|65091[0-9]|650920|65165[2-9]|6516[6-7][0-9]|65500[0-9]|65501[0-9]|6550[2-5][0-9])[0-9]{8,12}$", # BINs específicos, comprimento geralmente 16
    "Diners Club": r"^3(?:0[0-5]|[689][0-9])[0-9]{11,13}$",  # Começa com 300-305, 36, 38, 39, comprimento 14-16
    "Discover": r"^(?:6011|65[0-9]{2}|64[4-9][0-9]|622(?:12[6-9]|1[3-9][0-9]|[2-8][0-9]{2}|9[01][0-9]|92[0-5]))[0-9]{12,15}$", # Começa com 6011, 644-649, 65, 622126-622925, comprimento 16 ou 19
    "Hipercard": r"^(?:3841[0,4,6]0|606282)[0-9]{10,13}$",  # Começa com 384100, 384140, 384160, 606282, comprimento 16 ou 19 (mais comum 16)
    "JCB": r"^(?:2131|1800|35[0-9]{3})[0-9]{11,15}$",  # Começa com 2131, 1800, 3528-3589, comprimento 16-19
    "Aura": r"^50[0-9]{14,17}$", # Começa com 50, comprimento 16-19 (geralmente 16)
    "UnionPay": r"^62[0-9]{14,17}$", # Começa com 62, comprimento 16-19
    "Maestro": r"^(?:5[0678][0-9]{2}|6[0-9]{3})[0-9]{8,15}$", # Começa com 50, 56-58, 6xxx, comprimento 12-19
    "Cabal": r"^(?:589657|60[0-3][0-9]{3}|604[2-3][0-9]{2})[0-9]{10,13}$" # BINs específicos, comprimento 16-19
}

