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

if not os.path.exists(arquivo_chave):
    # Se a chave ainda não existir, gera uma nova
    chave = Fernet.generate_key()
    
    # Salva a chave em arquivo
    with open(arquivo_chave, "wb") as file_chave:
        file_chave.write(chave)
    
    print("Nova chave gerada e salva em 'chave.key'")
else:
    # Se já existir, apenas carrega
    with open(arquivo_chave, "rb") as file_chave:
        chave = file_chave.read()
    
    print("Chave existente carregada.")

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
