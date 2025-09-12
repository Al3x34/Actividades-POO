import tkinter as tk

# Crear la ventana
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")
ventana.geometry("300x250")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack()

# Campo de texto
entrada = tk.Entry(ventana)
entrada.pack()

# Lista para mostrar datos
lista = tk.Listbox(ventana)
lista.pack(pady=10)

# Función para agregar datos
def agregar():
    texto = entrada.get()
    if texto != "":
        lista.insert(tk.END, texto)
        entrada.delete(0, tk.END)

# Función para limpiar datos
def limpiar():
    seleccion = lista.curselection()
    if seleccion:
        lista.delete(seleccion)
    else:
        lista.delete(0, tk.END)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar)
btn_agregar.pack(pady=5)

btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
btn_limpiar.pack(pady=5)

# Mantener ventana abierta
ventana.mainloop()
