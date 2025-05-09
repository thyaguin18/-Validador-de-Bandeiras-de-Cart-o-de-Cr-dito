# Lê o valor máximo de caracteres permitidos
n = int(input())

# Lê o texto do post
texto = input()

# Se o tamanho do texto é menor ou igual ao limite, imprime sem alterações
if len(texto) <= n:
    print(texto)
else:
    # Caso contrário, o texto precisa ser truncado
    if n < 3:
        # Se n for muito pequeno para incluir "...", truncamos para os primeiros n caracteres do texto original.
        # Desta forma, o resultado final terá no máximo n caracteres.
        print(texto[:n])
    else:
        # Se n >= 3, há espaço para as reticências.
        # Corta os (n - 3) primeiros caracteres e adiciona as reticências.
        # O resultado terá exatamente n caracteres.
        resumo = texto[:n - 3] + "..."
        print(resumo)

