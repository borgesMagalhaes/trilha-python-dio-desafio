# Criando um Sistema Bancário com Python

**trilha-python-dio: desafio.py**

Este projeto é um **sistema bancário simples** escrito em Python, como parte do _desafio_ da trilha de Python na Digital Innovation One (DIO). O sistema implementa **três operações** básicas: **depósito**, **saque** e **extrato**.

---

## Visão Geral

- **Depósito**: Permite inserir valores positivos na conta.
- **Saque**: Respeita o limite de 3 saques diários, com valor máximo de R\$ 500,00 por saque, além de verificar se há saldo suficiente.
- **Extrato**: Lista todas as operações (depósitos e saques) e exibe o saldo atual. Também informa a quantidade de cada tipo de operação realizada.

---

## Arquivo Principal

- **desafio.py**: Arquivo que contém todo o código do sistema bancário.

---

## Funcionamento do Código

1. **Menu Interativo**

   - Ao rodar o programa, um menu oferece as opções de **Depósito**, **Saque**, **Extrato** e **Sair**.
   - O usuário pode escolher a operação digitando o número correspondente.

2. **Depósito**

   - Solicita um valor de depósito.
   - Verifica se o valor é **positivo** antes de adicioná-lo ao saldo.
   - Armazena essa operação em uma lista de movimentos (_extrato_).

3. **Saque**

   - Limita a **3 saques** por execução.
   - Exige que o valor do saque seja **positivo**, não ultrapasse **R\$ 500,00** e seja menor ou igual ao saldo.
   - Armazena a operação (valor negativo) na lista de movimentos.

4. **Extrato**
   - Lista, em ordem, cada depósito e saque feitos.
   - Mostra a **quantidade** de depósitos e saques.
   - Exibe o saldo final formatado como **R\$ x.xx**.

---

## Como Executar

1. Baixe ou clone este repositório.
2. Abra um terminal ou prompt de comando na pasta do projeto.
3. Certifique-se de ter o **Python 3** instalado (verifique com `python --version` ou `python3 --version`).
4. Execute o comando:
   ```bash
   python desafio.py
   ```
