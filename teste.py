from Tarefa import Tarefa, GerenciadorTarefas


class Teste:
    # Creating some sample tasks
    tarefa1 = Tarefa("Tarefa 1", "Descrição da Tarefa 1", "Responsável 1", "Alta")
    tarefa2 = Tarefa("Tarefa 2", "Descrição da Tarefa 2", "Responsável 2", "Média")
    tarefa3 = Tarefa("Tarefa 3", "Descrição da Tarefa 3", "Responsável 3", "Baixa")

    # Creating a task manager
    gerenciador = GerenciadorTarefas()

    # Adding tasks to the task manager
    gerenciador.adicionar_tarefa(tarefa1)
    gerenciador.adicionar_tarefa(tarefa2)
    gerenciador.adicionar_tarefa(tarefa3)

    # Listing all tasks
    gerenciador.listar_tarefas()

    # Moving task 1 to "Em Andamento"
    gerenciador.marcar_tarefa_em_andamento(1)

    # Listing tasks by stage
    gerenciador.listar_tarefas_por_etapa("Pendente")
    gerenciador.listar_tarefas_por_etapa("Em Andamento")
    gerenciador.listar_tarefas_por_etapa("Concluída")

# dandan é dogs 