# 🔐 Crypto Lab — Criptografia, Hash e Verificação de Integridade

Projeto técnico em Python demonstrando, na prática, os conceitos de:

- 🔒 Criptografia Simétrica (Fernet / AES)
- 🔓 Descriptografia
- 🔎 Hash SHA-256
- 🧪 Pipeline de verificação de integridade
- 📦 Controle de versão com Git

Este repositório foi desenvolvido como laboratório educacional para compreender a diferença entre **confidencialidade** e **integridade**, além de demonstrar a validação matemática do conteúdo após criptografia.
---
# 📂 Estrutura do Projeto

crypto-lab/
│
├── encrypt_file.py
├── descriptografar.py
├── hash_sha256.py
├── pipeline_integridade.py
├── criptografia_e_hash_explicacao.txt
├── criptografia_e_hash_explicacao.txt.enc
├── criptografia_e_hash_explicacao.txt.sha256
├── chave.key
├── README.md
└── .gitignore

---

# 🧠 Conceitos Fundamentais
## 1️⃣ Criptografia Simétrica (Confidencialidade)

Implementada com:
```python

from cryptography.fernet import Fernet

O módulo Fernet fornece:

- Criptografia baseada em AES
- Autenticação via HMAC-SHA256
- Token seguro contendo timestamp
- Reversibilidade com a mesma chave

Fluxo:

Arquivo original (.txt)
    ↓
encrypt_file.py
    ↓
Arquivo criptografado (.enc)

E o processo inverso:

Arquivo criptografado (.enc)
    ↓
descriptografar.py
    ↓
Conteúdo original restaurado

Objetivo: garantir confidencialidade.

2️⃣ Hash SHA-256 (Integridade)

Implementado com:
import hashlib

O SHA-256:
Gera uma impressão digital fixa de 64 caracteres hexadecimais
**É irreversível - Qualquer alteração de 1 byte altera completamente o hash
Não utiliza chave

Fluxo:
Arquivo original
    ↓
hash_sha256.py
    ↓
Arquivo .sha256 contendo o hash

Objetivo: garantir integridade explícita.

3️⃣ Pipeline de Integridade (Validação Matemática)

Arquivo:
-pipeline_integridade.py

Este script integra criptografia e hash no mesmo fluxo.

Processo implementado:
Arquivo original
   ↓
SHA-256 (hash original)
   ↓
Criptografia
   ↓
Descriptografia
   ↓
SHA-256 (hash restaurado)
   ↓
Comparação

Se:

hash_original == hash_restaurado

Então:

Integridade confirmada

Isso prova matematicamente que o conteúdo restaurado é idêntico ao original.

🧠 O que este projeto prova tecnicamente

1️⃣ Confidencialidade → via criptografia simétrica
2️⃣ Integridade implícita → via HMAC do Fernet
3️⃣ Integridade explícita → via SHA-256
4️⃣ Validação matemática → hashes idênticos após ciclo completo
5️⃣ Controle de versão → rastreabilidade com Git

⚙️ Como Executar
1️⃣ Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate

2️⃣ Instalar dependência
pip install cryptography
3️⃣ Criptografar
python encrypt_file.py
4️⃣ Descriptografar
python descriptografar.py
5️⃣ Gerar SHA-256
python hash_sha256.py
6️⃣ Executar o Pipeline Completo
python pipeline_integridade.py

⚠️ Aviso de Segurança

O arquivo chave.key está versionado apenas para fins educacionais.
Em ambiente real:
-Nunca versionar chaves
-Utilizar variáveis de ambiente
-Utilizar gerenciadores de segredo (Vault, Azure Key Vault, etc.)

🎯 Finalidade Educacional
Este projeto foi desenvolvido para consolidar:
- Conceitos de segurança da informação
- Diferença entre criptografia e hash
- Validação de integridade
- Organização de projeto com Git

📜 Licença

Uso educacional.
---

