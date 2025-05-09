# Validador de Cartão de Crédito

Este projeto tem como objetivo desenvolver uma aplicação simples capaz de identificar a bandeira de um cartão de crédito (como Visa, MasterCard, Amex, etc.) com base no número do cartão e validar o número utilizando o algoritmo de Luhn.

## Descrição

A aplicação é desenvolvida em Python e utiliza expressões regulares para identificar os padrões das bandeiras de cartão e o algoritmo de Luhn para validar a integridade do número do cartão.

O projeto foi estruturado de forma modular para facilitar o entendimento e a manutenção:

-   `main.py`: Ponto de entrada da aplicação, interface com o utilizador via linha de comando.
-   `validador.py`: Contém a lógica principal para limpar o número do cartão, validar pelo algoritmo de Luhn e identificar a bandeira.
-   `padroes_cartoes.py`: Armazena um dicionário com as expressões regulares para cada bandeira de cartão suportada.
-   `estrutura_boas_praticas.md`: Documento que detalha a estrutura do projeto e as boas práticas de codificação adotadas.

## Como Executar

1.  Certifique-se de que tem o Python 3 instalado.
2.  Guarde todos os ficheiros do projeto (`main.py`, `validador.py`, `padroes_cartoes.py`) no mesmo diretório.
3.  Abra um terminal ou linha de comando nesse diretório.
4.  Execute o script principal com o comando:
    ```bash
    python3 main.py
    ```
5.  Siga as instruções no menu para validar um número de cartão ou executar os testes internos.

## Funcionalidades

-   Limpeza do número do cartão (remove espaços e hífens).
-   Validação do número do cartão utilizando o Algoritmo de Luhn.
-   Identificação da bandeira do cartão (Visa, MasterCard, Amex, Elo, Diners Club, Discover, Hipercard, JCB, Aura, UnionPay, Maestro, Cabal) com base nos seus padrões de BIN e comprimento.
-   Interface de linha de comando interativa.
-   Conjunto de testes rápidos internos para verificar a funcionalidade básica.

## Padrões das Bandeiras

Os padrões de expressões regulares para as bandeiras estão definidos em `padroes_cartoes.py` e foram baseados em informações publicamente disponíveis. Estes padrões podem necessitar de atualizações periódicas conforme novas regras ou BINs sejam introduzidos pelas operadoras de cartão.

## Boas Práticas

O desenvolvimento seguiu boas práticas de codificação, incluindo:

-   **Modularidade**: Código dividido em ficheiros e funções com responsabilidades claras.
-   **Legibilidade**: Nomes de variáveis e funções descritivos, código bem formatado.
-   **Comentários e Docstrings**: Explicações no código e documentação de funções.
-   **Tratamento de Erros**: Validação de entradas e feedback ao utilizador.
-   **Testes**: Inclusão de testes rápidos para as funcionalidades centrais.

Este projeto demonstra como a lógica de validação de cartões pode ser implementada e como a organização do código contribui para um software mais robusto e de fácil manutenção.
