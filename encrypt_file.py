"""
Exercício didático de criptografia com Fernet (cryptography)

Objetivo:
- Gerar uma chave simétrica
- Salvar a chave em arquivo
- Criptografar um arquivo .txt
- Salvar o arquivo criptografado

Observação:
Neste exercício, a chave será versionada no Git apenas para fins educacionais.
Em ambiente real, NUNCA se deve subir a chave ao repositório.
"""

from cryptography.fernet import Fernet
import os

# ==============================
# 1) DEFINIÇÃO DOS ARQUIVOS
# ==============================

arquivo_original = "criptografia_e_hash_explicacao.txt"
arquivo_criptografado = arquivo_original + ".enc"
arquivo_chave = "chave.key"

# ==============================
# 2) GERAÇÃO OU REUTILIZAÇÃO DA CHAVE
# ==============================

# Tenta obter chave da variável de ambiente
chave_env = os.environ.get("SECRET_KEY")

if chave_env:
    chave = chave_env.encode()
else:
    print("Variável SECRET_KEY não encontrada. Gerando chave local para modo laboratório.")
    chave = Fernet.generate_key()

# ==============================
# 3) CARREGAR ARQUIVO ORIGINAL
# ==============================

with open(arquivo_original, "rb") as f:
    dados = f.read()

# ==============================
# 4) CRIPTOGRAFAR
# ==============================

fernet = Fernet(chave)
dados_criptografados = fernet.encrypt(dados)

# ==============================
# 5) SALVAR ARQUIVO CRIPTOGRAFADO
# ==============================

with open(arquivo_criptografado, "wb") as f_enc:
    f_enc.write(dados_criptografados)

print(f"Arquivo criptografado com sucesso: {arquivo_criptografado}")
