import hashlib

# Função para calcular o valor hash SHA-256
def getSHA(input_string):
    sha256 = hashlib.sha256()
    sha256.update(input_string.encode('utf-8'))
    return sha256.hexdigest()

# Strings das frutas
frutas = ["banana", "abacate", "melancia", "maçã", "manga", "jaca", "jaca"]

# Dicionário para rastrear os valores hash e suas posições
hash_to_index = {}

# Vetor para armazenar as frutas e seus hashes
vetor_frutas_hashes = [None] * len(frutas) * 10  # Multiplicado por 10 para evitar índices fora de alcance

# Calcular o hash para cada fruta e adicioná-la ao vetor
for fruta in frutas:
    hash_fruta = getSHA(fruta)
    
    # Encontrar o primeiro dígito numérico no hash
    primeiro_digito_numerico = None
    for caracter in hash_fruta:
        if caracter.isdigit():
            primeiro_digito_numerico = int(caracter)
            break
    
    # Se não encontrarmos um dígito numérico, continue procurando até encontrar
    if primeiro_digito_numerico is None:
        index = 0
        while index < len(hash_fruta) and not hash_fruta[index].isdigit():
            index += 1
        primeiro_dígito_numérico = int(hash_fruta[index])
    
    # Encontrar a próxima posição disponível
    index = primeiro_digito_numerico
    colisao = False  # Variável para rastrear colisões
    while vetor_frutas_hashes[index] is not None:
        if not colisao:
            colisao = True  # Marcar que houve uma colisão
            print(f"Colisão detectada para '{fruta}' na posição {index}.")
        index += 1
    
    # Atualizar o dicionário e vetor com a posição e o hash
    hash_to_index[hash_fruta] = index
    vetor_frutas_hashes[index] = (fruta, hash_fruta)

# Imprimir o vetor resultante com as frutas e seus hashes
for i, item in enumerate(vetor_frutas_hashes):
    if item is not None:
        fruta, hash_fruta = item
        print(f"Índice {i}: Fruta: {fruta}, Hash SHA-256: {hash_fruta}")
