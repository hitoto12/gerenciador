__init__(self, nome, descricao, responsavel, prioridade): 

#  O método de inicialização da classe Tarefa recebe como parâmetros o nome, descrição, responsável e prioridade da tarefa, e atribui esses valores aos respectivos atributos da classe.

marcar_em_andamento(self):
#  Método que atualiza a etapa da tarefa para "Em Andamento".

marcar_concluida(self):
#  Método que atualiza a etapa da tarefa para "Concluída".

__str__(self):
#  Método que retorna uma representação em string da tarefa.

obter_prioridade_texto(self):
#  Método que retorna o texto correspondente à prioridade da tarefa.

Função registrar_kanban(string):
#  Função que recebe uma string como parâmetro e registra essa string em um arquivo chamado "kanban.txt".


Classe GerenciadorTarefas:

__init__(self):
#  O método de inicialização da classe GerenciadorTarefas cria três listas vazias para armazenar as tarefas pendentes, em andamento e concluídas.

adicionar_tarefa(self, tarefa):
#  Método que recebe uma instância da classe Tarefa como parâmetro e adiciona a tarefa à lista correspondente à sua etapa.

listar_tarefas(self):
#  Método que retorna uma representação em string das tarefas organizadas por etapa e prioridade.

marcar_tarefa_em_andamento(self, indice_tarefa):
#  Método que recebe o índice da tarefa pendente a ser movida para a etapa "Em Andamento" e realiza a alteração.

marcar_tarefa_concluida(self, indice_tarefa):

#  Método que recebe o índice da tarefa a ser movida para a etapa "Concluída" e realiza a alteração.

organizar_tarefas_por_prioridade(self): 

# Método que organiza as tarefas em cada etapa com base em sua prioridade.


Classe InterfaceGrafica:

__init__(self):

#  O método de inicialização da classe InterfaceGrafica configura a janela principal da interface gráfica, cria os elementos da interface (rótulos, botões, lista de tarefas) e chama o método listar_tarefas() para exibir as tarefas na lista.

abrir_janela_adicionar_tarefa(self):

#  Método que abre uma janela para adicionar uma nova tarefa, exibindo campos de entrada para nome, descrição, responsável e prioridade.

adicionar_tarefa(self, nome, descricao, responsavel, prioridade, janela_adicionar):

#  Método que recebe os valores inseridos nos campos de entrada da janela de adição de tarefas, cria uma instância da classe Tarefa e a adiciona ao gerenciador de tarefas.

marcar_tarefa_em_andamento(self): 
# Método que marca a tarefa selecionada na lista como "Em Andamento".

marcar_tarefa_concluida(self): 
# Método que marca a tarefa.
