import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import Button
from tkinter import ttk
import time
import mysql.connector #SQL
# Conexion a SQL local
conexion = mysql.connector.connect(user = 'root', 
                                   password = 'root', 
                                   host ='localhost', 
                                   database = 'GUADALUPANA', 
                                   port = '3306')
print(conexion)
cursor = conexion.cursor()
cursor.execute
(
    '''
        CREATE TABLE IF NOT EXISTS pruebas
        (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Mensaje LONGTEXT,
            Tiempo TIMESTAMP DEFAULT CURRENT TIMESTAMP
        )
    '''
)
def Guardar1(Mensaje):
    try:
        conexion = mysql.connector.connect(user = 'root', 
                                   password = 'root', 
                                   host ='localhost', 
                                   database = 'GUADALUPANA', 
                                   port = '3306'
    )
        cursor1.execute('INSERT INTO pruebas (Mensaje) VALUES (%s)', (Mensaje,))
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
    finally:
        cursor1.close()
        conexion.close()  
cursor1 = conexion.cursor()
# Comunicacion del terminal hacia SQL
cursor1.execute
(
    '''
       CREATE TABLE IF NOT EXISTS `GUADALUPANA`.`datos`
        (
            `id_datos` INT AUTO_INCREMENT,
            `CUI` INT NOT NULL,
            `Nombre` VARCHAR(20),
            `Apellido` VARCHAR(20),
            `Direccion` VARCHAR(100),
            `Telefono` VARCHAR(20),
            `Plaza` VARCHAR(35),
            PRIMARY KEY (id_datos),
            CONSTRAINT CUI FOREIGN KEY (CUI)
            REFERENCES GUADALUPANA.Escolaridad(CUI)
        )
    '''
)
cursor2 = conexion.cursor()
# Comunicacion del terminal hacia SQL
cursor2.execute
(
    '''
       CREATE TABLE IF NOT EXISTS `GUADALUPANA`.`Escolaridad`
        (
            `id_esc` INT,
            `CUI` INT NOT NULL,
            `Grado` TEXT NOT NULL,
            PRIMARY KEY (CUI)
        )
    '''
)
cursor3 = conexion.cursor()
cursor3.execute
(
    '''
    CREATE TABLE IF NOT EXISTS `GUADALUPANA`.`Departamento`
    (
	    `id_depart` INT,
	    `Departamento` INT NOT NULL,
        PRIMARY KEY (id_depart)
    )
    '''
)
def Guardar(CUI):
    try:
        conexion = mysql.connector.connect(user = 'root', 
                                   password = 'root', 
                                   host ='localhost', 
                                   database = 'GUADALUPANA', 
                                   port = '3306'
    )
        cursor1.execute('INSERT INTO datos (CUI) VALUES (%s)', (CUI,))
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
    finally:
        cursor1.close()
        conexion.close()       

''''''
def Guardar(Nombre):
    try:
        conexion = mysql.connector.connect(user = 'root', 
                                   password = 'root', 
                                   host ='localhost', 
                                   database = 'GUADALUPANA', 
                                   port = '3306'
    )
        cursor1.execute('INSERT INTO datos (Nombre) VALUES (%s)', (Nombre,))
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
    finally:
        cursor1.close()
        conexion.close()     
def Guardar(Apellido):
    try:
        conexion = mysql.connector.connect(user = 'root', 
                                   password = 'root', 
                                   host ='localhost', 
                                   database = 'GUADALUPANA', 
                                   port = '3306'
    )
        cursor1.execute('INSERT INTO datos (Apellido) VALUES (%s)', (Apellido,))
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
    finally:
        cursor1.close()
        conexion.close()  
 
def Guardar(Telefono):
    try:
        conexion = mysql.connector.connect(user = 'root', 
                                   password = 'root', 
                                   host ='localhost', 
                                   database = 'GUADALUPANA', 
                                   port = '3306'
    )
        cursor1.execute('INSERT INTO datos (Telefono) VALUES (%s)', (Telefono,))
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
    finally:
        cursor1.close()
        conexion.close()   

def Guardar(Escolaridad):
    try:
        conexion = mysql.connector.connect(user = 'root', 
                                   password = 'root', 
                                   host ='localhost', 
                                   database = 'GUADALUPANA', 
                                   port = '3306'
    )
        cursor1.execute('INSERT INTO Escolaridad (Escolaridad) VALUES (%s)', (Escolaridad,))
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
    finally:
        cursor1.close()
        conexion.close()   
def Guardar(Plaza):
    try:
        conexion = mysql.connector.connect(user = 'root', 
                                   password = 'root', 
                                   host ='localhost', 
                                   database = 'GUADALUPANA', 
                                   port = '3306'
    )
        cursor1.execute('INSERT INTO datos (Plaza) VALUES (%s)', (Plaza))
        conexion.commit()
    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
    finally:
        cursor1.close()
        conexion.close()   
''''''
interfaz = tk.Tk()
interfaz.config(width=1000, height=1000, background= "light sky blue")
interfaz.title("Cooperativa Guadalupana")
messagebox.showwarning("Bienvenido")
title_label = tk.Label(interfaz, text="Cooperativa Guadalupana", font=("Helvetica", 20, "bold"), background="azure")
title_label.place(x=350, y= 10)


title_label2 = tk.Label(interfaz, text="Información de candidatos", font=("Helvetica", 15, "bold"), background="gainsboro")
title_label2.place(x=50, y= 200)

CUI_label = tk.Label(interfaz, text="CUI", background="white")
CUI_label.place(x=50, y= 250)

CUI_text = ttk.Entry(show="*")
CUI_text.place(x=50, y= 270)

Nombre_label = tk.Label(interfaz, text="Nombre", background="white")
Nombre_label.place(x=50, y= 285)

Nombre_text = ttk.Entry()
Nombre_text.place(x=50, y= 310)

Apellido_label = tk.Label(interfaz, text="Apellido", background="white")
Apellido_label.place(x=50, y= 335)

Apellido_text = ttk.Entry()
Apellido_text.place(x=50, y= 365)

Direccion_label = tk.Label(interfaz, text="Direccion", background="white")
Direccion_label.place(x=50, y= 385)

Direccion_text = ttk.Entry()
Direccion_text.place(x=50, y= 410)

Tele_label = tk.Label(interfaz, text="Telefono", background="white")
Tele_label.place(x=50, y= 425)

Tele_text = ttk.Entry()
Tele_text.place(x=50, y= 445)

#
Escolaridad_label = tk.Label(interfaz, text="Escolaridad", background="white")
Escolaridad_label.place(x=300, y= 285)

Escolaridad_box = ttk.Combobox(
    state="readonly",
    values=["Primaria", "Basicos", "Diversificado", "Universidad", "Maestria"]
)
def seleccion():
    selecc = Escolaridad_box.get()
    messagebox.showinfo(
        title="Informacion seleccionada"
    )
Escolaridad_box.bind("<<ComboboxSelected>>", seleccion)
Escolaridad_box.place(x=300, y= 310)

Plaza_label = tk.Label(interfaz, text="Plaza", background="white")
Plaza_label.place(x=300, y= 345)

Plaza_text = ttk.Entry()
Plaza_text.place(x=300, y= 375)

Guardar_boton = tk.Button (interfaz, text="Guardar", command=Guardar, font=("Helvetica", 14), background="lawn green")
Guardar_boton.place(x=250, y=500)


#time.sleep(1)

interfaz.mainloop()
conexion.close()
