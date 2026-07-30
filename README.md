Reserva Auto API

API REST desenvolvida com **FastAPI** para ajudar motoristas de aplicativo a criarem uma reserva financeira destinada à manutenção do veículo.

## Objetivo

Muitos motoristas de aplicativo acabam adiando manutenções por falta de planejamento financeiro.
Este projeto busca resolver esse problema permitindo que o motorista organize uma reserva destinada exclusivamente à manutenção do carro.

## Tecnologias

- Python
- FastAPI
- Pydantic
- SQLAlchemy (em desenvolvimento)
- PostgreSQL (em desenvolvimento)

## Funcionalidades atuais

- Cadastro de motoristas
- Validação de dados com Pydantic
- Documentação automática com Swagger

## Próximas funcionalidades

- Login com JWT
- Banco de dados PostgreSQL
- Metas de economia
- Histórico de depósitos
- Controle de manutenção
- Integração com PIX
- Dashboard financeiro

## Como executar

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Acesse:

```
http://127.0.0.1:8000/docs
```

## Status

Projeto em desenvolvimento.

## Autor

Sérgio Antônio da Silva Filho
