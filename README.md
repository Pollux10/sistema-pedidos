# 📦 Sistema de Pedidos (CLI)

Sistema simples de gerenciamento de pedidos executado via terminal, desenvolvido em Python, com persistência de dados em JSON.

---

## 📄 Descrição

O sistema é uma aplicação em linha de comando que permite o gerenciamento básico de produtos e pedidos.

Ao iniciar o programa, o usuário tem acesso a um menu interativo com opções para cadastrar produtos, visualizar produtos disponíveis, realizar pedidos e consultar pedidos já realizados.

Os dados são armazenados em um arquivo no formato JSON, garantindo que as informações não sejam perdidas ao encerrar o programa.

---

## 🔄 Funcionamento

1. O usuário inicia o programa  
2. O sistema carrega os dados do arquivo `data.json`  
3. Um menu interativo é exibido  
4. O usuário pode escolher entre as seguintes opções:

- **Adicionar produto**: cadastra nome e preço  
- **Listar produtos**: exibe todos os produtos cadastrados  
- **Fazer pedido**: seleciona um produto e define a quantidade  
- **Listar pedidos**: exibe todos os pedidos realizados  

5. Todas as ações são salvas automaticamente  
6. Os dados permanecem armazenados após o encerramento do programa  

---

## 🚀 Funcionalidades

- Cadastro de produtos  
- Listagem de produtos  
- Realização de pedidos  
- Listagem de pedidos  
- Armazenamento de dados em JSON  

---

## 🛠 Tecnologias utilizadas

- Python  
- JSON  

---

## ▶️ Como executar

```bash
python sistema-pedidos.py
