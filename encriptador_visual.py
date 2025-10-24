import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import numpy as np
import math
from tkinter import messagebox, Toplevel, font
import sys
import os
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
# --- 1. Lógica del Encriptador----
MODULO = 27
alfabeto = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
    'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
    'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
    'Z': 25, ' ': 26
}
num_a_letra = {valor: llave for llave, valor in alfabeto.items()}

# --- 2. Funciones de Lógica  ---

def procesar_matriz_clave():
    """
    Lee la matriz clave desde el GRID visual y el TAMAÑO seleccionado
    en los radio buttons.
    """
    try:
        # Obtener el tamaño (2 o 3) del radio button
        tam = tam_matriz_var.get()
        numeros = []
        
        # Recorrer solo los cuadros necesarios según el tamaño
        for i in range(tam):
            for j in range(tam):
                # Si el cuadro está vacío, usar "0", si no, usar el valor
                valor_str = matrix_entries[i][j].get() or "0"
                numeros.append(int(valor_str))
        
        
        matriz = np.array(numeros).reshape(tam, tam)
        
        determinante = round(np.linalg.det(matriz))
        if determinante == 0:
            messagebox.showerror("Error de Matriz", "La matriz clave no es invertible (su determinante es 0).")
            return None
        
        if math.gcd(int(determinante), MODULO) != 1:
            messagebox.showerror("Error de Matriz", f"El determinante ({determinante}) comparte factores con {MODULO} (ej: es múltiplo de 3). No se puede usar para aritmética modular.")
            return None
            
        return matriz
    except ValueError:
        messagebox.showerror("Error de Formato", "Por favor, ingrese solo NÚMEROS en los cuadros de la matriz.")
        return None
    except Exception as e:
        messagebox.showerror("Error de Matriz", f"Un error inesperado ocurrió: {e}")
        return None

def encriptar_mensaje():
    mensaje = entrada_mensaje.get("1.0", "end-1c").upper()
    matriz_clave = procesar_matriz_clave()
    
    if matriz_clave is None: return
    tam_matriz = matriz_clave.shape[0]
    numeros = [alfabeto.get(letra, 26) for letra in mensaje]
    while len(numeros) % tam_matriz != 0:
        numeros.append(26)

    resultado_numeros = []
    for i in range(0, len(numeros), tam_matriz):
        vector = np.array(numeros[i:i+tam_matriz])
        vector_cifrado = (matriz_clave.dot(vector) % MODULO).astype(int)
        resultado_numeros.extend(vector_cifrado)
        
    resultado_str = "".join([num_a_letra.get(num, '?') for num in resultado_numeros])
    
    area_resultado.config(state='normal')
    area_resultado.delete("1.0", tk.END)
    area_resultado.insert(tk.END, resultado_str)
    area_resultado.config(state='disabled')

def desencriptar_mensaje():
    mensaje_cifrado_texto = entrada_mensaje.get("1.0", "end-1c").upper()
    # --- MODIFICADO ---
    matriz_clave = procesar_matriz_clave()
    
    if matriz_clave is None: return

    # El resto de la función es idéntico...
    try:
        inversa_regular = np.linalg.inv(matriz_clave)
        determinante = round(np.linalg.det(matriz_clave))
        det_inverso = pow(determinante, -1, MODULO)
        adjunta = inversa_regular * determinante
        matriz_inversa_mod = (adjunta * det_inverso) % MODULO
        
        numeros_cifrados = [alfabeto.get(letra, 26) for letra in mensaje_cifrado_texto]
        tam_matriz = matriz_clave.shape[0]
        
        numeros_originales = []
        for i in range(0, len(numeros_cifrados), tam_matriz):
            vector_cifrado = np.array(numeros_cifrados[i:i+tam_matriz])
            vector_original = (matriz_inversa_mod.dot(vector_cifrado) % MODULO)
            numeros_originales.extend(np.round(vector_original).astype(int))

        texto_final = "".join([num_a_letra.get(num, '?') for num in numeros_originales])
        
        area_resultado.config(state='normal')
        area_resultado.delete("1.0", tk.END)
        area_resultado.insert(tk.END, texto_final.strip())
        area_resultado.config(state='disabled')
        
    except Exception as e:
        messagebox.showerror("Error al Desencriptar", f"No se pudo procesar el mensaje. ¿Estás seguro que la clave es correcta? \nError: {e}")

# --- 3. NUEVA Función para la Interfaz ---

def actualizar_grid_matriz():
    tam = tam_matriz_var.get()
    for i in range(3):
        for j in range(3):
            entry = matrix_entries[i][j]
            if i < tam and j < tam:
                entry.config(state='normal', bg='white')
            else:
                entry.config(state='disabled', bg='#f0f0f0')

# --- ¡FUNCIÓN DE CRÉDITOS---
def mostrar_creditos(event=None): 
    """Crea la ventana emergente de créditos."""
    ventana_creditos = Toplevel(ventana)
    ventana_creditos.title("Desarrolladores")
    ventana_creditos.geometry("500x500")
    ventana_creditos.resizable(False, False)
    ventana_creditos.grab_set()
    
    tk.Label(ventana_creditos, text="Proyecto de Álgebra Lineal", font=("Helvetica", 14, "bold")).pack(pady=10)
    tk.Label(ventana_creditos, text="Integrantes:", font=("Helvetica", 12, "italic")).pack()
    tk.Label(ventana_creditos, text="-------------------------------------------------").pack()
    tk.Label(ventana_creditos, text="Jeimy Vanesa Gómez López                        0903-25-16221").pack()
    tk.Label(ventana_creditos, text="Ivana Marcela Malin de León                      0903-25-18673").pack()
    tk.Label(ventana_creditos, text="Joaquín Daniel Maldonado Velasquez       0903-25-14491").pack()
    tk.Label(ventana_creditos, text="Rony Alberto Méndez Fuentes                    0903-25-29637").pack()
    try:
        
        ruta_logo_relativa = "logo.png" 
        ruta_logo = resource_path(ruta_logo_relativa)
        
        # Abrir la imagen usando PIL
        img = Image.open(ruta_logo)
        # Redimensionar la imagen si es demasiado grande (opcional, ajusta tamaño si es necesario)
        img = img.resize((200, 200), Image.LANCZOS) # Ajusta 100, 100 al tamaño deseado
        
        # Convertir a formato PhotoImage para Tkinter
        logo_tk = ImageTk.PhotoImage(img)
        
        # Guardar una referencia a la imagen para evitar que se borre (garbage collection)
        ventana_creditos.logo_referencia = logo_tk 
        
        # Mostrar la imagen en un Label
        label_logo = tk.Label(ventana_creditos, image=logo_tk)
        label_logo.pack(pady=5)
    except FileNotFoundError:
        messagebox.showwarning("Error de Imagen", f"No se encontró el archivo de logo: {ruta_logo}")
    except Exception as e:
        messagebox.showwarning("Error de Imagen", f"No se pudo cargar el logo: {e}")

    
    boton_cerrar = tk.Button(ventana_creditos, text="Cerrar", command=ventana_creditos.destroy)
    boton_cerrar.pack(pady=15)


# --- 4. Creación de la Ventana Principal  ---

ventana = tk.Tk()
ventana.title("Encriptador con Álgebra Lineal")
ventana.geometry("550x600")
ventana.resizable(False, False)

tk.Label(ventana, text="Encriptador y Desencriptador de Mensajes", font=("Helvetica", 14, "bold")).pack(pady=10)
tk.Label(ventana, text="Mensaje Original (para encriptar) o Cifrado (para desencriptar):").pack(pady=(10,0))
entrada_mensaje = tk.Text(ventana, height=5, width=50)
entrada_mensaje.pack()

frame_seleccion = tk.Frame(ventana)
frame_seleccion.pack(pady=5)
tk.Label(frame_seleccion, text="Tamaño de la Matriz Clave:").pack(side=tk.LEFT)
tam_matriz_var = tk.IntVar(value=2)
radio_2x2 = tk.Radiobutton(frame_seleccion, text="2x2", variable=tam_matriz_var, value=2, command=actualizar_grid_matriz)
radio_2x2.pack(side=tk.LEFT)
radio_3x3 = tk.Radiobutton(frame_seleccion, text="3x3", variable=tam_matriz_var, value=3, command=actualizar_grid_matriz)
radio_3x3.pack(side=tk.LEFT)

tk.Label(ventana, text="Matriz Clave:").pack()
frame_matriz = tk.Frame(ventana)
frame_matriz.pack()

matrix_entries = []
for i in range(3):
    fila_entries = []
    for j in range(3):
        entry = tk.Entry(frame_matriz, width=5, font=("Helvetica", 12), justify='center')
        entry.grid(row=i, column=j, padx=5, pady=5)
        fila_entries.append(entry)
    matrix_entries.append(fila_entries)

# --- Sección de Botones ---
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

boton_encriptar = tk.Button(frame_botones, text="Encriptar", command=encriptar_mensaje, font=("Helvetica", 10, "bold"))
boton_encriptar.pack(side=tk.LEFT, padx=10)

boton_desencriptar = tk.Button(frame_botones, text="Desencriptar", command=desencriptar_mensaje, font=("Helvetica", 10, "bold"))
boton_desencriptar.pack(side=tk.LEFT, padx=10)

tk.Label(ventana, text="Resultado:").pack(pady=(10,0))
area_resultado = tk.Text(ventana, height=5, width=50, state='disabled', bg="#f0f0f0")
area_resultado.pack(pady=(0, 10)) 


font_link = font.Font(family='Helvetica', size=12, underline=True)
label_creditos = tk.Label(ventana, text="Equipo de trabajo", fg="#1607F0", font=font_link, cursor="hand2")
label_creditos.pack(side=tk.BOTTOM, pady=10) 
label_creditos.bind("<Button-1>", mostrar_creditos) 

# --- LLAMADA INICIAL ---
# Llamamos a la función 1 vez al inicio para que ponga el estado default 2x2
actualizar_grid_matriz()

# Iniciar la aplicación
ventana.mainloop()