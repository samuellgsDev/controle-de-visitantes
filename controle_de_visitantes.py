import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import csv


class CondominioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Controle de Visitantes")

        # Inicialização de variáveis
        self.nome_var = tk.StringVar()
        self.doc_var = tk.StringVar()
        self.placa_var = tk.StringVar()
        self.consulta_doc_var = tk.StringVar()
        self.image_path = None
        self.thumbnail = None  # Miniatura da imagem

        # Criação dos elementos da interface
        self.label_nome = tk.Label(root, text="Nome:")
        self.label_doc = tk.Label(root, text="Documento de Identificação:")
        self.label_placa = tk.Label(root, text="Placa do Veículo:")
        self.label_consulta_doc = tk.Label(
            root, text="Consultar por Documento:")

        self.entry_nome = tk.Entry(root, textvariable=self.nome_var)
        self.entry_doc = tk.Entry(root, textvariable=self.doc_var)
        self.entry_placa = tk.Entry(root, textvariable=self.placa_var)
        self.entry_consulta_doc = tk.Entry(
            root, textvariable=self.consulta_doc_var)

        self.btn_registrar = tk.Button(
            root, text="Registrar Visitante", command=self.registrar_visitante)
        self.btn_selecionar_imagem = tk.Button(
            root, text="Selecionar Imagem", command=self.selecionar_imagem)
        self.btn_consultar = tk.Button(
            root, text="Consultar Visitante", command=self.consultar_visitante)

        # Área para visualizar a miniatura da imagem
        self.thumbnail_label = tk.Label(root)
        self.thumbnail_label.grid(row=7, column=0, columnspan=2)

        # Posicionamento dos elementos na interface
        self.label_nome.grid(row=0, column=0)
        self.entry_nome.grid(row=0, column=1)

        self.label_doc.grid(row=1, column=0)
        self.entry_doc.grid(row=1, column=1)

        self.label_placa.grid(row=2, column=0)
        self.entry_placa.grid(row=2, column=1)
        self.btn_selecionar_imagem.grid(row=3, column=0, columnspan=2)

        self.label_consulta_doc.grid(row=5, column=0)
        self.entry_consulta_doc.grid(row=5, column=1)

        self.btn_registrar.grid(row=4, column=0, columnspan=2)
        self.btn_consultar.grid(row=6, column=0, columnspan=2)
        self.thumbnail_label.grid(row=8, column=0, columnspan=2)

        # Criação do arquivo CSV para armazenar os dados dos visitantes
        self.arquivo_csv = "visitantes.csv"
        self.criar_arquivo_csv()

    def criar_arquivo_csv(self):
        try:
            with open(self.arquivo_csv, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Nome", "Documento", "Placa", "Imagem"])
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao criar o arquivo CSV: {e}")

    def registrar_visitante(self):
        nome = self.nome_var.get()
        doc = self.doc_var.get()
        placa = self.placa_var.get()

        if nome and doc and placa and self.image_path:
            with open(self.arquivo_csv, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([nome, doc, placa, self.image_path])
            messagebox.showinfo(
                "Registro", "Visitante registrado com sucesso!")
            self.limpar_campos()
        else:
            messagebox.showerror(
                "Erro", "Preencha todos os campos e selecione uma imagem.")

    def consultar_visitante(self):
        consulta_doc = self.consulta_doc_var.get()
        if not consulta_doc:
            messagebox.showerror(
                "Erro", "Informe o número de documento para a consulta.")
            return

        try:
            with open(self.arquivo_csv, newline="") as file:
                reader = csv.reader(file)
                next(reader)  # Pula a primeira linha (cabeçalho)
                for row in reader:
                    if row[1] == consulta_doc:
                        self.mostrar_informacoes_visitante(row)
                        return
                messagebox.showerror("Erro", "Visitante não encontrado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao consultar visitante: {e}")

    def selecionar_imagem(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.gif *.bmp *.ppm *.pgm")])
        if file_path:
            self.image_path = file_path
            self.mostrar_imagem_miniatura(file_path)

    def mostrar_imagem_miniatura(self, image_path):
        if image_path:
            image = Image.open(image_path)
            # Redimensionar a imagem para uma miniatura
            image.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(image)
            self.thumbnail_label.config(image=photo)
            self.thumbnail_label.image = photo

    def mostrar_informacoes_visitante(self, visitante):
        nome = visitante[0]
        doc = visitante[1]
        placa = visitante[2]
        image_path = visitante[3]

        # Criar uma nova janela para exibir as informações e a miniatura da imagem
        info_window = tk.Toplevel(self.root)
        info_window.geometry("400x400")
        info_window.title("Informações do Visitante")

        info_label = tk.Label(
            info_window, text=f"Nome: {nome}\nDocumento: {doc}\nPlaca: {placa}")
        info_label.pack()

        if image_path:
            image = Image.open(image_path)
            # Redimensionar a imagem para uma miniatura
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)

            thumbnail_label = tk.Label(info_window, image=photo)
            thumbnail_label.image = photo
            thumbnail_label.pack()

    def limpar_campos(self):
        self.nome_var.set("")
        self.doc_var.set("")
        self.placa_var.set("")
        self.image_path = ("")
        self.thumbnail_label.config(image=None)


def main():
    root = tk.Tk()
    app = CondominioApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
