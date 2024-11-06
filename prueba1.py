import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import Button

import mysql.connector #SQL
# Conexion a SQL local
conexion = mysql.connector.connect(user = 'root', 
                                   password = 'root', 
                                   host ='localhost', 
                                   database = 'PRUEBA', 
                                   port = '3306')
print(conexion)
cursor = conexion.cursor()
# Comunicacion del terminal hacia SQL
cursor.execute
(
    '''
        CREATE TABLE IF NOT EXISTS datos_serial
        (
            id INT AUTO_INCREMENT PRIMARY KEY,
            Mensaje_Serial LONGTEXT,
            Tiempo TIMESTAMP DEFAULT CURRENT TIMESTAMP
        )
    '''
)
interfaz = tk.Tk()
interfaz.config(width=1000, height=1000, background= "dim gray")
interfaz.mainloop()
conexion.close()