
import tkinter as tk
from tkinter import messagebox


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
        return f"{self.nome} ({self.etapa}) - Responsável: {self.responsavel} - Prioridade: " \
               f"{self.obter_prioridade_texto()}"

    def obter_prioridade_texto(self):
        if self.prioridade == 0:
            return "Baixa"
        elif self.prioridade == 1:
            return "Média"
        elif self.prioridade == 2:
            return "Alta"


def registrar_kanban(string):
    with open("kanban.txt", "w") as arquivo:
        arquivo.write(string)
        arquivo.close()


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
        self.organizar_tarefas_por_prioridade()

    def listar_tarefas(self):
        string_f = ''
        if len(self.tarefas_pendentes) != 0:
            string_f += 'Tarefas pendentes: \n'
            for i, tarefa in enumerate(self.tarefas_pendentes):
                if i + 1 == len(self.tarefas_pendentes) and len(self.tarefas_em_andamento) == 0 and len(self.tarefas_concluidas) == 0:
                    string_f += f"{i + 1}. {tarefa}"
                else:
                    string_f += f"{i + 1}. {tarefa}\n"

        if len(self.tarefas_em_andamento) != 0:
            if len(self.tarefas_pendentes) == 0:
                string_f += "Tarefas em andamento:\n"
            else:
                string_f += "\nTarefas em andamento:\n"
            for i, tarefa in enumerate(self.tarefas_em_andamento):
                if i + 1 == len(self.tarefas_em_andamento) and len(self.tarefas_concluidas) == 0:
                    string_f += f"{i + 1}. {tarefa}"
                else:
                    string_f += f"{i + 1}. {tarefa}\n"

        if len(self.tarefas_concluidas) != 0:
            if len(self.tarefas_em_andamento) == 0 and len(self.tarefas_pendentes) == 0:
                string_f += "Tarefas concluídas:\n"
            else:
                string_f += "\nTarefas concluídas:\n"
            for i, tarefa in enumerate(self.tarefas_concluidas):
                if i + 1 == len(self.tarefas_concluidas):
                    string_f += f"{i + 1}. {tarefa}"
                else:
                    string_f += f"{i + 1}. {tarefa}\n"
        registrar_kanban(string_f)
        return string_f

    def marcar_tarefa_em_andamento(self, indice_tarefa):
        index = indice_tarefa - 1
        if 0 <= index < len(self.tarefas_pendentes):
            tarefa = self.tarefas_pendentes.pop(index)
            tarefa.marcar_em_andamento()
            self.tarefas_em_andamento.append(tarefa)
        else:
            print("Índice inválido para tarefas pendentes.")

    def marcar_tarefa_concluida(self, indice_tarefa):
        index = indice_tarefa - 1
        if 0 <= index < len(self.tarefas_pendentes):
            tarefa = self.tarefas_pendentes.pop(index)
            tarefa.marcar_concluida()
            self.tarefas_concluidas.append(tarefa)
        elif 0 <= index < len(self.tarefas_em_andamento):
            tarefa = self.tarefas_em_andamento.pop(index)
            tarefa.marcar_concluida()
            self.tarefas_concluidas.append(tarefa)
        else:
            print("Índice inválido para tarefas.")

    def organizar_tarefas_por_prioridade(self):
        self.tarefas_pendentes.sort(key=lambda tarefa: tarefa.prioridade, reverse=True)
        self.tarefas_em_andamento.sort(key=lambda tarefa: tarefa.prioridade, reverse=True)
        self.tarefas_concluidas.sort(key=lambda tarefa: tarefa.prioridade, reverse=True)


class InterfaceGrafica:
    def __init__(self):
        self.gerenciador_tarefas = GerenciadorTarefas()
        self.janela_principal = tk.Tk()
        self.janela_principal.title("Gerenciador de Tarefas")
        self.janela_principal.resizable(False, False)
        self.janela_principal.geometry("600x400")

        self.frame_listagem = tk.Frame(self.janela_principal)
        self.frame_listagem.pack(pady=10)

        self.label_tarefas = tk.Label(self.frame_listagem, text="Lista de Tarefas:")
        self.label_tarefas.pack()

        self.scrollbar_y = tk.Scrollbar(self.frame_listagem)
        self.scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)

        self.scrollbar_x = tk.Scrollbar(self.frame_listagem, orient=tk.HORIZONTAL)
        self.scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.listbox_tarefas = tk.Listbox(self.frame_listagem, width=70, height=15, yscrollcommand=self.scrollbar_y.set,
                                          xscrollcommand=self.scrollbar_x.set)
        self.listbox_tarefas.pack()

        self.scrollbar_y.config(command=self.listbox_tarefas.yview)
        self.scrollbar_x.config(command=self.listbox_tarefas.xview)

        self.frame_botoes = tk.Frame(self.janela_principal)
        self.frame_botoes.pack(pady=10)

        self.botao_adicionar = tk.Button(self.frame_botoes, text="Adicionar Tarefa",
                                         command=self.abrir_janela_adicionar_tarefa)
        self.botao_adicionar.grid(row=0, column=0, padx=10)

        self.botao_em_andamento = tk.Button(self.frame_botoes, text="Marcar em Andamento",
                                            command=self.marcar_tarefa_em_andamento,)
        self.botao_em_andamento.grid(row=0, column=1, padx=10)

        self.botao_concluida = tk.Button(self.frame_botoes, text="Marcar Concluída",
                                         command=self.marcar_tarefa_concluida)
        self.botao_concluida.grid(row=0, column=2, padx=10)

        self.listar_tarefas()

    def abrir_janela_adicionar_tarefa(self):
        janela_adicionar = tk.Toplevel(self.janela_principal)
        janela_adicionar.title("Adicionar Tarefa")

        label_nome = tk.Label(janela_adicionar, text="Nome:")
        label_nome.grid(row=0, column=0, pady=5, padx=5, sticky=tk.W)

        entry_nome = tk.Entry(janela_adicionar)
        entry_nome.grid(row=0, column=1, pady=5, padx=5)

        label_descricao = tk.Label(janela_adicionar, text="Descrição:")
        label_descricao.grid(row=1, column=0, pady=5, padx=5, sticky=tk.W)

        entry_descricao = tk.Entry(janela_adicionar)
        entry_descricao.grid(row=1, column=1, pady=5, padx=5)

        label_responsavel = tk.Label(janela_adicionar, text="Responsável:")
        label_responsavel.grid(row=2, column=0, pady=5, padx=5, sticky=tk.W)

        entry_responsavel = tk.Entry(janela_adicionar)
        entry_responsavel.grid(row=2, column=1, pady=5, padx=5)

        label_prioridade = tk.Label(janela_adicionar, text="Prioridade:")
        label_prioridade.grid(row=3, column=0, pady=5, padx=5, sticky=tk.W)

        entry_prioridade = tk.Entry(janela_adicionar)
        entry_prioridade.grid(row=3, column=1, pady=5, padx=5)

        botao_adicionar = tk.Button(janela_adicionar, text="Adicionar",
                                    command=lambda: self.adicionar_tarefa(entry_nome.get(), entry_descricao.get(),
                                                                          entry_responsavel.get(),
                                                                          entry_prioridade.get(), janela_adicionar))
        botao_adicionar.grid(row=4, columnspan=2, pady=10)

    def adicionar_tarefa(self, nome, descricao, responsavel, prioridade, janela_adicionar):
        if nome and descricao and responsavel and prioridade:
            try:
                prioridade = int(prioridade)
                tarefa = Tarefa(nome, descricao, responsavel, prioridade)
                self.gerenciador_tarefas.adicionar_tarefa(tarefa)
                self.listar_tarefas()
                janela_adicionar.destroy()
            except ValueError:
                messagebox.showerror("Erro", "A prioridade deve ser um número inteiro.")
        else:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")

    def marcar_tarefa_em_andamento(self):
        selecionado = self.listbox_tarefas.curselection()
        if selecionado:
            indice_tarefa = int(selecionado[0])
            self.gerenciador_tarefas.marcar_tarefa_em_andamento(indice_tarefa)
            self.listar_tarefas()

    def marcar_tarefa_concluida(self):
        selecionado = self.listbox_tarefas.curselection()
        if selecionado:
            indice_tarefa = int(selecionado[0])
            self.gerenciador_tarefas.marcar_tarefa_concluida(indice_tarefa)
            self.listar_tarefas()

    def listar_tarefas(self):
        tarefas = self.gerenciador_tarefas.listar_tarefas()
        self.listbox_tarefas.delete(0, tk.END)
        for tarefa in tarefas.split('\n'):
            self.listbox_tarefas.insert(tk.END, tarefa)

    def iniciar(self):
        self.janela_principal.mainloop()


interface = InterfaceGrafica()
interface.iniciar()

