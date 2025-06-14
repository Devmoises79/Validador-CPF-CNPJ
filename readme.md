# ✅ Validador de CPF e CNPJ em Python

Este projeto tem como objetivo validar números de CPF e CNPJ informados pelo usuário, utilizando regras oficiais para o cálculo dos dígitos verificadores.

## 📌 Descrição

O programa solicita ao usuário que digite um CPF ou CNPJ (com ou sem formatação) e verifica se o número é válido de acordo com os algoritmos matemáticos definidos pela Receita Federal do Brasil.

- Valida CPFs com 11 dígitos
- Valida CNPJs com 14 dígitos
- Aceita números com ou sem pontuação (ex: `746.824.890-70` ou `74682489070`)
- Detecta repetições inválidas (ex: `111.111.111-11`)
- Implementado 100% em Python puro

## 🚀 Como Executar

1. Clone o repositório ou copie o código-fonte:

```bash
git clone https://github.com/seu-usuario/validador-cpf-cnpj.git
cd validador-cpf-cnpj
```

Execute com Python:

```bash
python validador.py
```

- Certifique-se de ter o Python 3 instalado.

# 🧠 Fundamentos Aplicados

- Manipulação de strings e listas

- Estruturas condicionais e laços

- Funções e validação de entrada

- Algoritmos matemáticos para validação de documentos

🧪 Exemplos de Testes
```bash
Entrada	Tipo	Resultado
746.824.890-70	CPF	✅ Válido
111.111.111-11	CPF	❌ Inválido
04.252.011/0001-10	CNPJ	✅ Válido
12.345.678/9012-34	CNPJ	❌ Inválido
```


## 📁 Estrutura do Projeto

```bash

validador-cpf-cnpj/
│
├── validador.py        # Arquivo principal com o código-fonte
└── README.md           # Documentação do projeto
```


🙋‍♂️ Autor
Moisés 
[@github.com/devmoises79]

# Me siga no LinkedIn! 🚀🌟
[@https://www.linkedin.com/in/moises-aniceto-71042a251/]

