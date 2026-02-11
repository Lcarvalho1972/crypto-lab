"""
Pipeline didático: SHA-256 + Criptografia + Descriptografia + comparação de integridade

Objetivo:
1) Calcular SHA-256 do arquivo original (impressão digital)
2) Criptografar o arquivo (Fernet)
3) Descriptografar (em memória, sem precisar salvar o TXT restaurado)
4) Calcular SHA-256 do conteúdo restaurado
5) Comparar hashes -> prova matemática de que o conteúdo voltou igual

Observação:
- Fernet já garante integridade internamente (HMAC), mas aqui fazemos a validação explícita com SHA-256
  para fins didáticos.
"""
import hashlib
import os
from cryptography.fernet import Fernet

ARQUIVO_ORIGINAL = "criptografia_e_hash_explicacao.txt"
ARQUIVO_ENC = ARQUIVO_ORIGINAL + ".enc"


def sha256_bytes(data: bytes) -> str:
    """Retorna o SHA-256 (hex) de bytes."""
    return hashlib.sha256(data).hexdigest()


def carregar_arquivo_binario(path: str) -> bytes:
    """Lê arquivo em modo binário e retorna bytes."""
    with open(path, "rb") as f:
        return f.read()


def salvar_arquivo_binario(path: str, data: bytes) -> None:
    """Salva bytes em arquivo binário."""
    with open(path, "wb") as f:
        f.write(data)


def main():
    # 1) Validações simples
    if not os.path.exists(ARQUIVO_ORIGINAL):
        raise FileNotFoundError(f"Arquivo original não encontrado: {ARQUIVO_ORIGINAL}")

    # 2) Carrega original e calcula hash
    dados_original = carregar_arquivo_binario(ARQUIVO_ORIGINAL)
    hash_original = sha256_bytes(dados_original)

    # 3) Carrega chave via variável de ambiente
    chave_env = os.environ.get("SECRET_KEY")
    if not chave_env:
        raise ValueError("SECRET_KEY não encontrada. Defina a variável de ambiente para executar o pipeline.")

    chave = chave_env.encode()
    fernet = Fernet(chave)

    # 4) Criptografa e salva .enc
    token = fernet.encrypt(dados_original)
    salvar_arquivo_binario(ARQUIVO_ENC, token)

    # 5) Descriptografa (em memória) e calcula hash do restaurado
    dados_restaurados = fernet.decrypt(token)
    hash_restaurado = sha256_bytes(dados_restaurados)

    # 6) Compara
    print("\n=== PIPELINE DE INTEGRIDADE (SHA-256) ===")
    print(f"Arquivo: {ARQUIVO_ORIGINAL}")
    print(f"SHA-256 original  : {hash_original}")
    print(f"SHA-256 restaurado: {hash_restaurado}")

    if hash_original == hash_restaurado:
        print("\n✅ Integridade confirmada: conteúdo voltou idêntico após encrypt → decrypt.\n")
    else:
        print("\n❌ Integridade falhou: hashes diferentes (conteúdo não voltou igual).\n")


if __name__ == "__main__":
    main()
