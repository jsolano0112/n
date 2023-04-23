import tkinter as tk
from tkinter import ttk, messagebox

class Jugador:
    def eventoParaIniciar(self):
        if nombreJugador.get() == "":
            mensajeError = 'No has ingresado tu nombre.'
            messagebox.showerror('Falta entrada de datos', mensajeError)
            print("vacío")
        else:
            print("Se quitó la ventana")
            ventanatk.withdraw()

    def nombreDelJugador(self):
        return nombreJugador.get()



#Ventana TKinter
ventanatk = tk.Tk()
ventanatk.geometry("300x100")
ventanatk.title('Jueguito del gusanito🐛')
ventanatk.resizable(0,0)

#para centrar
altura = ventanatk.winfo_reqheight()
anchura = ventanatk.winfo_reqwidth()
altura_pantalla = ventanatk.winfo_screenheight()
anchura_pantalla = ventanatk.winfo_screenwidth()
print(f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
x = (anchura_pantalla // 2) - (anchura // 2)
y = (altura_pantalla // 2) - (altura // 2)

ventanatk.geometry(f"+{x}+{y}")

#Labels
bienvenido = tk.Label(ventanatk, text='Bienvenido')
bienvenido.pack()

pregunta = tk.Label(ventanatk, text='Ingresa tu nombre')
pregunta.pack()

#Textbox para recibir nombre del jugador
nombreJugador = ttk.Entry(ventanatk, width=20)
nombreJugador.pack()


