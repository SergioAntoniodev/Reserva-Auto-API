# Reserva Auto API

API REST desenvolvida com **Python e FastAPI** para gerenciamento de motoristas e veículos, com autenticação JWT e integração com PostgreSQL.

O projeto está sendo desenvolvido como parte do meu portfólio de **Backend Development**, com foco em construção de APIs, autenticação, banco de dados, regras de negócio e boas práticas de desenvolvimento.

## Objetivo

A Reserva Auto API tem como objetivo servir como backend para um sistema de gerenciamento de veículos, permitindo que motoristas cadastrem e gerenciem seus veículos de forma segura através de uma API REST.

O projeto também será evoluído para incluir funcionalidades relacionadas a **manutenção e reserva de veículos**.

---

## Tecnologias utilizadas

* **Python**
* **FastAPI**
* **SQLAlchemy**
* **PostgreSQL**
* **Pydantic**
* **JWT**
* **pwdlib**
* **Git**
* **GitHub**
* **Swagger / OpenAPI**

---

## Autenticação

A API utiliza **JWT (JSON Web Token)** para autenticação.

O fluxo funciona da seguinte forma:

```text
Login
  ↓
Email + senha
  ↓
Validação da senha
  ↓
JWT
  ↓
Token Bearer
  ↓
Acesso aos endpoints protegidos
```

Os endpoints protegidos utilizam o usuário autenticado para identificar o motorista responsável pelos recursos.

---

## Motoristas

O sistema possui CRUD de motoristas.

### Funcionalidades

* Cadastro de motorista
* Listagem de motoristas
* Busca de motorista
* Atualização de motorista
* Exclusão de motorista
* Senhas armazenadas utilizando hash
* Autenticação através de JWT

---

## Veículos

Foi implementado o CRUD completo de veículos.

### Funcionalidades

* Cadastro de veículo
* Listagem dos veículos do motorista autenticado
* Atualização de veículo
* Exclusão de veículo
* Associação automática do veículo ao motorista autenticado

### Dados do veículo

Cada veículo possui:

```text
id
marca
modelo
ano
placa
quilometragem
driver_id
```

### Regra de negócio

O `driver_id` não precisa ser informado pelo usuário durante o cadastro.

A API identifica o motorista através do JWT:

```text
JWT
 ↓
get_current_driver()
 ↓
current_driver.id
 ↓
Vehicle.driver_id
```

Isso garante que cada motorista trabalhe apenas com seus próprios veículos.

---

## Estrutura do projeto

```text
Reserva-Auto-API/
│
├── app/
│   ├── database/
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── driver.py
│   │   └── Vehicle.py
│   │
│   ├── routers/
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── vehicles.py
│   │
│   ├── schemas/
│   │   ├── auth.py
│   │   ├── driver.py
│   │   └── vehicle.py
│   │
│   ├── services/
│   │   └── security.py
│   │
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Endpoints atuais

### Autenticação

| Método | Endpoint | Descrição                     |
| ------ | -------- | ----------------------------- |
| POST   | `/login` | Autenticação e geração do JWT |

### Motoristas

| Método | Endpoint             | Descrição           |
| ------ | -------------------- | ------------------- |
| POST   | `/users`             | Criar motorista     |
| GET    | `/users`             | Listar motoristas   |
| GET    | `/users/{id}`        | Buscar motorista    |
| PUT    | `/users/{driver_id}` | Atualizar motorista |
| DELETE | `/users/{driver_id}` | Excluir motorista   |

### Veículos

| Método | Endpoint                 | Descrição                    |
| ------ | ------------------------ | ---------------------------- |
| POST   | `/vehicles/`             | Criar veículo                |
| GET    | `/vehicles/`             | Listar veículos do motorista |
| PUT    | `/vehicles/{vehicle_id}` | Atualizar veículo            |
| DELETE | `/vehicles/{vehicle_id}` | Excluir veículo              |

---

## Testes da API

Os endpoints podem ser testados através da documentação interativa gerada automaticamente pelo FastAPI:

```text
http://127.0.0.1:8000/docs
```

O Swagger permite realizar autenticação utilizando o token JWT e testar os endpoints protegidos.

---

## Próximos passos

O projeto continua em desenvolvimento.

### Roadmap

* [x] Configuração do FastAPI
* [x] Integração com PostgreSQL
* [x] Configuração do SQLAlchemy
* [x] CRUD de motoristas
* [x] Hash de senhas
* [x] Autenticação JWT
* [x] CRUD de veículos
* [x] Associação entre motorista e veículo
* [ ] Cadastro de manutenções
* [ ] Histórico de manutenção dos veículos
* [ ] Sistema de reservas
* [ ] Regras de negócio para reservas
* [ ] Testes automatizados
* [ ] Docker
* [ ] Deploy em cloud

---

## Objetivo do projeto

Este projeto faz parte da minha evolução no desenvolvimento **Backend com Python**, colocando em prática conceitos de:

* Desenvolvimento de APIs REST
* Autenticação e segurança
* Bancos de dados relacionais
* ORM
* Validação de dados
* Relacionamento entre entidades
* CRUD
* Regras de negócio
* Git e GitHub
* Documentação de APIs

O objetivo é evoluir continuamente a aplicação, adicionando novas funcionalidades e aplicando conceitos utilizados no desenvolvimento backend profissional.

---

## Desenvolvedor

**Sérgio Antônio da Silva**

Estudante de Análise e Desenvolvimento de Sistemas e desenvolvedor focado em Backend.

**Tecnologias:** Python • FastAPI • SQLAlchemy • PostgreSQL • SQL • Git • GitHub
