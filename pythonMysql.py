import tkinter as tk


#importar modulos restantes de tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from clientes import *
from conexion import * 

class FormularioClientes: 
    
  global textBoxId
  def Formulario():
        
    try:
      base = Tk()
      base.geometry("1200x300")
      base.title("Formulario python")
      
      groupBox = LabelFrame(base, text = "Datos del personal", padx=5,pady=5)
      groupBox.grid(row=0, column=0, padx=10, pady=10)
      
      #ID
      labelId = Label(groupBox, text = "Id: ", width = 13, font = ("arial", 12)).grid(row=0, column=0)
      textBoxId = Entry(groupBox)
      textBoxId.grid(row = 0, column = 1)
      
      #Nombre
      labelNombre = Label(groupBox, text = "Nombre: ", width = 13, font = ("arial", 12)).grid(row=1, column=0)
      textBoxNombre = Entry(groupBox)
      textBoxNombre.grid(row = 1, column = 1)
      
      #Apellidos
      labelApellidos = Label(groupBox, text = "Nombre: ", width = 13, font = ("arial", 12)).grid(row=2, column=0)
      textBoxApellidos = Entry(groupBox)
      textBoxApellidos.grid(row = 2, column = 1)
      
      #sexo
      labelSexo = Label(groupBox, text = "Sexo: ", width = 13, font = ("arial", 12)).grid(row=3, column=0)
      selection_sex = tk.StringVar()
      combo = ttk.Combobox(groupBox, values = ["Maculino", "Femenino"], textvariable = selection_sex)
      combo.grid(row = 3, column=1)
      selection_sex.set("Selecciona un sexo")
      
      Button(groupBox, text = "Guardar", width = 10).grid(row = 4, column = 0)
      Button(groupBox, text = "Modificar", width = 10).grid(row = 4, column = 1)
      Button(groupBox, text = "Eliminar", width = 10).grid(row = 4, column = 2)
      
      #groupBox mostrar
      
      groupBox = LabelFrame(base, text = "Lista del personal", padx = 5, pady = 5)
      groupBox.grid(row=0, column=1, padx=5, pady=5)
      
      #crear un treeview
      
      #configurar las columnas
      tree = ttk.Treeview(groupBox, columns = ("Id", "Nombres", "Apellidos", "Sexo"), show='headings', height=5,)
      tree.column("#1", anchor=CENTER)
      tree.heading("#1", text="Id")
      
      tree.column("#2", anchor=CENTER)
      tree.heading("#2", text="Nombres")
      
      tree.column("#3", anchor=CENTER)
      tree.heading("#3", text="Apellidos")
      
      tree.column("#4", anchor=CENTER)
      tree.heading("#4", text="Sexo")
      
      tree.pack()
      
      base.mainloop()
            
    except ValueError as error:
      print("Error al mostrar la interfaz, error: {}".format(error))
  
  Formulario()      