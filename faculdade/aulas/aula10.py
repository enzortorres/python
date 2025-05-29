'''class Pessoa:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        if isinstance(novo_nome,str) and len(novo_nome)> 0:
            self.__nome = novo_nome
        else:
            print('Nome inválido')
p = Pessoa('Thereza')
print(p.get_nome())

p.set_nome('Thereza Gondim')
print(p.get_nome())

p.set_nome('')
print(p.get_nome())

#-------------------------------------------------------------------

class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = preco

    def get_preco(self):
        return self.__preco

    def set_preco(self, novo_preco):
        if isinstance(novo_preco,(int,float) and novo_preco >= 0):
            self.__preco = novo_preco
        else:
            print('Preço inválido')

p = Produto('Lápis', 1.5)
print(p.get_preco())

p.set_preco(2.0)
print(p.get_preco())

#---------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__(self,login,senha,dica_usuario):
        self.__login = login
        self.__senha = senha
        self.__dica_usuario = dica_usuario

    def verificar_login(self,login,senha):
        if len(senha) < 4:
            return False
        return self.__login == login and self.__senha ==senha

    def get_dica_usuario(self):
        return self.__dica_usuario

    def redefinir_senha(self,nova_senha):
        if len(nova_senha) < 4:
            self.__senha = nova_senha
            return True
        return False

class TelaLogin:
    def __init__(self,master):
        self.__master = master
        master.title('Tele Login')
        master.geometry('400x400')

        self.usuario = Usuario('admin',1234,'A senha começa com .....')

        self.lbl_login = tk.Label(master,text='Login')
        self.lbl_login.pack()

        self.entrada = tk.Entry(master)
        self.entrada.pack()

        self.lbl_senha = tk.Label(master,text='Senha')
        self.lbl_senha.pack()

        vs = master.register(self.limitar_caracteres)
        self.entry_senha = tk.Entry(master, show='*',validate='key',validatecommand=(vs,'%P'))
        self.entry_senha.pack()

        self.btn_login = tk.Button(master,text='Entrar',command='self.login')
        self.btn_login.pack()

        self.btn_esqueceu = tk.Button(master,text='Esqueceu',command='self.recuperar_senha')
        self.btn_esqueceu.pack()

    def limitar_caracteres(self,conteudo):
        return len(conteudo) <= 4

    def login(self):
        login = self.entry.login.get()
        senha = self.entry_senha.get()

        if len(senha) < 4:
            messagebox.showerror('Senha','A senha de conter.....')
            return

        if self.usuario.verificar_login(login,senha):
            messagebox.showinfo('Login','Logado com sucesso')
            self.master.destroy()
        else:
            messagebox.showerror('Login','login ou senha inválida')

    def recuperar_senha(self):
        resposta = messagebox.askyesno('Recuperar senha','Deseja ver a dica da senha?')
        if resposta:
            dica = self.usuario.get_dica_senha()
            messagebox.showinfo('Senha',dica)
        else:
            self.tela_redefinir_senha()

    def tela_redefinir_senha(self):
        nova_janela = tk.TopLevel(self.master)
        nova_janela.resizable(False,False)
        nova_janela.title('Tela Redefinir Senha')
        nova_janela.geometry('400x400')

        lbl_nova_senha = tk.Label(nova_janela,text='Nova Senha')
        lbl_nova_senha.pack()

        vs = self.master.register(self.limitar_caracteres)
        self.entry_senha = tk.Entry(nova_janela, show='*', validate='key', validatecommand=(vs, '%P'))
        self.entry_senha.pack()

        btn_confirmar = tk.Button(nova_janela,text='Confirmar',command=self.redefinir_senha)
        btn_confirmar.pack(pady=5)

    def redefinir_senha(self):
        nova_senha = self.entry_nova_senha.get()
        if self.usuario.redefinir_senha(nova_senha):
            messagebox.showinfo('Senha','Senha redefinida')
        else:
            messagebox.showerror('Erro','Senha incorreto')
if __name__ == '__main__':
    root = tk.Tk()
    app = TelaLogin(root)
    root.mainloop()'''

import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__(self, login, senha, dica_senha="Dica padrão"):
        self.__login = login
        self.__senha = senha
        self.__dica_senha = dica_senha

    def verifica_login(self, login, senha):
        if len(senha) < 4:
            return False
        return self.__login == login and self.__senha == senha

    def get_dica_senha(self):
        return self.__dica_senha

    def redefinir_senha(self, nova_senha):
        if len(nova_senha) >= 4:
            self.__senha = nova_senha
            return True
        return False

class TelaLogin:
    def __init__(self, master):
        self.master = master
        master.title('Tela Login')
        master.geometry('400x400')

        self.usuario = Usuario('admin', '1234', 'É o número padrão')

        self.lbl_login = tk.Label(master, text='Login')
        self.lbl_login.pack()

        self.entry_login = tk.Entry(master)
        self.entry_login.pack()

        self.lbl_senha = tk.Label(master, text='Senha')
        self.lbl_senha.pack()

        vs = master.register(self.limitar_caracteres)
        self.entry_senha = tk.Entry(master, show='*', validate='key', validatecommand=(vs, '%P'))
        self.entry_senha.pack()

        self.btn_login = tk.Button(master, text='Entrar', command=self.login)
        self.btn_login.pack(pady=5)

        self.btn_esqueceu = tk.Button(master, text='Esqueceu a senha?', command=self.recuperar_senha)
        self.btn_esqueceu.pack(pady=5)

    def limitar_caracteres(self, conteudo):
        return len(conteudo) <= 4

    def login(self):
        login = self.entry_login.get()
        senha = self.entry_senha.get()

        if len(senha) < 4:
            messagebox.showwarning('Senha fraca', 'A senha deve conter pelo menos 4 caracteres.')
            return

        if self.usuario.verifica_login(login, senha):
            messagebox.showinfo('Login', 'Logado com sucesso!')
            self.master.destroy()
        else:
            messagebox.showerror('Erro', 'Login ou senha inválidos.')

    def recuperar_senha(self):
        resposta = messagebox.askyesno('Recuperar Senha', 'Deseja ver a dica da senha?')
        if resposta:
            dica = self.usuario.get_dica_senha()
            messagebox.showinfo('Dica da Senha', f'{dica}')
        else:
            self.tela_redefinir_senha()

    def tela_redefinir_senha(self):
        nova_janela = tk.Toplevel(self.master)
        nova_janela.resizable(False, False)
        nova_janela.geometry('400x200')
        nova_janela.title('Redefinir Senha')

        lbl_nova_senha = tk.Label(nova_janela, text='Nova Senha')
        lbl_nova_senha.pack()

        vs = self.master.register(self.limitar_caracteres)
        self.entry_nova_senha = tk.Entry(nova_janela, show='*', validate='key', validatecommand=(vs, '%P'))
        self.entry_nova_senha.pack()

        btn_confirmar = tk.Button(nova_janela, text='Confirmar', command=self.redefinir_senha)
        btn_confirmar.pack(pady=10)

    def redefinir_senha(self):
        nova_senha = self.entry_nova_senha.get()
        if self.usuario.redefinir_senha(nova_senha):
            messagebox.showinfo('Sucesso', 'Senha redefinida com sucesso!')
        else:
            messagebox.showerror('Erro', 'A senha deve conter pelo menos 4 caracteres.')


if __name__ == '__main__':
    root = tk.Tk()
    app = TelaLogin(root)
    root.mainloop()




