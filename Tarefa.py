class Tarefa:
    def __init__(self, nome, descricao, responsavel, prioridade):
        self.nome = nome
        self.descricao = descricao
        self.responsavel = responsavel
        self.etapa = "Pendente"
        self.prioridade = prioridade

    def marcar_em_andamento(self):
        self.etapa = "Em Andamento"

    def marcar_concluida(self):
        self.etapa = "Concluída"

    def __str__(self):
        return f"{self.nome} ({self.etapa}) - Responsável: {self.responsavel} - Prioridade: {self.prioridade}"


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas_pendentes = []
        self.tarefas_em_andamento = []
        self.tarefas_concluidas = []

    def adicionar_tarefa(self, tarefa):
        if tarefa.etapa == "Pendente":
            self.tarefas_pendentes.append(tarefa)
        elif tarefa.etapa == "Em Andamento":
            self.tarefas_em_andamento.append(tarefa)
        elif tarefa.etapa == "Concluída":
            self.tarefas_concluidas.append(tarefa)

    def listar_tarefas(self):
        if len(self.tarefas_pendentes) != 0:
            print("Tarefas Pendentes:")
            for i, tarefa in enumerate(self.tarefas_pendentes):
                print(f"{i + 1}. {tarefa}")

        if len(self.tarefas_em_andamento) != 0:
            print("\n\nTarefas em Andamento:")
            for i, tarefa in enumerate(self.tarefas_em_andamento):
                print(f"{i + 1}. {tarefa}")

        if len(self.tarefas_concluidas) != 0:
            print("\n\nTarefas Concluídas:")
            for i, tarefa in enumerate(self.tarefas_concluidas):
                print(f"{i + 1}. {tarefa}")

    def listar_tarefas_por_etapa(self, etapa):
        if etapa == "Pendente" and len(self.tarefas_pendentes) != 0:
            print("Tarefas Pendentes:")
            for i, tarefa in enumerate(self.tarefas_pendentes):
                print(f"{i + 1}. {tarefa}")
        elif etapa == "Em Andamento" and len(self.tarefas_em_andamento) != 0:
            print("Tarefas em Andamento:")
            for i, tarefa in enumerate(self.tarefas_em_andamento):
                print(f"{i + 1}. {tarefa}")
        elif etapa == "Concluída" and len(self.tarefas_concluidas):
            print("Tarefas Concluídas:")
            for i, tarefa in enumerate(self.tarefas_concluidas):
                print(f"{i + 1}. {tarefa}")

    def marcar_tarefa_em_andamento(self, indice_tarefa):
        index = indice_tarefa - 1
        if 0 <= index < len(self.tarefas_pendentes):
            tarefa = self.tarefas_pendentes.pop(index)
            tarefa.marcar_em_andamento()
            self.tarefas_em_andamento.append(tarefa)
            self.registrar_kanban()
        else:
            print("Índice inválido para tarefas pendentes.")

    def marcar_tarefa_concluida(self, indice_tarefa):
        index = indice_tarefa - 1
        if 0 <= index < len(self.tarefas_em_andamento):
            tarefa = self.tarefas_em_andamento.pop(index)
            tarefa.marcar_concluida()
            self.tarefas_concluidas.append(tarefa)
            self.registrar_kanban()
        else:
            print("Índice inválido para tarefas em andamento.")

    def registrar_kanban(self):
        with open("kanban.txt", "w") as arquivo:
            arquivo.write("Tarefas Pendentes:\n")
            for i, tarefa in enumerate(self.tarefas_pendentes):
                arquivo.write(f"{i + 1}. {tarefa}\n")

            arquivo.write("\nTarefas em Andamento:\n")
            for i, tarefa in enumerate(self.tarefas_em_andamento):
                arquivo.write(f"{i + 1}. {tarefa}\n")

            arquivo.write("\nTarefas Concluídas:\n")
            for i, tarefa in enumerate(self.tarefas_concluidas):
                arquivo.write(f"{i + 1}. {tarefa}\n")