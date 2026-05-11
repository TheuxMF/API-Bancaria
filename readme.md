# Desafio: API Bancária Assíncrona com FastAPI

Neste desafio, você irá projetar e implementar uma API RESTful assíncrona usando FastAPI para gerenciar operações bancárias de depósitos e saques, vinculadas a contas correntes. Este desafio irá lhe proporcionar a experiência de construir uma aplicação backend moderna e eficiente que utiliza autenticação JWT e práticas recomendadas de design de APIs.

---

## Objetivos e Funcionalidades

O objetivo deste desafio é desenvolver uma API com as seguintes funcionalidades:

- **Cadastro de Transações:**  
  Permita o cadastro de transações bancárias, como depósitos e saques.

- **Exibição de Extrato:**  
  Implemente um endpoint para exibir o extrato de uma conta, mostrando todas as transações realizadas.

- **Autenticação com JWT:**  
  Utilize JWT (JSON Web Tokens) para garantir que apenas usuários autenticados possam acessar os endpoints que exigem autenticação.

---

## Requisitos Técnicos

Para a realização deste desafio, você deve atender aos seguintes requisitos técnicos:

- **FastAPI:**  
  Utilize FastAPI como framework para criar sua API. Aproveite os recursos assíncronos do framework para lidar com operações de I/O de forma eficiente.

- **Modelagem de Dados:**  
  Crie modelos de dados adequados para representar contas correntes e transações. Garanta que as transações estejam relacionadas a uma conta corrente e que uma conta possa ter múltiplas transações.

- **Autenticação JWT:**  
  Implemente autenticação baseada em JWT para proteger os endpoints da API.

- **Boas Práticas REST:**  
  Estruture os endpoints seguindo os padrões RESTful, utilizando corretamente métodos HTTP, códigos de status e organização de rotas.

- **Banco de Dados:**  
  Utilize um banco de dados para persistência das informações de contas e transações.

- **Operações Assíncronas:**  
  Utilize programação assíncrona (`async/await`) para melhorar o desempenho da aplicação.

---

## Tecnologias Utilizadas

- Python
- FastAPI
- JWT Authentication
- SQLAlchemy / ORM
- Banco de Dados SQL
- Uvicorn

---

## Estrutura Esperada da API

### Endpoints principais

#### Autenticação
- `POST /login`
- `POST /register`

#### Contas
- `GET /accounts/{id}`
- `POST /accounts`

#### Transações
- `POST /transactions/deposit`
- `POST /transactions/withdraw`
- `GET /transactions/statement/{account_id}`

---

## Objetivo do Projeto

Este projeto faz parte de um desafio prático da plataforma DIO (Digital Innovation One), com foco no desenvolvimento de APIs modernas utilizando FastAPI, autenticação JWT e programação assíncrona em Python.

---

## Autor

Projeto desenvolvido por **Matheus Marques** durante os estudos de backend com Python e FastAPI.