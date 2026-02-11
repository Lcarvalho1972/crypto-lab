"""
Exercício didático de DESCRIPTOGRAFIA com Fernet

Objetivo:
- Ler a chave simétrica
- Ler o arquivo criptografado
- Restaurar o conteúdo original

Observação:
Este script depende da chave.key gerada anteriormente.
"""

from cryptography.fernet import Fernet
import os

# ==============================
# 1) DEFINIÇÃO DOS ARQUIVOS
# ==============================

arquivo_chave = "chave.key"
arquivo_criptografado = "criptografia_e_hash_explicacao.txt.enc"

# ==============================
# 2) VALIDAÇÃO DE EXISTÊNCIA
# ==============================

if not os.path.exists(arquivo_chave):
    raise FileNotFoundError("Arquivo de chave não encontrado.")

if not os.path.exists(arquivo_criptografado):
    raise FileNotFoundError("Arquivo criptografado não encontrado.")

# ==============================
# 3) CARREGAR CHAVE
# ==============================

with open(arquivo_chave, "rb") as f:
    chave = f.read()

# ==============================
# 4) CARREGAR TOKEN CRIPTOGRAFADO
# ==============================

with open(arquivo_criptografado, "rb") as f:
    token = f.read()

# ==============================
# 5) DESCRIPTOGRAFAR
# ==============================

fernet = Fernet(chave)
texto_original = fernet.decrypt(token)

# ==============================
# 6) EXIBIR RESULTADO
# ==============================

print("\nConteúdo revelado com sucesso:\n")
print(texto_original.decode())
