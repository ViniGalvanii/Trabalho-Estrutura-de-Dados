# Trabalho-Estrutura-de-Dados: Sistema de Controle de Estoque com Estruturas de Dados

## Disciplina

Organização e Abstração na Programação

## Título do Trabalho

Sistema de Controle de Estoque utilizando Estruturas de Dados

## Integrantes

* Lucas A. Zilio - 1134707
* Vinicius Galvanii - 1137277


## Descrição do Sistema

Este sistema foi desenvolvido em Python com o objetivo de gerenciar um controle de estoque simples.

O sistema permite:

* Cadastro e listagem de clientes
* Cadastro e listagem de produtos
* Pesquisa de produtos por ID ou nome
* Realização de vendas
* Controle de fila de vendas
* Desfazer última operação realizada
* Cálculo do valor total do estoque
* Cálculo do valor total de vendas
* Relatório de clientes com valores gastos

Todas as operações são realizadas via menu interativo no terminal.

## Estruturas de Dados Utilizadas

O sistema utiliza três estruturas principais:

### Lista Encadeada

Utilizada para armazenar:

* Clientes
* Produtos

Permite inserção dinâmica e percorrimento eficiente dos dados.


### Fila (FIFO - First In, First Out)

Utilizada para armazenar:

* Vendas realizadas

A fila garante que as vendas sejam organizadas na ordem em que ocorreram.


### Pilha (LIFO - Last In, First Out)

Utilizada para:

* Desfazer a última operação realizada

A pilha armazena ações como:

* Cadastro de cliente
* Cadastro de produto
* Venda

Permitindo reverter a última ação executada.


## Persistência de Dados

O sistema utiliza arquivos CSV para armazenar os dados:

* `clientes.csv`
* `produtos.csv`
* `vendas.csv`

### Funcionamento:

* Ao iniciar o sistema, os dados são carregados automaticamente dos arquivos
* Sempre que ocorre uma alteração (cadastro ou venda), os dados são salvos automaticamente

Isso garante que as informações não sejam perdidas ao encerrar o programa.


## Como Executar o Projeto

### Requisitos:

* Python 3 instalado

### Execução:

1. Abra o terminal na pasta do projeto
2. Execute o comando:

```bash
python main.py
```

3. Utilize o menu exibido para interagir com o sistema


## Estrutura do Projeto

* `main.py` → Arquivo principal
* `cliente.py` → Classe Cliente
* `produto.py` → Classe Produto
* `venda.py` → Classe Venda
* `ListaEncadeada.py` → Estrutura de lista encadeada
* `fila.py` → Estrutura de fila
* `pilha.py` → Estrutura de pilha
* `salvamento.py` → Persistência em CSV


## Considerações Finais

O projeto atende aos requisitos propostos, utilizando estruturas de dados fundamentais e persistência em arquivos, simulando um sistema real de controle de estoque.

