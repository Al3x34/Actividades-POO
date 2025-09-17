import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry   # si no lo tienes: pip install tkcalendar

# Ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# ---- Lista de eventos ----
cols = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
tree.pack(fill="both", expand=True, padx=10, pady=10)

# ---- Entradas ----
frame_form = tk.Frame(root)
frame_form.pack(pady=5)

tk.Label(frame_form, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
cal_fecha = DateEntry(frame_form, date_pattern="yyyy-mm-dd")
cal_fecha.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Hora:").grid(row=0, column=2, padx=5, pady=5)
ent_hora = tk.Entry(frame_form, width=10)
ent_hora.grid(row=0, column=3, padx=5, pady=5)

tk.Label(frame_form, text="Descripción:").grid(row=1, column=0, padx=5, pady=5)
ent_desc = tk.Entry(frame_form, width=40)
ent_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)

# ---- Funciones ----
def agregar_evento():
    fecha = cal_fecha.get()
    hora = ent_hora.get()
    desc = ent_desc.get()
    if fecha and hora and desc:
        tree.insert("", "end", values=(fecha, hora, desc))
        ent_hora.delete(0, tk.END)
        ent_desc.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Completa todos los campos.")

def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        ok = messagebox.askyesno("Confirmar", "¿Eliminar evento?")
        if ok:
            tree.delete(seleccionado)
    else:
        messagebox.showinfo("Aviso", "Selecciona un evento.")

# ---- Botones ----
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Agregar Evento", command=agregar_evento).pack(side="left", padx=10)
tk.Button(frame_btn, text="Eliminar Evento", command=eliminar_evento).pack(side="left", padx=10)
tk.Button(frame_btn, text="Salir", command=root.quit).pack(side="left", padx=10)

root.mainloop()
