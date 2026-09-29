import sys

sys.path.insert(0, "src")

from app import app


def test_pagina_inicial():
    """Verifica se a página inicial está funcionando."""
    cliente = app.test_client()

    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert b"TechFlow" in resposta.data


def test_criar_tarefa():
    """Verifica se uma tarefa pode ser criada."""
    cliente = app.test_client()

    resposta = cliente.post(
        "/criar",
        data={
            "titulo": "Entregar pedido",
            "descricao": "Separar pedido do cliente",
            "prioridade": "Alta"
        }
    )

    assert resposta.status_code == 302


def test_concluir_tarefa():
    """Verifica se uma tarefa pode ser concluída."""
    cliente = app.test_client()

    cliente.post(
        "/criar",
        data={
            "titulo": "Testar sistema",
            "descricao": "Executar testes",
            "prioridade": "Média"
        }
    )

    resposta = cliente.get("/concluir/1")

    assert resposta.status_code == 302


def test_excluir_tarefa():
    """Verifica se uma tarefa pode ser excluída."""
    cliente = app.test_client()

    cliente.post(
        "/criar",
        data={
            "titulo": "Tarefa temporária",
            "descricao": "Tarefa para teste",
            "prioridade": "Baixa"
        }
    )

    resposta = cliente.get("/excluir/1")

    assert resposta.status_code == 302

def test_editar_tarefa():
    """Verifica se uma tarefa pode ser atualizada."""
    from app import tarefas

    cliente = app.test_client()

    tarefas.clear()

    cliente.post(
        "/criar",
        data={
            "titulo": "Tarefa original",
            "descricao": "Descrição original",
            "prioridade": "Baixa"
        }
    )

    tarefa_id = tarefas[-1]["id"]

    resposta = cliente.post(
        f"/editar/{tarefa_id}",
        data={
            "titulo": "Tarefa atualizada",
            "descricao": "Nova descrição",
            "prioridade": "Alta"
        }
    )

    assert resposta.status_code == 302
    assert tarefas[-1]["titulo"] == "Tarefa atualizada"
    assert tarefas[-1]["descricao"] == "Nova descrição"
    assert tarefas[-1]["prioridade"] == "Alta"
