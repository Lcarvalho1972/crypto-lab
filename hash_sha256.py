"""
Exercício didático: Hash SHA-256 de arquivos

Objetivo:
- Calcular a "impressão digital" (hash) de um arquivo
- Usar SHA-256 para verificar integridade (alterações mudam o hash)

Observação:
Hash NÃO é criptografia. Não existe "desfazer hash".
"""

import hashlib
import os

arquivo_alvo = "criptografia_e_hash_explicacao.txt"
arquivo_saida = arquivo_alvo + ".sha256"

if not os.path.exists(arquivo_alvo):
    raise FileNotFoundError(f"Arquivo não encontrado: {arquivo_alvo}")

# Lê o arquivo em modo binário
with open(arquivo_alvo, "rb") as f:
    dados = f.read()

# Calcula SHA-256
hash_sha256 = hashlib.sha256(dados).hexdigest()

# Exibe no terminal
print(f"\nArquivo: {arquivo_alvo}")
print(f"SHA-256: {hash_sha256}\n")

# Salva em um arquivo .sha256 (útil para validar depois)
with open(arquivo_saida, "w", encoding="utf-8") as f_out:
    f_out.write(hash_sha256 + "\n")

print(f"Hash salvo em: {arquivo_saida}")
