import tkinter as tk
from PIL import Image, ImageTk

# ---------- SISTEMA DE USUÁRIO ----------
def cadastrar():
    user = entry_user.get()
    senha = entry_pass.get()
    
    with open("usuarios.txt", "a") as arq:
        arq.write(f"{user},{senha}\n")
        
    status.config(text="Conta criada!")

def login():
    user = entry_user.get()
    senha = entry_pass.get()
    
    try:
        with open("usuarios.txt", "r") as arq:
            for linha in arq:
                u, s = linha.strip().split(",")
                if u == user and s == senha:
                    abrir_galeria()
                    return
    except:
      pass
    
    status.config(text="Erro no login")

# ---------- GALERIA ----------
imagens = ["foto1.png", "foto2.png", "foto3.png"]
index = 0

def mostrar_imagem():
    global img_tk
    img = Image.open(imagens[index])
    img = img.resize((250, 250))
    img_tk = ImageTk.PhotoImage(img)
    label_img.config(image=img_tk)

def proxima_imagem():
    global index
    index += 1
    if index < len(imagens):
         mostrar_imagem()
    else:
         abrir_carta()
         
# ---------- CARTA ----------
def abrir_carta():
    limpar_tela()
    
    tk.Label(janela, text=" Uma cartinha pra você ", font=("Arial", 14)).pack(pady=20)
    
    def mostrar_texto():
        texto = tk.Label(janela, text="Você é muito especial! \nObrigado por estar aqui.",
                    wraplength=250, justify="center")
        texto.pack(pady=20)

    tk.Button(janela, text="Abrir carta", command=mostrar_texto).pack()

# ---------- TROCA DE TELA ----------
def limpar_tela():
    for widget in janela.winfo_children():
        widget.destroy()

def abrir_galeria():
    limpar_tela()
    
    global label_img 
    label_img = tk.Label(janela)
    label_img.pack(pady=20)
    
    mostrar_imagem()
    
    tk.Button(janela, text=" Próxima", command=proxima_imagem).pack()

# ---------- INTERFACE LOGIN ----------
janela = tk.Tk()
janela.title("Abajur Inteligente")
janela.geometry("300x400")

tk.Label(janela, text="Usuário").pack()
entry_user = tk.Entry(janela)
entry_user.pack()

tk.Label(janela, text="Senha").pack()
entry_pass = tk.Entry(janela, show="*")
entry_pass.pack()

tk.Button(janela, text="Cadastrar", command=cadastrar).pack(pady=5)
tk.Button(janela, text="Login", command=login).pack(pady=5)

status = tk.Label(janela, text="")
status.pack()

janela.mainloop()