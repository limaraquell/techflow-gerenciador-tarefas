from flask import Flask, request, redirect

app = Flask(__name__)

# Lista temporária para armazenar as tarefas.
# Os dados serão perdidos quando o programa for encerrado.
tarefas = []

proximo_id = 1


@app.route("/")
def inicio():
    """Exibe a página principal com todas as tarefas."""
    html = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>TechFlow - Gerenciador de Tarefas</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 40px auto;
                padding: 20px;
                background: #f4f4f4;
            }

            h1 {
                color: #333;
            }

            form {
                background: white;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 8px;
            }

            input, select, button {
                padding: 10px;
                margin: 5px;
            }

            .tarefa {
                background: white;
                padding: 15px;
                margin-bottom: 10px;
                border-radius: 8px;
            }

            .alta {
                border-left: 5px solid #d9534f;
            }

            .media {
                border-left: 5px solid #f0ad4e;
            }

            .baixa {
                border-left: 5px solid #5cb85c;
            }
        </style>
    </head>

    <body>
        <h1>TechFlow - Gerenciador de Tarefas</h1>

        <form method="POST" action="/criar">
            <h2>Nova tarefa</h2>

            <input
                type="text"
                name="titulo"
                placeholder="Título da tarefa"
                required
            >

            <input
                type="text"
                name="descricao"
                placeholder="Descrição"
            >

            <select name="prioridade">
                <option value="Baixa">Baixa</option>
                <option value="Média">Média</option>
                <option value="Alta">Alta</option>
            </select>

            <button type="submit">Criar tarefa</button>
        </form>
    """

    if tarefas:
        html += "<h2>Tarefas cadastradas</h2>"

        for tarefa in tarefas:
            prioridade = tarefa["prioridade"].lower()
            html += f"""
            <div class="tarefa {prioridade}">
                <h3>{tarefa["titulo"]}</h3>
                <p>{tarefa["descricao"]}</p>
                <p>
                    <strong>Prioridade:</strong>
                    {tarefa["prioridade"]}
                </p>
                <p>
                    <strong>Status:</strong>
                    {tarefa["status"]}
                </p>

                <a href="/concluir/{tarefa['id']}">
                    Marcar como concluída
                </a>
                |
                <a href="/excluir/{tarefa['id']}">
                    Excluir
                </a>
            </div>
            """
    else:
        html += "<p>Nenhuma tarefa cadastrada.</p>"

    html += """
    </body>
    </html>
    """

    return html


@app.route("/criar", methods=["POST"])
def criar_tarefa():
    """Cria uma nova tarefa."""
    global proximo_id

    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")
    prioridade = request.form.get("prioridade")

    tarefa = {
        "id": proximo_id,
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": "A Fazer"
    }

    tarefas.append(tarefa)
    proximo_id += 1

    return redirect("/")


@app.route("/concluir/<int:tarefa_id>")
def concluir_tarefa(tarefa_id):
    """Altera o status de uma tarefa para concluída."""
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["status"] = "Concluída"

    return redirect("/")
@app.route("/editar/<int:tarefa_id>", methods=["POST"])
def editar_tarefa(tarefa_id):
    """Atualiza os dados de uma tarefa."""
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
            tarefa["titulo"] = request.form.get("titulo")
            tarefa["descricao"] = request.form.get("descricao")
            tarefa["prioridade"] = request.form.get("prioridade")

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    

@app.route("/excluir/<int:tarefa_id>")
def excluir_tarefa(tarefa_id):
    """Exclui uma tarefa."""
    global tarefas

    tarefas = [
        tarefa for tarefa in tarefas
        if tarefa["id"] != tarefa_id
    ]

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
