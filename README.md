# TechFlow - Gerenciador de Tarefas

## Sobre o projeto

O TechFlow é um sistema web básico de gerenciamento de tarefas desenvolvido para uma startup de logística.

O sistema tem como objetivo permitir que a equipe acompanhe suas atividades, organize tarefas e identifique prioridades durante o fluxo de trabalho.

## Objetivo

Desenvolver uma aplicação simples para gerenciamento de tarefas, aplicando conceitos de Engenharia de Software, metodologia ágil, versionamento de código, testes automatizados e integração contínua.

## Escopo inicial

O projeto inicialmente contempla as seguintes funcionalidades:

- Criar tarefas;
- Listar tarefas;
- Atualizar tarefas;
- Excluir tarefas;
- Definir status das tarefas;
- Definir prioridade das tarefas.

## Metodologia

O projeto utiliza a metodologia **Kanban** para organização e acompanhamento das atividades.

O quadro será dividido em três etapas:

- **To Do:** tarefas que ainda serão realizadas;
- **In Progress:** tarefas em desenvolvimento;
- **Done:** tarefas concluídas.

## Tecnologias utilizadas

- Python
- Flask
- Pytest
- Git
- GitHub
- GitHub Actions

## Estrutura do projeto

```text
techflow-gerenciador-tarefas/
├── docs/
├── src/
│   └── app.py
├── tests/
│   └── test_tarefas.py
└── README.md
## Mudança de escopo

Durante o desenvolvimento do projeto, foi identificada a necessidade de facilitar a localização de tarefas críticas pela equipe da startup de logística.

Por esse motivo, o escopo inicial foi ampliado para incluir a funcionalidade de **filtro de tarefas por prioridade**.

A mudança foi registrada no quadro Kanban por meio de um novo card e posteriormente implementada no sistema.

Após a implementação, foi criado um teste automatizado específico para verificar o funcionamento do filtro. O GitHub Actions executou os testes e confirmou que a alteração estava funcionando corretamente.

A alteração foi concluída e o card correspondente foi movido para a coluna **Done** no Kanban.

### Escopo inicial

- Criar tarefas;
- Listar tarefas;
- Atualizar tarefas;
- Excluir tarefas;
- Definir status;
- Definir prioridade.

### Nova funcionalidade adicionada

- Filtrar tarefas por prioridade (Alta, Média ou Baixa).

A mudança demonstra a capacidade do projeto de se adaptar a uma nova necessidade sem perder o controle sobre o desenvolvimento, os testes e o histórico de alterações.
