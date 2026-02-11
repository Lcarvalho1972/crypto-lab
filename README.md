# crypto-lab 🔐 (Fernet / cryptography)

Projeto didático em Python para demonstrar **criptografia simétrica** usando `cryptography.fernet`.

> ⚠️ Aviso (muito importante): neste repositório a chave `chave.key` é versionada **apenas para fins educacionais**.
> Em um cenário real, **NUNCA** suba chaves, senhas ou segredos para o GitHub.
---
## ✅ O que este projeto faz
- Gera (ou reutiliza) uma chave simétrica (`chave.key`)
- Criptografa um arquivo `.txt` e salva como `.enc`
- Descriptografa o `.enc` e imprime o conteúdo original no terminal

Arquivos principais:
- `encrypt_file.py` → criptografa
- `descriptografar.py` → descriptografa
- `criptografia_e_hash_explicacao.txt` → arquivo original (exemplo)
- `criptografia_e_hash_explicacao.txt.enc` → arquivo criptografado gerado
- `chave.key` → chave simétrica (didático)
---
## 📦 Requisitos
- Python 3.x
- Biblioteca `cryptography`
---
## 🧪 Como executar (passo a passo)
### 1) Criar e ativar o ambiente virtual
```bash
python3 -m venv .venv
source .venv/bin/activate
