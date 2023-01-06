def cifra_cesar(texto, chave):
    """Cifra o texto informado utilizando a Cifra de César.
    A chave especifica quantos deslocamentos devem ser feitos
    no alfabeto para cifrar o texto.
    """
    texto_cifrado = ""
    for c in texto:
        if c.isalpha():
            # Deslocando o caractere para a direita
            # no alfabeto, com o número de posições
            # especificado pela chave
            c_codificado = chr((ord(c) - ord("a") + chave) % 26 + ord("a"))
            texto_cifrado += c_codificado
        else:
            # Não alterando caracteres que não são letras
            texto_cifrado += c
    return texto_cifrado

# Exemplo de uso
texto = "ola mundo"
chave = 3
texto_cifrado = cifra_cesar(texto, chave)
print(texto_cifrado)  # Imprime "qod qrqj"

# Descriptografando o texto
texto_decifrado = cifra_cesar(texto_cifrado, -chave)
print(texto_decifrado)  # Imprime "ola mundo"
